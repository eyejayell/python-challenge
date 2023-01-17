import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")

    csv_header = next(csv_reader)
    total_months = 0
    total_profit = 0

    for row in csv_reader:
        total_months +=1
        total_profit += int(row[1])
    print(f"total months: {total_months}")
    print(f"Total profit: {total_profit}")


