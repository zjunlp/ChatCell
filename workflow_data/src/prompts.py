"""
This file was initially developed by the project at https://github.com/vandijklab/cell2sentence-ft. 
Many thanks for their contributions to this field. It adheres to the Attribution-NonCommercial-ShareAlike 
4.0 International License. 

If you use this file, please cite the papers "Levine et al., Cell2Sentence: Teaching Large Language 
Models the Language of Biology. 2023 (https://www.biorxiv.org/content/10.1101/2023.09.11.557287v3)" and 
"Rahul M Dhodapkar. Representing cells as sentences enables natural-language processing for single-cell 
transcriptomics. 2022 (https://www.biorxiv.org/content/10.1101/2022.09.18.508438)."
"""
import random


def construct_cell_type_template(cell_type):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    if cell_type[0] in vowels:
        cell_type = f"n {cell_type}"
    else:
        cell_type = f" {cell_type}"

    cell_type_templates = [
        "List the initial 100 genes associated with a{}: ",
        "Provide the top 100 genes for a{}: ",
        "Identify 100 genes corresponding to a{}: ",
        "Catalog the 100 primary genes for a{}: ",
        "Name the first set of 100 genes in a{}: ",
        "Outline 100 genes initially associated with a{}: ",
        "Specify the first 100 genes linked to a{}: ",
        "Show the leading 100 genes of a{}: ",
        "Enumerate the 100 starting genes for a{}: ",
        "List the 100 most highly expressed genes in a{}, ordered from highest to lowest expression: ",
        "Provide a ranking of the top 100 expressed genes in a{} by decreasing levels: ",
        "Detail the 100 genes with the greatest expression levels in a{}: ",
        "Identify the 100 genes in a{} with the highest expression, sorted in descending order: ",
        "Catalog the 100 most active genes in a{} cell, ordered by decreasing expression: ",
        "Name the 100 genes with peak expression levels in a{}, from highest to lowest: ",
        "Describe the 100 most abundantly expressed genes in a{}, in descending order: ",
        "Which 100 genes have the highest expression in a{}? List them in descending order: ",
        "Show the 100 most significantly expressed genes in a{}, organized by decreasing levels: ",
        "Enumerate the 100 genes with the strongest expression in a{}, ranked from highest to lowest: ",
        "List the top 100 genes by decreasing expression specifically for a{}: ",
        "Provide the first 100 highly expressed genes in a{}, sorted by expression level: ",
        "Identify the initial 100 genes with peak expression levels in a{}: ",
        "Catalog the top 100 expressed genes corresponding to a{}, from highest to lowest: ",
        "What are the first 100 genes with the greatest expression in a{}? ",
        "Name the top 100 genes sorted by decreasing expression for a{}: ",
        "Show the leading 100 genes by expression level associated with a{}: ",
        "Enumerate the first 100 genes by highest expression levels in a{}: ",
        "Specify the 100 primary genes in a{} ordered by decreasing expression: ",
        "Outline the initial set of 100 genes with high expression in a{}: ",
        "Detail the 100 starting genes for a{}, ranked by expression level: ",
        "Rank the first 100 genes by expression level found in a{}: ",
        "Describe the 100 most active genes initially associated with a{}: ",
        "Which are the first 100 genes in a{} sorted by decreasing expression? ",
        "Provide a ranking of the initial 100 genes by decreasing expression levels in a{}: ",
        "List 100 primary genes from highest to lowest expression in a{}: ",
        "Catalog the 100 initial genes for a{}, ordered by expression level from highest to lowest: ",
        "Identify the 100 leading genes in a{} based on expression levels: ",
        "Show the 100 primary genes for a{}, sorted by decreasing expression: ",
        "Enumerate the 100 most abundantly expressed starting genes in a{}: ",
        ## add
        "Reveal the first 100 genes with the highest expression in a{}, sorted in order of decreasing levels: ",
        "Compile a list of the top 100 genes by expression in a{}, descending from highest to lowest: ",
        "Pinpoint the 100 leading genes based on expression levels in a{}: ",
        "Disclose the initial 100 genes showing the highest expression in a{}, in a descending sequence: ",
        "Present the foremost 100 genes by expression in a{}, ranked from the highest to the lowest: ",
        "Highlight the 100 genes with the utmost expression in a{}, arranged by diminishing levels: ",
        "Unveil the top 100 genes characterized by their expression in a{}, in descending order: ",
        "Report on the first 100 genes with maximum expression in a{}, listed from highest to lowest: ",
        "Profile the 100 genes leading in expression in a{}, ordered by decreasing levels: ",
        "Summarize the primary 100 genes by expression level in a{}, from the highest to the lowest: ",
        "Expose the 100 genes at the pinnacle of expression in a{}, sequenced by decreasing order: ",
        "Discern the top 100 genes for expression in a{}, aligned from highest to lowest: ",
        "Uncover the first 100 genes exhibiting the highest levels of expression in a{}, organized by descending order: ",
        "Depict the leading 100 genes in terms of expression in a{}, ranked by decreasing levels: ",
        "Characterize the 100 most prominently expressed genes in a{}, in a downward sequence: ",
        "Account for the 100 genes with superior expression in a{}, sorted from highest to lowest: ",
        "Render the 100 most expressed genes in a{}, categorized by descending expression levels: ",
        "Illustrate the 100 top-expressed genes in a{}, ordered by decreasing levels of expression: ",
        "Convey the initial 100 genes with the highest level of expression in a{}, from highest to lowest: ",
        "Sketch the primary 100 genes based on their expression in a{}, descending from highest expression: ",
        "Clarify the 100 genes leading in expression within a{}, sorted in decreasing order of expression: ",
        "Communicate the first 100 genes ranked by expression in a{}, from the highest to the lowest levels: ",
        "Indicate the 100 most prominently featured genes in a{} based on expression, in reverse order: ",
        "Relate the top 100 genes according to expression in a{}, descending by level: ",
        "Itemize the 100 genes with the leading expression figures in a{}, ordered from the highest downward: ".
    ]

    selected_template = random.choice(cell_type_templates)

    formatted_template = selected_template.format(cell_type)

    return formatted_template


