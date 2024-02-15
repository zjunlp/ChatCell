from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import json

# Path to your data file
my_data_path = 'path_to_your_data.json'

# Load data from the JSON file
with open(my_data_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract true labels and predicted labels
y_true = [x['target'].strip().lower() for x in data]  # Replace with your true labels
y_pred = [x['my_target'].strip().lower() for x in data]  # Replace with your predicted labels

# Calculate evaluation metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='weighted')
recall = recall_score(y_true, y_pred, average='weighted')
f1 = f1_score(y_true, y_pred, average='weighted')

# Print evaluation metrics
print("Accuracy: ", round(100 * accuracy, 2))
print("Precision: ", round(100 * precision, 2))
print("Recall: ", round(100 * recall, 2))
print("F1 Score: ", round(100 * f1, 2))
