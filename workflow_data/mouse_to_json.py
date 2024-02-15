import json
from datasets import concatenate_datasets, load_from_disk
from random import choice,seed
from src.prompts import construct_cell_type_template, construct_prediction_template
from tqdm  import tqdm

random_seed = 42  # You can use any integer value as the seed
input_path='output_dir_in_transform.py_path'
train_json_file_path = 'mouse/train.json'
val_json_file_path = 'mouse/valid.json'
test_json_file_path = 'mouse/test.json'

# Load the dataset
dataset = load_from_disk(input_path)
train_dataset, val_dataset,test_dataset = dataset["train"], dataset["valid"],dataset["test"]

print(dataset)
seed(random_seed)


def preprocess_function(examples):
    """Preprocess the dataset to generate source and target texts.

    Args:
        examples (Dataset): The slice of the dataset to process.

    Returns:
        list[dict]: A list of processed data containing source and target texts.
    """
    text_column = "cell_type"
    label_column = "input_ids"
    max_length = 1024

    batch_size = len(examples[text_column])
    inputs = []
    targets = []
    for i in tqdm(range(batch_size)):
        prompt_type = choice([0, 1, 2])
        if prompt_type == 0:
            input = construct_cell_type_template(examples["cell_type"][i])
            target = " ".join(examples["input_ids"][i].split(" ")[:100])
        elif prompt_type == 1:
            input = construct_cell_type_template("cell")
            target = " ".join(examples["input_ids"][i].split(" ")[:100])
        else:
            input = construct_prediction_template(
                " ".join(examples["input_ids"][i].split(" ")[:100])
            )
            target = examples["cell_type"][i]

        inputs.append(input)
        targets.append(target)
        
    data_list = []
    for input, target in zip(inputs, targets):
        data_list.append({"source": input, "target": target})
    return data_list

def save_to_json(data, file_path):
    """Save data to a JSON file.

    Args:
        data (list): The data to be saved.
        file_path (str): The path where the JSON file will be saved.
    """
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# Process and save datasets
for dataset, path in zip([train_dataset, val_dataset, test_dataset], [train_json_file_path, val_json_file_path, test_json_file_path]):
    preprocessed_data = preprocess_function(dataset)
    save_to_json(preprocessed_data, path)