def construct_prediction_template(genes):
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
        ## add
        "Ascertain which cell type is most closely associated with these 100 genes exhibiting the highest levels of expression.",
        "Elucidate the cell type that these 100 genes, ranked by their expression, most closely correlate with.",
        "Predict the cell type associated with the highest expression of these 100 genes.",
        "Identify the cell lineage that these 100 genes, ordered by expression magnitude, suggest.",
        "Decipher the cell type connected to the top 100 genes by expression level.",
        "Clarify the cell type that most likely expresses these 100 genes at high levels.",
        "Characterize the cell type associated with the highest expression among these 100 genes.",
        "Trace the likely cell type for these 100 genes, characterized by their elevated expression levels.",
        "Profile the cell type most aligned with the expression patterns of these 100 genes.",
        "Outline the cell type that is most probably expressed by these top 100 genes.",
        "Summarize the cell type indicative of these 100 genes with the highest expression rankings.",
        "Highlight the cell type that these 100 genes, when highly expressed, most likely indicate.",
        "Interpret the cell type likely reflected by the top 100 genes according to their expression levels.",
        "Sketch the probable cell type that these 100 genes with elevated expression levels delineate.",
        "Extrapolate the cell type likely exemplified by these top 100 expressed genes.",
        "Map out the cell type that is suggested by the high expression of these 100 genes.",
        "Predict the cell type signified by the highest expression levels in these 100 genes.",
        "Synthesize the probable cell type from the expression data of these 100 top genes.",
        "Derive the cell type most indicative of these 100 genes with the highest expression signatures.",
        "Elaborate on the cell type that these 100 genes with top expression levels are suggesting.",
        "Formulate the cell type hypothesis based on the expression profile of these 100 genes.",
        "Project the cell type that would typically express these 100 genes at high levels.",
        "Render the likely cell type associated with the expression pattern of these 100 genes.",
        "Dissect the probable cell type based on the high expression of these 100 genes.",
        "Propose the cell type that is inferred by the expression data of these 100 top genes.",
        "Assess the cell type that these 100 highly expressed genes most plausibly suggest.",
        "Conceptualize the cell type that would manifest these 100 genes with their peak expression levels.",
        "Analyze the cell type that is most resonant with these 100 genes’ expression profiles.",
        "Frame the cell type likely to be identified by the expression patterns of these 100 genes.",
        "Articulate the cell type that these 100 genes with the highest expression might typify."

    ]

    prediction_templates = [
        "This is the cell type corresponding to these genes: ",
        "These genes are most likely associated with the following cell type: ",
        "This is the probable cell type for these genes: ",
        "Based on these genes, the corresponding cell type is: ",
        "These genes suggest the cell type is most likely: ",
        "These genes are indicative of the cell type: ",
        "The associated cell type for these genes appears to be: ",
        "These genes typically correspond to: ",
        "The expected cell type based on these genes is: ",
        "These genes are commonly found in: ",
        "The cell type that these genes are most commonly linked with is: ",
        "Based on the expression levels, the cell type would likely be: ",
        "The genes provided are most commonly expressed in: ",
        "Given these genes, the likely corresponding cell type is: ",
        "The cell type these genes most likely originate from is: ",
        "These genes are most frequently associated with the cell type: ",
        "From these genes, it can be inferred that the cell type is: ",
        "The cell type best represented by these genes is: ",
        ## add
        "The cell type that typically exhibits these genes is: ",
        "The genes in question are characteristic of the following cell type: ",
        "Considering the genetic markers, the cell type is likely: ",
        "These genetic sequences suggest a strong association with the cell type: ",
        "The cellular identity associated with these genes is most likely: ",
        "Analysis of these genes points to the cell type being: ",
        "The genetic profile suggests the cell type as: ",
        "Identifying the cell type, these genes are predominantly linked to: ",
        "The predominant cell type for these gene expressions is: ",
        "Correlating these genes, we deduce the cell type to be: ",
        "Given the genetic evidence, the corresponding cell type is inferred as: ",
        "The genetic markers indicate the cell type is: ",
        "From the genetic signatures, the associated cell type is: ",
        "Linking these genes to a cell type leads us to conclude: ",
        "The cell type, as suggested by these genes, is likely: ",
        "Drawing from these genes, the cell type is identified as: ",
        "The gene analysis suggests a cell type affiliation with: ",
        "These genes delineate the cell type as: "
    ]

    # build prompt

    selected_initial_template = random.choice(initial_prompt_templates)
    selected_prediction_template = random.choice(prediction_templates)

    formatted_template = (
        selected_initial_template + " " + genes + " " + selected_prediction_template
    )

    return formatted_template
