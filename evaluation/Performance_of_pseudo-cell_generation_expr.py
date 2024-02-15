import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import anndata
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
import scanpy as sc
import pandas as pd

# Load data
my_data_path=""
ground_truth_data_path=""
k = 5

my_data = anndata.read_h5ad(my_data_path)
ground_truth_data = anndata.read_h5ad(ground_truth_data_path)

# Check if gene names from my_data match those from ground_truth_data
genes_my_data = my_data.var_names
genes_ground_truth_data = ground_truth_data.var_names
if not np.array_equal(genes_my_data, genes_ground_truth_data):
    #align my_data to contain the gene names present in ground_truth_data
    my_data=my_data[:,genes_ground_truth_data]

# Extract features and labels
features = my_data.X
labels = my_data.obs['cell_type']
features_gt = ground_truth_data.X
labels_gt = ground_truth_data.obs['cell_type']

# KNN Classifier
knn = KNeighborsClassifier(n_neighbors=k)
knn_gt = KNeighborsClassifier(n_neighbors=k)

# Train and predict
knn.fit(features, labels)
knn_gt.fit(features_gt, labels_gt)
test_pred = knn.predict(features)
test_pred_gt = knn_gt.predict(features)

# Evaluate accuracy
accuracy_quality = accuracy_score(labels, test_pred_gt)
print("accuracy_quality:", round(100 * accuracy_quality, 2))

# Compare predictions
length = len(labels)
count = sum(1 for i in range(length) if test_pred_gt[i] == labels[i] and test_pred[i] == labels[i])
accuracy_discriminability = round(100 * count / length, 2)
print("accuracy_discriminability:", accuracy_discriminability)
