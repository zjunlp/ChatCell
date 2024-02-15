import os
import json
from tqdm import tqdm
from datasets import load_from_disk, concatenate_datasets
from transformers import AutoTokenizer

# Paths for tokenizers and data files
tokenizer_last = 'google-t5/t5-base'
tokenizer_now ='your_new_tokenizer_path' 
GSE117872_json_file_path = 'GSE117872.json'
GSE149383_json_file_path = 'GSE149383.json'
cell_sentences_hf_path = 'cell_sentences_hf_path'

# List of essential cell biology terms
cell_vocab=['Dermal Fibroblast', 'Dermal Papilla', 'TAC-1', 'IRS', 'Basal', 'K6+ Bulge Companion Layer', 'Medulla', 'alowCD34+ bulge', 'Mix', 'Isthmus', 'ORS', 'Infundibulum', 'Spinous', 'ahighCD34+ bulge', 'TAC-2', 'Macrophage DC', 'Endothelial', 'Dermal Sheath', 'Sebaceous Gland', 'Granular', 'Hair Shaft-cuticle.cortex', 'Schwann Cell', 'Melanocyte']
cell_vocab.extend(['PBMC','Erlotinib','Cisplatin'])

# Load mouse datasets
train_ds = load_from_disk(os.path.join(cell_sentences_hf_path, 'train'))
val_ds = load_from_disk(os.path.join(cell_sentences_hf_path, 'valid'))
test_ds = load_from_disk(os.path.join(cell_sentences_hf_path, 'test'))
# Concatenate datasets and preprocess
total_ds = concatenate_datasets([train_ds, val_ds, test_ds])
total_ds = total_ds.map(lambda example: {"first_100_gene_words": example["input_ids"].split(" ")[:100]})
for cell_idx in tqdm(range(len(total_ds))):
    cell_sentence_list = total_ds[cell_idx]["first_100_gene_words"]
    cell_vocab.extend(cell_sentence_list)

# Load GSE datasets
with open(GSE117872_json_file_path, 'r') as f1, open(GSE149383_json_file_path, 'r') as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)
GSE_data=data1+data2
for x in GSE_data:
    gene=x['source']
    gene=gene.split()[-100:]
    gene[-1]=gene[-1][:-1]
    cell_vocab.extend(gene)

# Load the tokenizer and update its vocabulary
tokenizer = AutoTokenizer.from_pretrained(tokenizer_last,from_slow=True)
dif=list(set(cell_vocab) - set(tokenizer.vocab.keys()))
dif.sort()
tokenizer.add_tokens(dif)
# Save the updated tokenizer
tokenizer.save_pretrained(tokenizer_now)


