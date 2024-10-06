from data_loader import load_data
from kmeans_algo import kmeans
from visualization import visualize_clusters_3d

if __name__ == "__main__":
  FILE_PATH = "../iris/iris.data"
  data = load_data(FILE_PATH)
  
  k = 3
  final_centroids, cluster_tags = kmeans(data, k)

  for i in range(k):
    print(f"Cluster {i+1}")
    print(f"Centroid is {final_centroids[i]}")
    print()
  for i,tag in enumerate(cluster_tags):
    print(f"datapt {i+1} belongs to Cluster {tag+1}")

  visualize_clusters_3d(data, final_centroids, cluster_tags)
