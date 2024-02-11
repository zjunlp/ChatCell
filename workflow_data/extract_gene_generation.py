import numpy as np
import anndata
import json
from tqdm import tqdm
import scanpy as sc
from src.utils import post_process_generated_cell_sentences, convert_cell_sentence_back_to_expression_vector

cell500=['Dermal Fibroblast', 'TAC-1', 'IRS', 'Basal', 'Medulla', 'alowCD34+ bulge', 'Mix', 'ORS', 'Infundibulum', 'Spinous', 'ahighCD34+ bulge', 'TAC-2', 'Hair Shaft-cuticle.cortex']
cell500.append('Endothelial')
cell500.append('Isthmus')
cell500.append('Dermal Papilla')
print(len(cell500))
for i in range(len(cell500)):
    cell500[i] = ' ' + cell500[i] 

initial_prompt_templates = [
        "Identify the cell type most likely associated with these 100 highly expressed genes listed in descending order.",
        "Determine the probable cell type for the following 100 genes with the highest expression levels.",
        "Indicate the cell type typically linked to these 100 top-expressed genes.",
        "Specify the most likely cell type based on these 100 genes sorted by decreasing expression.",
        "Find the cell type that corresponds to these top 100 highly expressed genes.",
        "Point out the cell type these 100 genes with peak expression levels most commonly represent.",
        "Deduce the cell type likely to have these 100 highly expressed genes.",
        "Pinpoint the cell type that these 100 genes with the highest expression levels are most likely associated with.",
        "Ascertain the cell type from which these 100 highly expressed genes likely originate.",
        "Reveal the likely cell type linked to these 100 genes, listed by decreasing expression levels.",
        "Uncover the most probable cell type related to these 100 highly expressed genes.",
        "Indicate the cell type that would logically have these 100 top-expressed genes.",
        "Provide the likely cell type based on these 100 genes with high expression levels.",
        "Isolate the cell type commonly associated with these 100 top genes.",
        "Establish the cell type that these 100 genes with the highest expression levels are most likely from.",
        "Discern the likely cell type for these 100 genes sorted by expression level.",
        "Note the cell type typically associated with these 100 most expressed genes.",
        "Report the cell type most probably linked to these 100 genes with peak expression.",
        "Conclude the most likely cell type these 100 genes are associated with.",
        "State the probable cell type connected to these 100 top-expressed genes.",
        "What cell type is most likely represented by these top 100 highly expressed genes?",
        "Identify the probable cell type for these 100 genes with the highest expression levels.",
        "Which cell type is typically associated with these 100 most expressed genes?",
        "Can you deduce the cell type based on this list of 100 highly expressed genes?",
        "Given these 100 genes sorted by decreasing expression, what is the likely cell type?",
        "Based on these top 100 genes, which cell type are they most commonly found in?",
        "What type of cell is most likely to express these 100 genes in decreasing order of expression?",
        "What is the probable cell type these 100 highly expressed genes are associated with?",
        "From which cell type do these 100 most expressed genes likely originate?",
        "Determine the cell type likely associated with these 100 genes listed by decreasing expression.",
        "Given these 100 highly expressed genes, can you identify the likely cell type?",
        "Infer the cell type based on these 100 genes with the highest expression levels.",
        "Which cell type is likely to have these 100 genes with the highest expression?",
        "Could you specify the cell type most likely associated with these top 100 genes?",
        "What cell type would you associate with these 100 highly expressed genes?",
        "Can you tell the likely cell type for these 100 genes, sorted by decreasing expression?",
        "What is the likely cell type based on these 100 top expressed genes?",
        "Identify the cell type most commonly associated with these 100 genes.",
        "Based on these genes listed by decreasing expression, what cell type are they likely from?",
        "Given these 100 genes with high expression levels, what is the probable cell type?",
        "Which cell type is expected to have these 100 genes with the highest levels of expression?",
        "What is the most probable cell type based on these 100 genes with peak expression levels?",
        "What cell type would most likely have these 100 top expressed genes?",
        "Which cell type most probably corresponds to these 100 highly expressed genes?",
        "Could you determine the likely cell type based on these 100 most expressed genes?",
        "What type of cell would most likely contain these 100 genes with highest expression?",
        "Based on the list of 100 genes, what is the most likely corresponding cell type?",
        "Please identify the cell type that these 100 highly expressed genes are most likely linked to.",
        "Given these 100 genes ranked by expression, what would be the associated cell type?",
        "What would be the probable cell type for these 100 genes, listed by decreasing expression?",
        "Can you deduce the most likely cell type for these top 100 highly expressed genes?",
        "Identify the likely cell type these 100 genes with top expression could represent.",
        "Based on the following 100 genes, can you determine the cell type they are commonly found in?",
        "What is the likely originating cell type of these 100 top expressed genes?",
        "Specify the cell type most commonly linked with these 100 highly expressed genes.",
        "Which cell type would you expect to find these 100 genes with high expression levels?",
        "Indicate the probable cell type these 100 genes are commonly associated with.",
        "According to these 100 genes with highest expression, what cell type are they most likely from?",
        "Which cell type is these 100 genes with the highest expression levels most commonly found in?",
        "Could you point out the likely cell type linked with these 100 genes sorted by decreasing expression?",
]

print(len(cell500))
def get_sentence(path_input,path_output):
    with open(path_input, "r", encoding="utf-8") as file:
        data = json.load(file)
    filtered_data = []
    for item in tqdm(data, desc="Processing", unit="data"):
        flag=0
        for prompt in initial_prompt_templates:
            if(item['source'].startswith(prompt)):
                flag=1
        if flag==0:

            for cell_type in cell500:
                if cell_type in item['source']:
                    item['cell_type']=cell_type.strip()
                    item['gene']=item['my_target']
                    filtered_data.append(item)
                    break
    print(len(filtered_data))
    with open(path_output, "w", encoding="utf-8") as output_file:
        json.dump(filtered_data, output_file, indent=4, ensure_ascii=False)


get_sentence('','')
