import os
import csv

budget_path = os.path.join('/Users/mic_elstan/Desktop/UC Davis Bootcamp/Homeworks/Python-Challenge/Python-challenge/PyBank/Resources')

budget_path_csv = os.path.join(budget_path, 'budget_data.csv')


print ("Financial Analysis")
print("-----------------------------------------")

with open(budget_path_csv, 'r') as csvfile:


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
    
    # PL = Profit/Loss

    average_pl = 0
    total_pl = []
    month_count = 0
    changes_pl = []
    month_total =[]
    current_pl = 0
    end_pl = 0

    for row in csvreader:
        row += 1
        
        net_total = net_total + int(row[1])

        if (int (row[1]) > 0):
            profit = profit + int(row[1])
            row_of_profit +=1

        elif (int (row[1]) < 0):
            loss = loss + int(row[1])
            row_of_loss +=1

        month_total.append(row[0])
        total_pl.append(int(row[1]))

        if (int(row[1]) > max):
            max = int(row[1])
            month_max = row[0]
        elif (int(row[1]) < min):
            min = int(row[1])
            month_min = row[0]
            
        # Average    
        for i in range(len(total_pl) - 1):
            changes_pl.append(total_pl[i + 1] - total_pl[i])

            average_pl = (sum(changes_pl)) / (len(month_total))



print(f"Total Months: {str(row)} ")
print(f"Total: ${str(net_total)}")
print(f"Average Change : ${str('%.2f' % average_pl)}")
print(f"Greatest Increase in Profits: {month_max} (${str(max)})")
print(f"Greatest Decrease in Profits: {month_min} (${str(min)})")

output_file = '/Users/mic_elstan/Desktop/UC Davis Bootcamp/Homeworks/Python-Challenge/Python-challenge/Export.txt'

with open (output_file, 'w') as csvfile:
    file.write("Financial Analysis")
    file.write("------------------------")
    file.write(f"Total Months: {str(row)}")
    file.write(f"Total: ${str(net_total)}")
    file.write(f"Average Change: ${str('%.2f' % average_pl)}")
    file.write(f"Greatest Increase in Profits: {month_max} (${str(max)})")
    file.write(f"Greatest Decrease in Profits: {month_min} (${str(min)})")