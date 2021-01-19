import os
import csv
#film_found= True
BDate=[]
Profit_Losses=[]
Change_profit_losses=[]
month_count=0
max_profit_month=""
max_profit_value=0
min_profit_month=""
min_profit_value=0
previous_value=0
#Suscriber_Count=[]
#Number_Reviews=[]
#Course_length=[]
#selected_movie=[]
csvpath = os.path.join('..','PyBank/Resources','budget_data.csv')
print(csvpath)
with open(csvpath) as csvfile:
    cvsreader = csv.reader(csvfile, delimiter=',')
#    print(cvsreader)
    csv_header = next(cvsreader)
    print(csv_header)
   

    for row in cvsreader:
        if float(row[1])-previous_value>max_profit_value:
            max_profit_value=float(row[1])-previous_value #keep highest profit
            max_profit_month=row[0] 
        elif float(row[1])-previous_value<min_profit_value:
            min_profit_value=float(row[1])-previous_value #keep highest losses
            min_profit_month=row[0] 

        BDate.append(row[0])
        month_count=month_count+1
        Profit_Losses.append(float(row[1]))
        Change_profit_losses.append(float(row[1])-previous_value)
        previous_value=float(row[1])
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: "+ str(month_count))
    print("Total: $"+str(sum(Profit_Losses)))
    print("Average Change: $"+str(sum(Change_profit_losses)/len(Change_profit_losses)))
    print(f"Greatest Increase in Profits:  {max_profit_month} ({max_profit_value})")
    print(f"Greatest Decrease in Profits:  {min_profit_month} ({min_profit_value})")

    # Specify the file to write to
output_path = os.path.join("..", "PyBank/analysis", "financial_analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Financial Analysis"])

    # Write the second row
    csvwriter.writerow(["-------------------------"])

    csvwriter.writerow(["Total Months: "+ str(month_count)])
    csvwriter.writerow(["Total: $"+str(sum(Profit_Losses))])
    csvwriter.writerow(["Average Change: $"+str(sum(Change_profit_losses)/len(Change_profit_losses))])
    csvwriter.writerow([f"Greatest Increase in Profits:  {max_profit_month} ({max_profit_value})"])
    csvwriter.writerow([f"Greatest Decrease in Profits:  {min_profit_month} ({min_profit_value})"])
