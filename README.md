# Clustering Algorithms on the Iris Dataset

Data Mining First Assignment by Prof. Dr. Monalisa Mandal.
- The Final Assignment PDF is [here](https://github.com/sensoubhik11/CS9030-assignment1/blob/master/24MA4108.pdf)
- The Notebook for KMeans Clustering is [here](https://github.com/sensoubhik11/CS9030-assignment1/blob/master/K-Means%20Algorithm.ipynb)
- The Notebook for DBSCAN Clustering is [here](https://github.com/sensoubhik11/CS9030-assignment1/blob/master/DBSCAN.ipynb)
- The Notebook for Algomerative Hierarchical Clustering is [here](https://github.com/sensoubhik11/CS9030-assignment1/blob/master/AHC.ipynb)

## Introduction

This project implements various clustering algorithms on the Iris dataset, including K-Means, DBSCAN, and Agglomerative Hierarchical Clustering (AHC). The goal is to analyze the dataset and visualize the results to understand how different algorithms categorize the data.

## Project Description

In this assignment, we explore three clustering algorithms:

1. **K-Means Clustering**: A manual implementation of the K-Means algorithm, providing a visualization of the clusters formed.
2. **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**: Utilizes a library to perform DBSCAN clustering, accompanied by cluster visualizations.
3. **Agglomerative Hierarchical Clustering**: Implements single linkage, complete linkage, average linkage, and Ward’s method. Visualizes the results using dendrograms.

```
├── iris/
│   ├── iris.data               # Iris dataset (no headers)
├── K-Means Algorithm.ipynb  # Notebook with K-Means algorithm implementation
├── DBSCAN.ipynb             # Notebook with DBSCAN clustering implementation
├── AHC.ipynb                # Notebook with Agglomerative Hierarchical Clustering
├── Front-Page.ipynb
├── Assignment-1.ipynb       # Final Merged Notebook
├── 24MA4108.pdf             # Final Assignment PDF
├── README.md                # Project's README file
└── requirements.txt         # Dependencies required to run the project
```
## Dataset

The dataset used in this project is the Iris dataset, which consists of the following features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width
- Species (used for reference but not for clustering)

## Requirements

To run this project, you will need the following Python packages:

- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- scipy

## Installation

To run this project on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/sensoubhik11/CS9030-assignment1.git
   cd CS9030-assignment1
    ```

2. You can create a virtual environment and then install the required packages using the following command:

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3. Then run jupyer-lab which you can access at localhost:8888
   ```bash
   jupyter-lab
   ```
## How to Use

### K-Means Clustering:
- Open the `KMeans_Clustering.ipynb` file in Jupyter.
- Run through the notebook to view the code implementation and visualizations.

### DBSCAN Clustering:
- Open the `DBSCAN_Clustering.ipynb` notebook.
- Run all the cells from dataset loading to cluster visualization.

### Agglomerative Hierarchical Clustering (AHC):
- Open the `AHC_Clustering.ipynb` file.
- Execute the notebook to view the dendrograms for different linkage methods.

