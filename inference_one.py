from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    HfArgumentParser,
    Trainer,
    TrainingArguments,
    AutoModelForSeq2SeqLM,
)
import torch

# Set the path to the  model and specify the input text
model_folder = "zjunlp/chatcell-small"
input_text="Detail the 100 starting genes for a Mix, ranked by expression level: "
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


model.eval()
# Encode the input text and generate a response with specified generation parameters
input_ids = tokenizer(input_text,return_tensors="pt").input_ids.to(device)
output_ids = model.generate(input_ids, max_length=512, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50, top_p=0.95, do_sample=True)
# Decode and print the generated output text
output_text = tokenizer.decode(output_ids[0],skip_special_tokens=True)

print(output_text)
