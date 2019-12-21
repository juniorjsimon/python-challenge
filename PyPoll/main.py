# Import Modules
import os
import csv

# file path
csvpath = os.path.join('Resources', 'election_data.csv')

# Variables
total_votes = 0


# open and read csv
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # read header row first
    csv_header = next(csvreader)
    row = next(csvreader)

 