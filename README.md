

<div align="center">


<h2 align="center">  <img src="figure/logo.png" width="8%" height="18%"> ChatCell: Facilitating Single-Cell Analysis with Natural Language </h2>

<p align="center">
  <a href="https://www.zjukg.org/project/ChatCell">💻 Project Page</a> •
  <a href="https://huggingface.co/datasets/zjunlp/Single-cell-Instructions">🤗 Dataset</a> •
  <a href="https://huggingface.co/spaces/zjunlp/Chatcell">🍎 Demo</a> •
  <a href="#overview">🏖️ Overview</a> •
  <a href="#tasks">🧬 Single-cell Analysis Tasks</a> •
  <a href="#quickstart">🛠️ Quickstart</a> •
  <a href="#citation">📝 How to cite</a>
</p>

[![Code License](https://img.shields.io/badge/Code%20License-MIT-green.svg)](https://github.com/zjunlp/ChatCell/blob/main/LICENSE)
[![Data License](https://img.shields.io/badge/Data%20License-CC%20BY%204.0-red.svg)](https://github.com/zjunlp/ChatCell/blob/main/DATA_LICENSE)


<div align=center><img src="figure/intro.gif" width="60%" height="100%" /></div>
ChatCell allows researchers to input instructions in either natural or single-cell language, thereby facilitating the execution of necessary tasks in single-cell analysis. Black and red texts denote human and single-cell language, respectively.

</div>

## 🆕 News

- \[**Feb 2024**\] We released the model weights and datasets.


## 📌 Table of Contents

- <a href="#overview">🏖️ Overview</a>
- <a href="#task">🧬 Single-cell Analysis Tasks</a>
- <a href="#quickstart">🛠️ Quickstart</a>
- <a href="#citation">📝 How to cite</a>
---

## 🏖️ Overview

Single-cell biology examines the intricate functions of the cells, ranging from energy production to genetic information transfer, playing a critical role in unraveling the fundamental principles of life and mechanisms influencing health and disease. The field has witnessed a surge in single-cell RNA sequencing (scRNA-seq) data, driven by advancements in high-throughput sequencing and reduced costs. Traditional single-cell foundation models leverage extensive scRNA-seq datasets, applying NLP techniques to analyze gene expression matrices—structured formats that simplify scRNA-seq data into computationally tractable representations—during pre-training. They are subsequently fine-tuned for distinct single-cell analysis tasks, as shown in Figure (a).

<p align="center">
<img src="figure/overview.jpg"  width="60%" height="60%">
</p>
