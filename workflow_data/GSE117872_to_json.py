import pandas as pd
import numpy as np
import json
import random

# Seed for reproducibility
random.seed(42)

# Function to construct a template for drug sensitivity prediction
def construct_template(drug_name, gene_list):
    prompts=[
        "Predict the drug sensitivity of a cancer cell to {} as resistant or sensitive, using its top 100 genes expressed in descending order of expression {}.",
        "Determine whether a cancer cell is likely to be resistant or sensitive to {}, based on its 100 highest expressed genes in descending order {}.",
        "Identify the drug sensitivity classification (resistant/sensitive) for a cancer cell to {}, using its top 100 genes sorted by decreasing expression levels {}.",
        "Assess the likelihood of a cancer cell being resistant or sensitive to {}, considering its 100 genes with the highest expression in descending order {}.",
        "Evaluate a cancer cell's response to {} (resistant or sensitive), based on the cell's 100 most actively expressed genes in descending order {}.",
        "Analyze the drug sensitivity (resistant/sensitive) of a cancer cell to {}, by examining its top 100 genes with the highest expression levels in descending order {}.",
        "Predict the efficacy of {} on a cancer cell, classifying it as resistant or sensitive, based on the cell's 100 most expressed genes in descending order {}.",
        "Distinguish between resistant and sensitive cancer cells in response to {}, using the data from the 100 most expressed genes in descending order {}.",
        "Classify a cancer cell's reaction to {} as resistant or sensitive, analyzing its top 100 genes by highest expression in descending order {}.",
        "Forecast the drug sensitivity outcome (resistant/sensitive) of a cancer cell to {}, guided by its 100 most expressed genes in descending order {}."
    ]
    selected_template = random.choice(prompts)
    return selected_template.format(drug_name, gene_list)

# Read and process gene expression data
expression_data_path = '/newdisk1/lkw/chatcell/data/drug/GSE117872/GSE117872_good_Data_TPM.txt'
# Read drug sensitivity data (adjust the file path and column names as necessary)
cell_info_path = '/newdisk1/lkw/chatcell/data/drug/GSE117872/GSE117872_good_Data_cellinfo.txt'
output_json_path = '/newdisk1/lkw/chatcell_github/GSE117872.json'

expression_data = pd.read_csv(expression_data_path, sep='\t').transpose()

# Extract the top 100 expressed genes for each sample
top100genes = [' '.join(row.sort_values(ascending=False).head(100).index).upper() for _, row in expression_data.iterrows()]

cell_info_data = pd.read_csv(cell_info_path, sep='\t')

# Generate structured JSON data
json_data = []
for i, row in cell_info_data.iterrows():
    drug_name = 'Cisplatin'  # Example; adjust as needed
    gene_list = top100genes[i].upper()
    sensitivity = cell_info_data.iat[i, 5]  # 
    if sensitivity=='Holiday':
        sensitivity='sensitive'
    sensitivity=sensitivity.lower()
    json_data.append({
        "source": construct_template(drug_name, gene_list),
        "target": sensitivity,
    })

# Save JSON data to file
with open(output_json_path, 'w', encoding='utf-8') as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)

print("JSON file has been created.")
