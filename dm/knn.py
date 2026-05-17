def create_dataset():
  """ Create a simple dataset for testing """
  X = [
    [1.0, 2.0],
    [1.5, 1.8],
    [5.0, 8.0],
    [6.0, 9.0],
    [1.0, 0.6],
    [9.0, 11.0]
  ]
  y = ['A', 'A', 'B', 'B', 'A', 'B']
  return X, y

def get_distance(train_point, test_point):
  """ Using Euclidean distance """
  len_train_point = len(train_point)
  len_test_point = len(test_point)

  if len_train_point != len_test_point:
    raise ValueError("Dimension of train_point and test_point must be the same.")

  distance = 0
  for i in range(len_train_point):
    distance += (train_point[i] - test_point[i]) ** 2

  return (distance ** 0.5)

def knn_classify(X, y, test_point, k):
  X_len = len(X)
  y_len = len(y)
  if X_len != y_len:
    raise ValueError("Length of X and y must be the same.")

  if X_len == 0:
    raise ValueError("X or y cannot be empty.")

  # find dist of point from all other points
  distances = []
  for i in range(X_len):
    distance = get_distance(X[i], test_point)
    distances.append((distance, y[i]))

  # Sort distances AND select the k nearest neighbors
  distances.sort(key=lambda x: x[0])
  neighbors = distances[:k]

  # Determine the most common class among the neighbors
  classFrequency = {}
  for _, label in neighbors:
    classFrequency[label] = classFrequency.get(label, 0) + 1

  # Get the class with the highest frequency
  max_frequency = 0
  max_frequency_class = None

  for label, frequency in classFrequency.items():
    if frequency > max_frequency:
      max_frequency = frequency
      max_frequency_class = label

  return max_frequency_class

if __name__ == "__main__":
  X, y = create_dataset()
  test_point = [2.0, 3.0]
  k = 3
  predicted_class = knn_classify(X, y, test_point, k)
  print(f"Predicted class for test point {test_point} is: {predicted_class}")
  