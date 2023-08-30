import csv
from package import Package
from hashmap import HashMap

# Replace this with the actual path to your CSV file
file_path = 'WGUPS Package File.csv'

# Open the CSV file and create a CSV reader
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
     
    # Iterate through each row in the CSV file
    for row in csvreader:
        print(row)