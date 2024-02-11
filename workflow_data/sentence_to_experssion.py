import numpy as np
import anndata
import json
from tqdm import tqdm
import scanpy as sc
import sys
import pandas as pd

from src.utils import post_process_generated_cell_sentences, convert_cell_sentence_back_to_expression_vector
def get_vocab(path):
    # Load in gene vocabulary
    global_vocab = set()
    with open(path, "r") as fp:
        for line in fp:
            line = line.rstrip()  # remove end whitespace, e.g. newline
            line_elements = line.split(" ")
            gene_name = line_elements[0]
            global_vocab.add(gene_name)

    global_vocab_list = list(global_vocab)
    global_vocab_list = [gene_name.upper() for gene_name in global_vocab_list]
    return global_vocab_list



def reconstruct(path_input,path_output):

    with open(path_input, "r", encoding="utf-8") as file:
        data = json.load(file)
    

    all_cell_sentences_converted_back_to_expression = []
    global_vocab_list=get_vocab('')
    dataset_df = pd.read_csv("")
    slope = dataset_df.iloc[0, 2].item()
    intercept = dataset_df.iloc[0, 3].item()
    print(f"slope: {slope:.4f}, intercept: {intercept:.4f}")

    for cell_idx in tqdm(data):
        cell_sentence_list = cell_idx["my_target"]
        words = cell_sentence_list.split()    
        cell_sentence_str = " ".join(words)
        post_processed_sentence, num_genes_replaced = post_process_generated_cell_sentences(
            cell_sentence=cell_sentence_str,
            global_dictionary=global_vocab_list,
            replace_nonsense_string="NOT_A_GENE",
        )
        post_processed_sentence=post_processed_sentence[:100]
        reconstructed_expr_vec = convert_cell_sentence_back_to_expression_vector(
            cell_sentence=post_processed_sentence, 
            global_dictionary=global_vocab_list, 
            slope=slope, 
            intercept=intercept
        )
        all_cell_sentences_converted_back_to_expression.append(reconstructed_expr_vec)
    all_cell_sentences_converted_back_to_expression = np.stack(all_cell_sentences_converted_back_to_expression, dtype=np.float32)
    all_cell_sentences_converted_back_to_expression.shape
    reconstructed_adata = sc.AnnData(X=all_cell_sentences_converted_back_to_expression)

    if 'cell_type' not in reconstructed_adata.obs.columns:
        reconstructed_adata.obs['cell_type'] = ''
    reconstructed_adata.var.index = global_vocab_list

    for i, cell_data in enumerate(data):
        reconstructed_adata.obs["cell_type"][i] = cell_data["cell_type"]


    reconstructed_adata.write_h5ad(path_output)

reconstruct('','')

