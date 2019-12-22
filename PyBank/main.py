# import module
import os
import csv

# file path
csvpath = os.path.join('Resources', 'budget_data.csv')


# variables 
total_months = 0
total_revenue = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# open and read csv
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # read header row first
    csv_header = next(csvreader)
    row = next(csvreader)


    # print the output header
    print(f"Financial Analysis")
    print(f"---------------------------") 
    
    # calculate total number oof months, Net Amount profits and set the variables for the rows
    previous_row = int(row[1])
    total_months = total_months + 1
    net_amount = net_amount + int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

   
    for row in csvreader:

   
        # Calculate the total number of months
         total_months = total_months + 1

         #Net amount of profit/loss over entire period
         net_amount = net_amount + int(row[1])

         #Calculate average changes in "Profit/Losses" over the entire period
         revenue_change = int(row[1]) - previous_row
         monthly_change.append(revenue_change)
         previous_row = int(row[1])
         month_count.append(row[0])

        # Calculate The Greatest Increase
         if int(row[1]) > greatest_increase:
             greatest_increase = int(row[1])
             greatest_increase_month = row[0]
            
        # Calculate The Greatest Decrease
         if int(row[1]) < greatest_decrease:
             greatest_decrease = int(row[1])
             greatest_decrease_month = row[0]  
        

    # Calculate The Average & The Date
    average_change = sum(monthly_change)/ len(monthly_change)
    
    # max and min monthly change
    highest = max(monthly_change)
    lowest = min(monthly_change)

 
  
# Print the output analysis
print(f"Total Months: {total_months}")
print(f"Total: $ {net_amount}")
print(f"Average Change: $ {average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${highest})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest})")

# Specify the file to write on
output_file = os.path.join('PyBank_Results.txt')

# Open and write to file
with open(output_file, 'w',) as txtfile:

# Write data to a text file
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: $ {net_amount}\n")
    txtfile.write(f"Average Change: $ {average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest})\n")