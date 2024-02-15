import json
from collections import Counter
from tqdm import tqdm

# Function to get the gene vocabulary
def get_gene_vocab(path):
    # Load gene vocabulary from a file
    gene_vocab = set()
    with open(path, "r") as file:
        for line in file:
            gene_name = line.strip().split()[0].upper()
            gene_vocab.add(gene_name)
    return list(gene_vocab)

# Function to calculate statistics from the input JSON data
def calculate_statistics(json_path, global_path):
    # Load data from JSON file
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    num_cases = len(data)  # Total number of cases
    invalid_gene_count = 0  # Count of invalid gene names
    total_gene_count = 0  # Total count of gene names
    unique_gene_count = 0  # Total count of unique gene names
    global_vocab_list = get_gene_vocab(global_path)

    # Iterate over each cell in the data
    for cell_idx in tqdm(data):
        cell_sentence_list = cell_idx["my_target"]
        words = cell_sentence_list.split()
        cell_sentence_str = " ".join(words)
        generated_gene_names = cell_sentence_str.split(" ")
        generated_gene_names = [gene.upper() for gene in generated_gene_names]
        gene_name_to_occurrences = Counter(generated_gene_names)

        # Check for invalid gene names
        for gene_name in generated_gene_names:
            if gene_name not in global_vocab_list:
                invalid_gene_count += 1

        unique_gene_count += len(gene_name_to_occurrences)
        total_gene_count += len(words)

    print("Total number of cases:", num_cases)
    print("Total gene count:", total_gene_count, round(total_gene_count / num_cases, 2))
    print("Valid gene count:", total_gene_count - invalid_gene_count, round(100 * (total_gene_count - invalid_gene_count) / total_gene_count, 2))
    print("Unique gene count:", unique_gene_count, round(100 * unique_gene_count / total_gene_count, 2))

# Paths to input files
json_path = 'path_to_your_data.json'
global_path = 'vocab_human.txt' 

# Call the function to calculate statistics
calculate_statistics(json_path, global_path)
