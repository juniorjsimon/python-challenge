import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')



with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.DictReader(csvfile)

    #print(csvreader)

    # Read each row of data after the header
    #for row in csvreader:
        #print(row)

    print("Finacial Analysis")
    print("--------------------------")



       

    for row in csvreader:

          total_revenue = 0
        # Calculate the totals
         total_months = total_months + 1

