# loading dataset into 2D matrix
import csv

def load_data(FILE_PATH: str) -> list[list[float]]:
  """
  Loads csv data into a 2D matrix where each row-list represents a single data point
  """
  data = []
  with open(FILE_PATH, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    # next(csvreader) # Omit the the first line, i.e., the header
    for line in csvreader:
      data.append([float(value) for value in line[:-1]])
  
  return data