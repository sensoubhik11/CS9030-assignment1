import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

def visualize_clusters_3d(data: list[list[float]], centroids: list[list[float]], cluster_tags: list[int]):
  # Use PCA to reduce data to 3 dimensions
  pca = PCA(n_components=3)
  data_3d = pca.fit_transform(data)
  centroids_3d = pca.transform(centroids)

  fig = plt.figure(figsize=(10, 8))
  ax = fig.add_subplot(111, projection='3d')  # Create a 3D axis

  # Plot each cluster
  for cluster in range(len(centroids_3d)):
    # Get the points for the current cluster
    cluster_points = [data_3d[i] for i in range(len(data_3d)) if cluster_tags[i] == cluster]

    # Extract x, y, z coordinates from reduced 3D data
    x_coords = [point[0] for point in cluster_points]
    y_coords = [point[1] for point in cluster_points]
    z_coords = [point[2] for point in cluster_points]

    ax.scatter(x_coords, y_coords, z_coords, label=f'Cluster {cluster + 1}', alpha=0.7)
  
  # Plot the centroids
  centroids_x = [centroid[0] for centroid in centroids_3d]
  centroids_y = [centroid[1] for centroid in centroids_3d]
  centroids_z = [centroid[2] for centroid in centroids_3d]
  ax.scatter(centroids_x, centroids_y, centroids_z, color='black', marker='*', s=100, label='Centroids')

  ax.set_title('K-means Clustering in 3D (PCA Reduced)')
  ax.set_xlabel('Principal Component 1')
  ax.set_ylabel('Principal Component 2')
  ax.set_zlabel('Principal Component 3')  # Label the z-axis
  ax.legend()

  plt.savefig('../output/kmeans_cluster3d_pca.png')
  plt.close()
