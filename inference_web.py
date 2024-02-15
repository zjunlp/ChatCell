import gradio as gr
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    HfArgumentParser,
    Trainer,
    TrainingArguments,
    AutoModelForSeq2SeqLM,
)
import torch
model_folder = "zjunlp/chatcell-small"
tokenizer = AutoTokenizer.from_pretrained(model_folder)
model = AutoModelForSeq2SeqLM.from_pretrained(model_folder)
model.eval()



def run_detector(input_text):
    # Encode the input text and generate a response with specified generation parameters
    input_ids = tokenizer(input_text,return_tensors="pt").input_ids.to(device)
    output_ids = model.generate(input_ids, max_length=512, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50, top_p=0.95, do_sample=True)
    # Decode and print the generated output text
    output_text = tokenizer.decode(output_ids[0],skip_special_tokens=True)

    return output_text




css = """
.green { color: black!important;line-height:1.9em; padding: 0.2em 0.2em; background: #ccffcc; border-radius:0.5rem;}
.red { color: black!important;line-height:1.9em; padding: 0.2em 0.2em; background: #ffad99; border-radius:0.5rem;}
.hyperlinks {
  display: flex;
  align-items: center;
  align-content: center;
  padding-top: 12px;
  justify-content: flex-end;
  margin: 0 10px; /* Adjust the margin as needed */
  text-decoration: none;
  color: #000; /* Set the desired text color */
}
"""

