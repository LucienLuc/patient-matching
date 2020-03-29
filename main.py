import algorithm
import csv

data = []
with open("Patient Matching Data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

data = data[1:-1]
algorithm.groupByConfidenceScore(data,0.8)