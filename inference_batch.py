from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    HfArgumentParser,
    Trainer,
    TrainingArguments,
    AutoModelForSeq2SeqLM,
)
import torch
import json
from tqdm import tqdm  
# Define paths and load the model and tokenizer

model_folder = ""
input_path=""
output_path=""
tokenizer = AutoTokenizer.from_pretrained(model_folder)
model = AutoModelForSeq2SeqLM.from_pretrained(model_folder)
print(f"Tokenizer vocabulary size: {len(tokenizer.vocab.keys())}")

# Determine the execution device based on availability of CUDA
if torch.cuda.is_available():
    device = torch.device("cuda")
    model.to(device)  
else:
    device = torch.device("cpu")
# Move model to the selected device

# Load data from a JSON file
with open(input_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Prepare the list of input texts
input_texts = [item["source"] for item in data]

batch_size = 128  

model.eval()
output_texts = []
for i in tqdm(range(0, len(input_texts), batch_size)):
    batch_input_texts = input_texts[i:i+batch_size]
    input_ids = tokenizer.batch_encode_plus(batch_input_texts, padding=True, truncation=True, return_tensors="pt").input_ids.to(device)
    output_ids = model.generate(input_ids, max_length=512, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50, top_p=0.95, do_sample=True)
    batch_output_texts = tokenizer.batch_decode(output_ids,skip_special_tokens=True)
    output_texts.extend(batch_output_texts)

for item, output_text in zip(data, output_texts):
    item['my_target'] = output_text

# Save the updated data to a new JSON file
with open(output_path, "w", encoding="utf-8") as output_file:
    json.dump(data, output_file, indent=4, ensure_ascii=False)