capybara_problem=''
with gr.Blocks(css=css,
               theme=gr.themes.Soft(text_size="sm")) as app:
    
    with gr.Row():

        gr.HTML("""
                <div style="text-align: center; margin: 0 auto;">
                <p><h1> Chatcell: Facilitating Single-Cell Analysis with Natural Language</h1>
                </div>

        """)
    with gr.Row():
        gr.Markdown("<p align='center'><a href='https://www.zjukg.org/project/ChatCell'>🐣Project</a> &nbsp;&nbsp;&nbsp; <a href='https://arxiv.org/abs/2306.08018'>📃Paper</a>&nbsp;&nbsp;&nbsp; <a href='https://github.com/zjunlp/ChatCell'>🥳Code</a></p>")

    with gr.Row():
        input_box = gr.Textbox(value=capybara_problem, placeholder="Enter text here", lines=4, label="Input Text", )
    with gr.Row():
        output_text = gr.Textbox(label="Prediction")

    with gr.Row():
        clear_button = gr.ClearButton()
        submit_button = gr.Button(variant="primary")

    examples = gr.Examples(
        examples=[
            ["List the initial 100 genes associated with a TAC-1:"],
            ["Enumerate the 100 most abundantly expressed starting genes in a cell:"],
            ["Could you determine the likely cell type based on these 100 most expressed genes? GM42418 IL1RAPL1 CDK8 MALAT1 JARID2 CAMK1D ZC3H7A GPHN LARS2 HEXB FGFR2 BRWD1 CASC5 MCCC2 NEAT1 PCNT NFIA NIPBL KIF23 GM26917 BZW1 MYOF PRPF38B HSPA9 HNRNPAB RORA ANLN AHNAK CIT ATRX ADGRG6 RTF1 SMC1A TENM1 HMCN1 LDLRAD4 QK AKAP13 LUC7L3 COL1A2 STX12 PTPN14 AKIRIN1 SNRNP48 MYH9 ATXN1 TRAPPC8 MKL1 MAN1A2 S100A14 DPM1 VPS13C FAM132A AMOT ITGA9 TCF4 ARF6 MBNL1 RPS6KC1 ANXA1 NAA35 SRSF6 GGTA1 2410089E03RIK CRYBG3 SMURF1 LITAF CERS6 BEND6 SRSF4 MTUS1 PLCH2 RBM27 ABCB7 PIEZO1 CUL2 RBMS1 RIC8B PTMA CEP128 HNRNPH1 HMMR KPNA4 MTDH EFNA5 EIF2B2 LARP4B SFSWAP CEP83 SLCO3A1 POLR2A KIF20A PGLYRP4 SLC39A11 ITPR2 CDC42SE1 COX7C NCAPG FKBP5 RIOK3 These genes are commonly found in:"],
            ["Distinguish between resistant and sensitive cancer cells in response to Cisplatin, using the data from the 100 most expressed genes in descending order MYL12B FTL MYL12A HIST1H4C RPL23 GSTP1 RPS3 ENO1 RPLP1 TXN ANXA2 PPP1CB B2M RPLP0 HSPA8 H2AFZ TPI1 ANXA1 RPL7 GAPDH CHP1 LDHA RPL3 S100A11 PRDX1 CALM2 CAPZA1 SLC25A5 RPS27 YWHAZ GNB2L1 PTBP3 RPS6 MOB1A S100A2 ACTG1 BROX SAT1 RPL35A CA2 PSMB4 RPL8 TBL1XR1 RPS18 HNRNPH1 RPL27 RPS14 RPS11 ANP32E RPL19 C6ORF62 RPL9 EEF1A1 RPL5 COLGALT1 NPM1 CCT6A RQCD1 CACUL1 RPL4 HSP90AA1 MALAT1 ALDOA PSMA4 SEC61G RPL38 PSMB5 FABP5 HSP90AB1 RPL35 CHCHD2 EIF3E COX4I1 RPL21 PAFAH1B2 PTMA TMED4 PSMB3 H3F3B AGO1 DYNLL1 ATP5A1 LDHB COX7B ACTB RPS27A PSME2 ELMSAN1 NDUFA1 HMGB2 PSMB6 TMSB10 SET RPL12 RPL37A RPS13 EIF1 ATP5G1 RPS3A TOB1."],
            ["Evaluate a cancer cell's response to Erlotinib (resistant or sensitive), based on the cell's 100 most actively expressed genes in descending order MT-RNR2 MT-CO3 MT-CO1 RPL13 RPLP1 FTH1 GAPDH RPS8 PABPC1 FTL ANXA2 NCL RPS12 PTMA RPS14 CAV1 RPS3 RPS4X MT-CO2 RPL37 KRT7 RPS2 TMSB4X HSP90AA1 GSTP1 MT-ND4 MT-ATP6 S100A6 NAP1L1 RPL31 HSP90AB1 B2M RPL19 PPIA NUCKS1 MT-ND5 RPS27A TPM1 RPL18 ATP5G3 RPLP0 RPL8 TXN GNAS PSMA7 RPL30 MYL6 SLC25A5 RAD21 RTN4 RPL37A HSPD1 LRRFIP1 DEK MT-ND1 RPL11 TPT1 TMSB10 RPS24 SSRP1 LUC7L3 RPS20 KRT18 RPS16 RPL5 RPL35 RPS21 HNRNPC RPLP2 NACA GNB2L1 LGALS1 UQCRH FAU CHCHD2 RPL23 LDHB UBA52 HSP90B1 SEC62 RPL6 DSTN RPL27A RPL23A RPL22L1 KTN1 RPL14 CALM2 PRDX1 ADIPOR2 ZFAS1 HIST1H4C UQCRQ CALU PTTG1 EIF1 RPL26 RPL10A RAN ARPC2."]
        ],
        examples_per_page=3,
        inputs=[input_box],
    )



    with gr.Accordion("Disclaimer", open=False):
        gr.Markdown(
            """
            - `Accuracy` :
                - AI-generated text detectors aim for accuracy, but achieving 100% is challenging.
                - The provided prediction is for demo purposes only and should not be considered a consumer product.
                - Users are advised to exercise discretion, and we assume no liability for any use.
            - `Detection Use Cases` : 
                - In this work, our focus is to achieve an ultra-low false positive rate, crucial for sensitive downstream use case (e.g., avoiding false accusations in academic honesty cases). 
                - We find optimal application in content moderation, for example in detecting AI-generated reviews on platforms like Amazon, Google, Yelp, etc. This represents one of the most compelling and noteworthy use cases for Binoculars.
            - `Human Supervision Advisory` :
                - Strongly caution against using Binoculars (or any detector) without human supervision.
            - `Performance by Language` :
                - As noted in our paper, Binoculars exhibit superior detection performance in the English language compared to other languages.
            """
        )
    with gr.Accordion("Cite our work", open=False):
        gr.Markdown(
            """
            ```bibtex
            @article{fang2024chatcell,
                  title={ChatCell: Facilitating Single-Cell Analysis with Natural Language},
                  author={Fang, Yin and Liu, Kangwei and Zhang, Ningyu and Deng, Xinle and Yang, Penghui and Chen, Zhuo and Tang, Xiangru and Gerstein, Mark and Fan, Xiaohui and Chen, Huajun},
                  journal={arXiv preprint arXiv:2306.08018},
                  year={2024}
            }
            """
        )

    submit_button.click(run_detector, inputs=input_box, outputs=output_text)
    clear_button.click(lambda: ("", ""), outputs=[input_box, output_text])

app.launch()
# 📙
