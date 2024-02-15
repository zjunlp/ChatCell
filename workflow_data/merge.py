import json
import random


def merge_and_shuffle_json(file1_json_file_path, file2_json_file_path, file3_json_file_path):
    """
    Merges and shuffles data from two JSON files and returns the combined list.
    
    :param file1: Path to the first JSON file.
    :param file2: Path to the second JSON file.
    :param file3: Path to the third JSON file.

    :return: Merged and shuffled list of data from both files.
    """
    with open(file1_json_file_path, 'r') as f1, open(file2_json_file_path, 'r') as f2, open(file3_json_file_path, 'r') as f3:
        data1 = json.load(f1)
        data2 = json.load(f2)
        data3 = json.load(f3)
    # Merge and shuffle the data
    merged_data = data1 + data2
    random.seed(42)
    random.shuffle(merged_data)
    # Merge and shuffle the data
    merged_data = data3 +merged_data 
    random.seed(42)
    random.shuffle(merged_data)
    return merged_data

# File paths
mouse_train_json_file_path = 'mouse/train.json'
mouse_val_json_file_path = 'mouse/valid.json'
mouse_test_json_file_path = 'mouse/test.json'

GSE117872_train_json_file_path = 'GSE117872/train.json'
GSE117872_val_json_file_path = 'GSE117872/valid.json'
GSE117872_test_json_file_path = 'GSE117872/test.json'

GSE149383_train_json_file_path = 'GSE149383/train.json'
GSE149383_val_json_file_path = 'GSE149383/valid.json'
GSE149383_test_json_file_path = 'GSE149383/test.json'
# Output file paths
sum_train_json_file_path = 'sum/train.json'
sum_val_json_file_path = 'sum/valid.json'
sum_test_json_file_path = 'sum/test.json'

# Merging and shuffling
sum_train_data = merge_and_shuffle_json(GSE117872_train_json_file_path, GSE149383_train_json_file_path, mouse_train_json_file_path)
sum_val_data = merge_and_shuffle_json(GSE117872_val_json_file_path, GSE149383_val_json_file_path, mouse_val_json_file_path)
sum_test_data = merge_and_shuffle_json(GSE117872_test_json_file_path, GSE149383_test_json_file_path, mouse_test_json_file_path)

# Assuming you intend to write the merged and shuffled data to new JSON files
def write_to_file(data, file_path):
    """
    Writes given data to a file specified by file_path.
    
    :param data: Data to be written.
    :param file_path: Path for the output file.
    """
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, indent=4)


# Writing the merged and shuffled data to files
write_to_file(sum_train_data, sum_train_json_file_path)
write_to_file(sum_val_data, sum_val_json_file_path)
write_to_file(sum_test_data, sum_test_json_file_path)
