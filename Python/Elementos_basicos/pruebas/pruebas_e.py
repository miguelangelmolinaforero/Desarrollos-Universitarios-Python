import csv
import operator

l = [[1, 2, 3, 4], [5, 6, 7, 8]]

with open("output.csv", "wb") as f:
  writer = csv.writer(f)
  writer.writerows(zip(*l))