

<div align="center">

[![Code License](https://img.shields.io/badge/Code%20License-MIT-green.svg)](https://github.com/zjunlp/ChatCell/blob/main/LICENSE)
[![Data License](https://img.shields.io/badge/Data%20License-CC%20BY%204.0-red.svg)](https://github.com/zjunlp/ChatCell/blob/main/DATA_LICENSE)


<h2 align="center">  <img src="figure/logo.png" width="8%" height="18%"> ChatCell: Facilitating Single-Cell Analysis with Natural Language </h2>

<p align="center">
  <a href="https://www.zjukg.org/project/ChatCell">💻 Project Page</a> •
  <a href="https://huggingface.co/datasets/zjunlp/ChatCell-Instructions">🤗 Dataset</a> •
  <a href="https://huggingface.co/spaces/zjunlp/Chatcell">🍎 Demo</a> •
  <a href="#1">🏖️ Overview</a> •
  <a href="#2">🧬 Single-cell Analysis Tasks</a> •
  <a href="#3">🛠️ Quickstart</a> •
  <a href="#4">📝 Cite</a>
</p>



<div align=center><img src="figure/intro.gif" width="60%" height="100%" /></div>
<b>ChatCell</b> allows researchers to input instructions in either natural or single-cell language, thereby facilitating the execution of necessary tasks in single-cell analysis. Black and red texts denote human and single-cell language, respectively.

</div>

## 🆕 News

- **\[Feb 2024\]** We released the model weights and datasets.


## 📌 Table of Contents

- [🏖️ Overview](#1)
- [🧬 Single-cell Analysis Tasks](#2)
- [🛠️ Quickstart](#3)
- [📝 Cite](#4)


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
We present <b>ChatCell</b>, a new paradigm that leverages natural language to make single-cell analysis more accessible and intuitive.

- Initially, we convert scRNA-seq data into a single-cell language that LLMs can readily interpret.
- Subsequently, we employ templates to integrate this single-cell language with task descriptions and target outcomes, creating comprehensive single-cell instructions.
- To improve the LLM's expertise in the single-cell domain,  we conduct vocabulary adaptation, enriching the model with a specialized single-cell lexicon.
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

<h2 id="3">🛠️ Quickstart</h2>

- **📚 Prepare the data**

**Step1: Translate scRNA-seq data into cell sentence**

- **🔨 SHARE-seq mouse skin dataset**
  - To transform the data using the `transform.py` script, first, define `data_filepath` to point to the location of your downloaded SHARE-seq mouse skin dataset `.h5ad` file. Next, designate `output_dir` for saving the generated cell sentences. Additionally, set the `eval_output_dir` parameter, which will be used to store figures and evaluation metrics. To initiate the transformation, execute the command: `python transform.py`.
  - Configure the `mouse_to_json.py` file by setting the `input_path` to the subdirectory `cell_sentences_hf`, which is the `output_dir` specified in `transform.py`. Then, set `train_json_file_path`, `val_json_file_path`, and `test_json_file_path` to the paths for the train, valid, and test datasets in JSON format, respectively.To execute the script, run: `python mouse_to_json.py`

- **⌨️ GSE149383 and GSE117872 dataset** 

  - Before running `GSE149383_to_json.py` or `GSE117872_to_json.py`, update the `expression_data_path` and `cell_info_path` with the locations of your `erl_total_data_2K.csv` (for GSE149383) or `GSE117872_good_Data_TPM.txt` (for GSE117872) and `erl_total_2K_meta.csv` (for GSE149383) or `GSE117872_good_Data_cellinfo.txt` (for GSE117872) files, respectively. Also, set the `output_json_path` for where you want the JSON outputs. Then, run the script with `python GSE149383_to_json.py` or `python GSE117872_to_json.py`.
  - In `split.py`, make the `input_path` the same as the `output_json_path` from above. Specify paths for `train_json_file_path`, `val_json_file_path`, and `test_json_file_path` for splitting the dataset. Run it with `python split.py`.
  
- **🔍Merge data**

  - In `merge.py`, configure the JSON file paths by specifying the locations for three distinct datasets - training, validation, and testing. These datasets originate from sources such as `GSE117872`, `GSE149383`, and `mouse`. Ensure these paths point to the JSON files previously generated.

**Step2: Train and Generate Execution**

- **🔨 Train**
  - Set the parameters for `train_json_path`, `valid_json_path`, `tokenizer_path`, `model_path`, and `output_dir` in the `finetune.py` script, then run the code directly to initiate the fine-tuning process.
- **⌨️ Generate**
  - For single-instance inference, configure the necessary parameters in `inference_one.py`, then execute `python inference_one.py`.
  - For web interface inference, set the appropriate parameters in `inference_web.py`, followed by running `python inference_web.py`.
  - For batch inference, adjust the required parameters in `inference_batch.py`, then proceed with `python inference_batch.py`.

**Step3: Pseudo-cell Generation - Translating Sentences into Expressions** 

- **🔨Data Extraction**
  - Extract data for generating cells based on cell type (for training datasets larger than 500, encompassing 16 types) by configuring the relevant parameters in `extract_gene_generation.py`. Execute with `python extract_gene_generation.py`.

- **⌨️ Transformation Process**
  - Following the generation of the files above, set the appropriate parameters in `sentence_to_expression.py` and run the script with `python sentence_to_expression.py`.


<h2 id="4">📝 Cite</h2>

If you use our repository, please cite the following related paper:
```
@article{fang2024chatcell,
  title={ChatCell: Facilitating Single-Cell Analysis with Natural Language},
  author={Fang, Yin and Liu, Kangwei and Zhang, Ningyu and Deng, Xinle and Yang, Penghui and Chen, Zhuo and Tang, Xiangru and Gerstein, Mark and Fan, Xiaohui and Chen, Huajun},
  journal={arXiv preprint arXiv:2306.08018},
  year={2024},
}
```


