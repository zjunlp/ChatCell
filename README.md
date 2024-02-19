

<div align="center">

[![Paper page](https://huggingface.co/datasets/huggingface/badges/resolve/main/paper-page-sm-dark.svg)](https://huggingface.co/papers/2402.08303)
[![Code License](https://img.shields.io/badge/Code%20License-MIT-green.svg)](https://github.com/zjunlp/ChatCell/blob/main/LICENSE)
[![Data License](https://img.shields.io/badge/Data%20License-CC%20BY%204.0-red.svg)](https://github.com/zjunlp/ChatCell/blob/main/DATA_LICENSE)


<h2 align="center">  <img src="figure/logo.png" width="8%" height="18%"> ChatCell: Facilitating Single-Cell Analysis with Natural Language </h2>

<p align="center">
  <a href="https://www.zjukg.org/project/ChatCell">💻 Homepage</a> •
  <a href="https://huggingface.co/datasets/zjunlp/ChatCell-Instructions">🤗 Dataset</a> •
  <a href="https://huggingface.co/spaces/zjunlp/Chatcell">🍎 Demo</a> •
  <a href="https://arxiv.org/abs/2402.08303">📑 Paper</a> •
  <a href="#1">🏖️ Overview</a> •
  <a href="#2">🧬 Single-cell Analysis Tasks</a> •
  <a href="#3">⌚️ QuickStart</a> •
  <a href="#4">🛠️ Usage</a> •
  <a href="#5">🚀 Evaluation</a> •
  <a href="#6">📝 Cite</a>
</p>



<div align=center><img src="figure/intro.gif" width="60%" height="100%" /></div>
<b>ChatCell</b> allows researchers to input instructions in either natural or single-cell language, thereby facilitating the execution of necessary tasks in single-cell analysis. Black and red texts denote human and single-cell language, respectively.

</div>

## ✨ Acknowledgements 

Special thanks to the authors of [Cell2Sentence: Teaching Large Language Models the Language of Biology](https://github.com/vandijklab/cell2sentence-ft) and [Representing cells as sentences enables natural-language processing for single-cell transcriptomics
](https://github.com/rahuldhodapkar/cell2sentence) for their inspiring work. 

The [`src`](./workflow_data/src) folder and [`transform.py`](./workflow_data/transform.py) in this project are grounded in their research. Grateful for their valuable contributions to the field. 


## 🆕 News

- **\[Feb 2024\]** Our [ChatCell app](https://chat.openai.com/g/g-vUwj222gQ-chatcell) is now live on GPTStore, give it a try📱!
- **\[Feb 2024\]** We released the model weights based on T5 in [small](https://huggingface.co/zjunlp/chatcell-small), [base](https://huggingface.co/zjunlp/chatcell-base), and [large](https://huggingface.co/zjunlp/chatcell-large) configurations on Huggingface 🤗.
- **\[Feb 2024\]** We released the [instructions of ChatCell](https://huggingface.co/datasets/zjunlp/ChatCell-Instructions) on Huggingface 🤗.
- **\[Feb 2024\]** We released the [paper](https://arxiv.org/abs/2402.08303).


## 📌 Table of Contents

- [🏖️ Overview](#1)
- [🧬 Single-cell Analysis Tasks](#2)
- [⌚️ QuickStart](#3)
- [🛠️ Usage](#4)
- [🚀 Evaluation](#5)
- [📝 Cite](#6)

---

<h2 id="1">🏖️ Overview</h2>

**Background**
- Single-cell biology examines the intricate functions of the cells, ranging from energy production to genetic information transfer, playing a critical role in unraveling the fundamental principles of life and mechanisms influencing health and disease. 
- The field has witnessed a surge in single-cell RNA sequencing (scRNA-seq) data, driven by advancements in high-throughput sequencing and reduced costs.
- Traditional single-cell foundation models leverage extensive scRNA-seq datasets, applying NLP techniques to analyze gene expression matrices—structured formats that simplify scRNA-seq data into computationally tractable representations—during pre-training. They are subsequently fine-tuned for distinct single-cell analysis tasks, as shown in Figure (a).

<p align="center">
<img src="figure/overview.jpg"  width="100%" height="60%">
</p>
<div align="center">
Figure 1:  (a) Comparison of traditional single-cell engineering and <b>ChatCell</b>. (b) Overview of <b>ChatCell</b>.
</div>
<br>
We present <b>ChatCell</b>, a new approach that leverages natural language to make single-cell analysis more accessible and intuitive.

- Initially, we convert scRNA-seq data into a single-cell language that LLMs can readily interpret.
- Subsequently, we employ templates to integrate this single-cell language with task descriptions and target outcomes, creating comprehensive single-cell instructions.
- To improve the LLM's expertise in the single-cell domain,  we initialize with T5 and conduct vocabulary adaptation, enriching the model with a specialized single-cell lexicon.
- Following this, we utilize unified sequence generation to empower the model to adeptly execute a range of single-cell tasks.


<h2 id="2">🧬 Single-cell Analysis Tasks</h2>

We concentrate on the following single-cell tasks:

- <b>Random Cell Sentence Generation.</b>
Random cell sentence generation challenges the model to create cell sentences devoid of predefined biological conditions or constraints. This task aims to evaluate the model's ability to generate valid and contextually appropriate cell sentences, potentially simulating natural variations in cellular behavior. 

<p align="center">
<img src="figure/example1.jpg"  width="80%" height="60%">
</p>


- <b>Pseudo-cell Generation.</b>
Pseudo-cell generation focuses on generating gene sequences tailored to specific cell type labels. This task is vital for unraveling gene expression and regulation across different cell types, offering insights for medical research and disease studies, particularly in the context of diseased cell types.


<p align="center">
<img src="figure/example2.jpg"  width="80%" height="60%">
</p>

- <b>Cell Type Annotation.</b>
For cell type annotation, the model is tasked with precisely classifying cells into their respective types based on gene expression patterns encapsulated in cell sentences. This task is fundamental for understanding cellular functions and interactions within tissues and organs, playing a crucial role in developmental biology and regenerative medicine.

<p align="center">
<img src="figure/example3.jpg"  width="80%" height="60%">
</p>

- <b>Drug Sensitivity Prediction.</b>
The drug sensitivity prediction task aims to predict the response of different cells to various drugs. It is pivotal in designing effective, personalized treatment plans and contributes significantly to drug development, especially in optimizing drug efficacy and safety.


<p align="center">
<img src="figure/example4.jpg"  width="80%" height="60%">
</p>

<h2 id="3">⌚️ QuickStart</h2>

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("zjunlp/chatcell-small")
model = AutoModelForSeq2SeqLM.from_pretrained("zjunlp/chatcell-small")
input_text="Detail the 100 starting genes for a Mix, ranked by expression level: "

# Encode the input text and generate a response with specified generation parameters
input_ids = tokenizer(input_text,return_tensors="pt").input_ids
output_ids = model.generate(input_ids, max_length=512, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50, top_p=0.95, do_sample=True)

# Decode and print the generated output text
output_text = tokenizer.decode(output_ids[0],skip_special_tokens=True)
print(output_text)
```



<h2 id="4">🛠️ Usage</h2>

<h3 id="1">📚 Step1: Prepare the data</h3>

❗️Note: You can download the original data from the `raw_data` directory. Alternatively, you can directly download the [pre-processed data we provide on huggingface](https://huggingface.co/datasets/zjunlp/ChatCell-Instructions) to **skip Step 1 of the process**.

Change to the evaluation directory with the command: `cd workflow_data`.

**1. For tasks such as random cell sentence generation, pseudo-cell generation, and cell type annotation, we utilize cells from the SHARE-seq mouse skin dataset.**

- Follow these steps to use the  `transform.py` script (This file was initially developed by the [Cell2Sentence](https://github.com/vandijklab/cell2sentence-ft) team, thanks for their great work!🤗) to **translate scENA-seq data into cell sentence**:

  - Define `data_filepath` to specify the path to your downloaded SHARE-seq mouse skin dataset `.h5ad` file.
  - Define `output_dir` to specify the directory where the generated cell sentences will be saved.
  - Define `eval_output_dir` to specify where figures and evaluation metrics will be stored.
  - Run the transformation process by executing the following command in your terminal: `python transform.py`.

- Then **covert cell sentences to instructions** with `mouse_to_json.py`:

  - Set `input_path` to the `output_dir` specified in  `transform.py`.
  - Define `train_json_file_path`, `val_json_file_path`, and `test_json_file_path` to specify the paths where you want to save your train, validation, and test datasets in JSON format, respectively.
  - Run the following command in your terminal to start the conversion process: `python mouse_to_json.py`.


**2. For the drug sensitivity prediction task, we select GSE149383 and GSE117872 datasets.**

- For GSE149383: Open `GSE149383_to_json.py`, define `expression_data_path` and `cell_info_path` to the location of your downloaded `erl_total_data_2K.csv` and `erl_total_2K_meta.csv` file.
- For GSE117872: Open `GSE117872_to_json.py`, define `expression_data_path` and `cell_info_path` to the location of your downloaded `GSE117872_good_Data_TPM.txt` and `GSE117872_good_Data_cellinfo.txt` file.
- Update `output_json_path` with the desired location for the JSON output files.
- Execute the conversion script:
  - Run `python GSE149383_to_json.py` for the GSE149383 dataset.
  - Run `python GSE117872_to_json.py` for the GSE117872 dataset.
- Open `split.py`, define `input_path` to the same locations as `output_json_path` used above. Specify the locations for `train_json_file_path`, `val_json_file_path`, and `test_json_file_path` where you want the split datasets to be saved.
- Run the script with `python split.py` to split the dataset into training, validation, and test sets.

**3. After preparing instructions for each specific task, follow the steps below to merge the datasets using the `merge.py` script.**

- Ensure that the paths for `train_json_file_path`, `val_json_file_path`, and `test_json_file_path` are correctly set to point to the JSON files you previously generated for each dataset, such as `GSE117872`, `GSE149383`, and `mouse`.
- Run `python merge.py` to start the merging process. This will combine the specified training, validation, and testing datasets into a unified format, ready for further analysis or model training.


<h3 id="7"> 📜 Step2 : Vocabulary Adaptation</h3>

To adapt the tokenizer vocabulary with new terms from cell biology, follow these steps using the `vocabulary_adaptation.py` script.

- Ensure you have the following parameters configured in the script before running it:

  - `tokenizer_last`: The path to the directory containing the pre-existing tokenizer.

  - `tokenizer_now`: The destination path where the updated tokenizer will be saved.

  - `GSE117872_json_file_path`: This should be set to the `output_json_path` variable from the `GSE117872_to_json.py` script

  - `GSE149383_json_file_path`: Similarly, this should match the `output_json_path` variable in the `GSE149383_to_json.py` script.

  - `cell_sentences_hf_path`: This path should correspond to the `cell_sentences_hf` directory, which is specified as the `output_dir` variable within the `transform.py` script

- Once all parameters are configured, execute the script to update the tokenizer's vocabulary with new cell biology terms. Run the following command in your terminal: `python vocabulary_adaptation.py`.

<h3 id="2">🛠️ Step3: Train and generate</h3>

**1. Training**

- Open the `finetune.py` script. Update the script with the paths for your training and validation JSON files (`train_json_path` and `valid_json_path`), the tokenizer location (`tokenizer_path`), the base model directory (`model_path`), and the directory where you want to save the fine-tuned model (`output_dir`).
- Execute the fine-tuning process by running the following command in your terminal: `python finetune.py`

**2. Generation**

- Single-Instance Inference:
  - To run inference on a single instance, set the necessary parameters in `inference_one.py`.
  - Execute the script with: `python inference_one.py`.
- Web Interface Inference:  
  - For interactive web interface inference using Gradio, configure `inference_web.py` with the required parameters.
  - Launch the web demo by running: `python inference_web.py`.
- Batch Inference:  
  - For inference on a batch of instances, adjust the parameters in `inference_batch.py` as needed.
  - Start the batch inference process with: `python inference_batch.py`.


<h3 id="3">⌨️ Step4: Translating sentences into gene expressions</h3>

**For the pseudo-cell generation task, we also translate sentences into gene expressions, including data extraction and transformation stages.**

- Data Extraction:
  - Open `extract_gene_generation.py`. Set up the necessary parameters for generating cells based on cell type. This step is intended for training datasets larger than 500 samples, covering 16 cell types.
  - Run the following command in your terminal to start the data extraction process: `python extract_gene_generation.py`.

- Transformation Process:
  - After generating the necessary files, proceed by configuring `sentence_to_expression.py` with the appropriate parameters for the translation process.
  - Execute the transformation script with the command: `python sentence_to_expression.py`.
 

<h2 id="5">🚀 Evaluation</h2>

To evaluate the performance of various tasks, follow these steps:

- Change to the evaluation directory with the command: `cd evaluation`.

- Random Cell Generation Task:
  - Open `Performance_of_random_cell_generation.py`.
  - Specify the `json_path` to the JSON file with the generated data.
  - Specify the `global_path` to the global gene vocabulary file, usually located in the `cell_sentences` subdirectory within `output_dir` specified by the `transform.py` script, and is named `vocab_human.txt`.
  - Run the command: `python Performance_of_random_cell_generation.py`. 

- Pseudo-cell Generation Task:
  - Depending on the format of your data, open `python Performance_of_pseudo-cell_generation_lev.py`, or `python Performance_of_pseudo-cell_generation_expr.py`.
  - Specify the `my_data_path` to the file with the generated pseudo-cell data.
  - Specify the `ground_truth_data_path` to the file with the ground truth data.
  - Specify the `k` to the K-value for KNN analysis.
  - Depending on the format of your data, run: `python Performance_of_pseudo-cell_generation_lev.py`, or `python Performance_of_pseudo-cell_generation_expr.py`.

- Cell Type Annotation and Drug Sensitivity Prediction Tasks:
  - Open `python performance_of_classification.py`.
  - Specify the `my_data_path` to the JSON file containing the generated data for the task.
  - Run the command: `python performance_of_classification.py`.

 
  
<h2 id="6">📝 Cite</h2>
```
@article{fang2024chatcell,
  title={ChatCell: Facilitating Single-Cell Analysis with Natural Language},
  author={Fang, Yin and Liu, Kangwei and Zhang, Ningyu and Deng, Xinle and Yang, Penghui and Chen, Zhuo and Tang, Xiangru and Gerstein, Mark and Fan, Xiaohui and Chen, Huajun},
  year={2024},
}
```

### Other Related Projects

- [Cell2Sentence](https://github.com/rahuldhodapkar/cell2sentence)
- [CellPLM](https://github.com/OmicsML/CellPLM)
- [ScGPT](https://github.com/bowang-lab/scGPT)
- [ScBERT](https://github.com/TencentAILabHealthcare/scBERT)
- [GenePT](https://github.com/yiqunchen/GenePT)
- [ScMulan](https://github.com/SuperBianC/scMulan)
- [bulk2space](https://github.com/ZJUFanLab/bulk2space)
