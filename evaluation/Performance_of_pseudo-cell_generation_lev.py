import numpy as np
from sklearn.metrics import accuracy_score
import anndata
from Levenshtein import distance
from collections import Counter
from tqdm import tqdm
import json

class KNNLevenshtein:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test, y_test):
        predictions = []
        for x in tqdm(X_test):
            prediction = self._predict(x)
            predictions.append(prediction)
        return np.array(predictions)

    def _predict(self, x):
        distances = [distance(x, x_train) for x_train in self.X_train]
        k_neighbors_indices = np.argsort(distances)[:self.k]
        k_neighbor_labels = [self.y_train[i] for i in k_neighbors_indices]
        most_common = Counter(k_neighbor_labels).most_common(1)
        return most_common[0][0]

my_data_path='path_to_your_data.json'
ground_truth_data_path='path_to_ground_truth_data.json'
k = 5

# Load data from the first file
with open(my_data_path, "r", encoding="utf-8") as file:
    data = json.load(file)[0:100]

features = [x['gene'].strip() for x in data]
labels = [x['cell_type'].strip() for x in data]

# Train and predict on the first dataset
knn_model = KNNLevenshtein(k=k)
knn_model.fit(features, labels)
test_pred = knn_model.predict(features, labels)

# Load data from the second file
with open(ground_truth_data_path, "r", encoding="utf-8") as file:
    data = json.load(file)[0:100]
features_gt = [x['gene'].strip() for x in data]
labels_gt = [x['cell_type'].strip() for x in data]

# Train and predict on the second dataset
knn_model_gt = KNNLevenshtein(k=k)
knn_model_gt.fit(features_gt, labels_gt)
test_pred_gt = knn_model_gt.predict(features, labels)

# Evaluate accuracy

accuracy_quality = accuracy_score(labels, test_pred_gt)
print("accuracy_quality:", round(100 * accuracy_quality, 2))
length = len(labels)
count = sum(1 for i in range(length) if test_pred_gt[i] == labels[i] and test_pred[i] == labels[i])
accuracy_discriminability = round(100 * count / len(test_pred_gt), 2)
print("accuracy_discriminability:", accuracy_discriminability)
