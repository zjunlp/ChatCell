import pandas as pd
import random
import json
import sys
# Set random seed for reproducibility
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

# Define file paths for CSV data and output JSON
expression_data_path = '/newdisk1/lkw/chatcell/data/drug/GSE149383/erl_total_data_2K.csv'
cell_info_path = '/newdisk1/lkw/chatcell/data/drug/GSE149383/erl_total_2K_meta.csv'
output_json_path = '/newdisk1/lkw/chatcell_github/GSE149383.json'

# Load expression data from CSV
expression_data = pd.read_csv(expression_data_path)
print(expression_data.head())

# Transpose data to have genes as columns
expression_data = expression_data.T
rows, columns = expression_data.shape
print(expression_data.head(), f"Rows: {rows}", f"Columns: {columns}", sep='\n')

# Initialize a list to store top 100 gene names for each sample
top100genes = []

# Iterate over rows, skipping the first row with gene names
flag=0
for index, row in expression_data.iterrows():
    if flag==0:# Skip the header row with gene names
        flag=1
        continue
    # Sort and select top 100 genes
    top_100_genes = row.sort_values(ascending=False).head(100).index.tolist()
    top_100_genes = [expression_data.iloc[0, int(gene)] for gene in top_100_genes]
    
    top100genes.append(' '.join(top_100_genes))

print(f"Total samples processed: {len(top100genes)}")


# Load metadata
metadata = pd.read_csv(cell_info_path, header=None)
print(metadata.head(), f"Rows: {metadata.shape[0]}", f"Columns: {metadata.shape[1]}", sep='\n')

# Prepare JSON data
json_data = []
for i in range(len(metadata)):
    drug_name = 'Erlotinib'  # Example drug name
    gene_list = top100genes[i].upper()
    sensitivity_value = metadata.iloc[i, 3]
    entry = {"source": construct_template(drug_name, gene_list), "target": sensitivity_value}
    json_data.append(entry)

# Save JSON data to file
with open(output_json_path, 'w', encoding='utf-8') as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)

print("JSON file has been created.")
