def squared_euclid_dis(point1: list[float], point2: list[float])-> float:
  """
  function to calculate squared euclidean distance between two n-dimensional points
  """
  sum: float = 0.0
  for i in range(len(point1)):
    sum = sum + (point1[i]-point2[i])**2
  return sum

def update_centroids(data: list[list[float]], cluster_tags: list[int], k:int)-> list[list[float]]:
  dim: int = len(data[0]) # no of coordinates of a single data point
  new_centroids = [[0]*dim for _ in range(k)]
  count = [0]*k # keep track of how many points in each cluster

  for i, tag in enumerate(cluster_tags):
    for m in range(dim):
      new_centroids[tag][m] += data[i][m]
    count[tag] += 1
  
  for idx,centroid in enumerate(new_centroids):
    for m in range(dim):
      if count[idx]>0:
        centroid[m] = centroid[m]/count[idx] 

  return new_centroids

def kmeans(data: list[list[float]], k: int):
  centroids: list[list[float]] = data[0:k]
  cluster_tags: list[int] = [None]*len(data) # will store which datapt is closer to which
                                            # centroid thus telling us to which cluster it belongs
                                            # by storing the tag(index of centroid) at the index which
                                            # is equal to the index of datapt in data matrix
  

  # iteration begins
  while True:
    for i, data_pt in enumerate(data):
      min_dis: float = float('inf')
      for j, centroid in enumerate(centroids):
        dis: float = squared_euclid_dis(data_pt, centroid)
        if dis < min_dis:
          min_dis = dis
          cluster_tags[i] = j
    
    new_centroids = update_centroids(data, cluster_tags, k)
    if new_centroids == centroids:
      break
    centroids = new_centroids

  return centroids, cluster_tags
