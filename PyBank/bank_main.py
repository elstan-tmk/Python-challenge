import os
import csv


#budget_path = os.path.join(".", "Resources")

#budget_path_csv = os.path.join(budget_path, 'budget_data.csv')


with open('Resources/budget_data.csv', 'r') as csvfile:


    csvreader = csv.reader(csvfile, delimiter = ',')
    # Read header row
    header = next(csvreader)

    # set all the data into 0 
    row = 0
    profit = 0
    loss = 0
    net_total = 0
    row_of_profit = 0
    row_of_loss = 0
    min = 0
    max = 0
    
    # revenue = Profit/Loss

    average_revenue = 0
    total_revenue = 0
    month_count = 0
    changes_revenue = []
    month_total = 0
    greatest_increase = ["", 0]
    greatest_decrease = ["", 9999999999999]
    
    
    month_total += 1
    first_row = next(csvreader)
    total_revenue += int(first_row[1])
    prev_revenue = int(first_row[1])
    

    for row in csvreader:
        month_total += 1
        total_revenue += int(row[1])
        
        net_total = net_total + int(row[1])
        net_change = int(row[1]) - prev_revenue     #value of current month - value of previous

        prev_revenue = int(row[1])                  # Reset the value of prev_net to the row

        changes_revenue += [net_change]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

       
    average_revenue = sum(changes_revenue) / len(changes_revenue)



print(f"Total Months: {month_total} ")
print(f"Total: ${str(net_total)}")
print(f"Average Change : ${str('%.2f' % average_revenue)}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

output_file = os.path.join("bankdata.txt")


with open (output_file, 'w') as csvfile:
    csvfile.write("Financial Analysis\n")
    csvfile.write("------------------------\n")
    csvfile.write(f"Total Months: {month_total}\n")
    csvfile.write(f"Total: ${str(net_total)}\n")
    csvfile.write(f"Average Change: ${str('%.2f' % average_revenue)}\n")
    csvfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    csvfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")