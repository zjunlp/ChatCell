import torch
from random import choice
from datasets import Dataset, DatasetDict
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, Seq2SeqTrainer, Seq2SeqTrainingArguments
import numpy as np
from rouge import Rouge
import os
from datasets import load_dataset, load_metric
import json

os.environ["WANDB_DISABLED"]="true"
metric = load_metric("rouge")

train_json_path = ""
valid_json_path = ""
tokenizer_path=""
model_path=""
batch_size = 8
output_dir=""


tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)

model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
print(len(tokenizer))

if model.config.vocab_size !=len(tokenizer) :
    print("Token embeddings size is not len(tokenizer), resizing.")
    model.resize_token_embeddings(len(tokenizer))
else:
    print("Token embeddings size is already len(tokenizer), no need to adjust.")

# Function to load and prepare datasets

def load_dataset(train_json_path, valid_json_path):
    # Load datasets from JSON
    with open(train_json_path, 'r', encoding='utf-8') as file:
        train_data = json.load(file)
    train_dataset = Dataset.from_dict({'source': [item['source'] for item in train_data],
                                       'target': [item['target'] for item in train_data]})

    with open(valid_json_path, 'r', encoding='utf-8') as file:
        valid_data = json.load(file)
    valid_dataset = Dataset.from_dict({'source': [item['source'] for item in valid_data],
                                       'target': [item['target'] for item in valid_data]})

    # Combine into a DatasetDict
    dataset_dict = DatasetDict({
        'train': train_dataset,
        'valid': valid_dataset
    })

    return dataset_dict
# Load and prepare the dataset
dataset_dict = load_dataset(train_json_path, valid_json_path)
print(dataset_dict)

# Function to preprocess the datasets

def process_func(examples):
    inputs = examples['source']
    targets = examples['target']
    model_inputs = tokenizer(inputs)
    labels = tokenizer(targets)
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# Apply preprocessing

dataset_all = dataset_dict.map(process_func, batched=True)

print(dataset_all)
# Training arguments
args = Seq2SeqTrainingArguments(
    output_dir=output_dir,
    evaluation_strategy="steps",
    eval_steps=5000,
    logging_strategy="steps",
    logging_steps=100,
    save_strategy="steps",
    save_steps=5000,
    learning_rate=4e-5,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    weight_decay=0.01,
    save_total_limit=3,
    num_train_epochs=50,
    predict_with_generate=True,
    fp16=False,
    load_best_model_at_end=True,
    metric_for_best_model="rouge1",
)

# Function to compute metrics for evaluation

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    decoded_preds = tokenizer.batch_decode(predictions, skip_special_tokens=True)
    # Replace -100 in the labels as we can't decode them.
    labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    # Rouge expects a newline after each sentence
    decoded_preds = [pred.strip() for pred in decoded_preds]
    decoded_labels = [label.strip() for label in decoded_labels]

    
    # Compute ROUGE scores
    result = metric.compute(predictions=decoded_preds, references=decoded_labels,
                            use_stemmer=True)

    # Extract ROUGE f1 scores
    result = {key: value.mid.fmeasure * 100 for key, value in result.items()}
    
    # Add mean generated length to metrics
    prediction_lens = [np.count_nonzero(pred != tokenizer.pad_token_id)
                      for pred in predictions]
    result["gen_len"] = np.mean(prediction_lens)
    
    return {k: round(v, 4) for k, v in result.items()}
trainer = Seq2SeqTrainer(
    model=model,
    args=args,
    train_dataset=dataset_all['train'],
    eval_dataset=dataset_all['valid'],
    data_collator=DataCollatorForSeq2Seq(tokenizer=tokenizer),
    tokenizer=tokenizer,
    compute_metrics=compute_metrics
)

# Start training

trainer.train()
trainer.save_model()

