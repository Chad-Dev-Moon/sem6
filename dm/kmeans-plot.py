from random import randint
import matplotlib.pyplot as plt

def generate_random_dataset(num_points, x1_range, x2_range):
  dataset = []
  for _ in range(num_points):
    x1 = randint(x1_range[0], x1_range[1])
    x2 = randint(x2_range[0], x2_range[1])
    dataset.append([x1, x2])
  return dataset

def distance_2d(center, point):
  return ((center[0] - point[0]) ** 2 + (center[1] - point[1]) ** 2) ** 0.5

def get_min_idx(pointVec):
  idx = 0
  minVal = pointVec[0]

  for i in range(1, len(pointVec)):
    if pointVec[i] < minVal:
      minVal = pointVec[i]
      idx = i

  return idx

def plot_and_save_clusters(clusters, centers, filename = 'images/k_means_clustering.png'):
  colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
  k = len(clusters)
  
  for i in range(k):
    plt.plot(
      [point[0] for point in clusters[i]], 
      [point[1] for point in clusters[i]], 
      colors[i] + 'o', 
      label=f'Cluster {i+1}'
    )

  for i in range(k):
    center = centers[i]
    plt.plot(
      center[0], 
      center[1],
      colors[i] + 's', 
      label='Cluster Centers'
    )
  plt.xlabel('X1')
  plt.ylabel('X2')
  plt.title('K-Means Clustering')
  # plt.legend()
  plt.savefig(filename)
  plt.clf()



def k_means_clustering(dataset, k, limit=20):
  dataset_len = len(dataset)
  if k > dataset_len:
    raise ValueError("k cannot be greater than the number of data points in the dataset.")
  
  cluster_centers = []
  x1_points = [row[0] for row in dataset]
  max_x1 = max(x1_points)
  min_x1 = min(x1_points)
  
  x2_points = [row[1] for row in dataset]
  max_x2 = max(x2_points)
  min_x2 = min(x2_points)

  for _ in range(k):
    x1 = randint(min_x1, max_x1)
    x2 = randint(min_x2, max_x2)
    cluster_centers.append([x1, x2])
  
  iterations = 0
  while True:
    pointToClustersDist = []

    for point in dataset:
      pointVec = []

      for center in cluster_centers:
        d = distance_2d(center, point)
        pointVec.append(d)

      pointToClustersDist.append(pointVec)
    
    # now we cluster
    clusters = [[] for _ in range(k)]
    for i in range(dataset_len):
      point = dataset[i]
      
      pointVec = pointToClustersDist[i]
      minIdx = get_min_idx(pointVec)
      
      clusters[minIdx].append(point)
    
    # plot the intermediate clusters
    plot_and_save_clusters(clusters, cluster_centers, f'images/k_m_c_{iterations}.png')
    
    # now we update the cluster centers
    new_cluster_centers = []
    for i in range(k):
      cluster = clusters[i]
      new_center = cluster_centers[i]
      
      # update, only if the cluster is not empty
      if cluster:
        x1_sum = sum(point[0] for point in cluster)
        x2_sum = sum(point[1] for point in cluster)
        new_center = [x1_sum / len(cluster), x2_sum / len(cluster)]
      
      new_cluster_centers.append(new_center)

    # Check for convergence
    if new_cluster_centers == cluster_centers or iterations > limit:
      break

    cluster_centers = new_cluster_centers
    iterations += 1

  return clusters, cluster_centers

if __name__ == "__main__":
  dataset = generate_random_dataset(1000, (0, 200), (0, 200))
  k = 4
  clusters, centers = k_means_clustering(dataset, k)
  print("Clusters:", clusters)
  print("Cluster Centers:", centers)
  
  # plotting
  plot_and_save_clusters(clusters, centers, 'images/k_means_clustering_final.png')