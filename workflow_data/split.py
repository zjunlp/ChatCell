import json
import random

# Set a fixed seed for reproducibility
random.seed(42)

# Load the JSON data
input_path='GSE117872.json'
train_json_file_path='GSE117872/train.json'
val_json_file_path='GSE117872/valid.json'
test_json_file_path='GSE117872/test.json'
with open(input_path, 'r') as file:
    data = json.load(file)

# Shuffle the data randomly for distribution in datasets
random.shuffle(data)

# Calculate the split indices for training, validation, and test sets
train_size = int(0.8 * len(data))  # 80% for training
val_size = int(0.1 * len(data))    # 10% for validation

# Split the data into training, validation, and test sets
train_data = data[:train_size]
val_data = data[train_size:train_size + val_size]
test_data = data[train_size + val_size:]

# Print the sizes of the full dataset and each split to verify
print(f"Total: {len(data)}, Train: {len(train_data)}, Validation: {len(val_data)}, Test: {len(test_data)}")

# Function to save datasets back to JSON files with indentation for readability
def save_to_json(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

# Save each dataset to its respective JSON file
save_to_json(train_json_file_path, train_data)
save_to_json(val_json_file_path, val_data)
save_to_json(test_json_file_path, test_data)
