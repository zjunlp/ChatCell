To evaluate the performance of various tasks, follow these steps:

- Change to the evaluation directory with the command: `cd evaluation`.

- Random Cell Generation Task:
  - Open `Performance_of_random_cell_generation.py`.
  - Specify the `json_path` to the JSON file with the generated data.
  - Specify the `global_path` to the global gene vocabulary file, usually located in the `cell_sentences` subdirectory within `output_dir` specified by the `transform.py` script, and is named `vocab_human.txt`.￼￼￼
  - Run the command: `python Performance_of_random_cell_generation.py`. 

- Pseudo-cell Generation Task:
  - Depending on the format of your data, open `python Performance_of_pseudo-cell_generation_lev.py`, or `python Performance_of_pseudo-cell_generation_expr.py`.
  - Specify the `my_data_path` to the JSON file with the generated pseudo-cell data.
  - Specify the `ground_truth_data_path` to the JSON file with the ground truth data.
  - Specify the `k` to the K-value for KNN analysis.
  - Depending on the format of your data, run: `python Performance_of_pseudo-cell_generation_lev.py`, or `python Performance_of_pseudo-cell_generation_expr.py`.

- Cell Type Annotation and Drug Sensitivity Prediction Tasks:
  - Open `python performance_of_classification.py`.
  - Specify the `my_data_path` to the JSON file containing the generated data for the task.
  - Run the command: `python performance_of_classification.py`.
