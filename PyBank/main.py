import pandas as pd

budget_path = "Resources/budget_data.csv"

budget_df = pd.read_csv(budget_path,encoding="utf-8")
budget_df.head()

budget_df["Change in Profit"] = budget_df["Profit/Losses"].diff()
budget_df.head()

df = budget_df.set_index("Change in Profit")
df.head()

#Swapping between df and budget_df here because there was an issue using df with the "Change in Profit" column - is this because the index was set to a column added after the CSV import?

month_count = len(budget_df["Date"].unique())
total_profit =  df["Profit/Losses"].sum()
avg_profit = round(budget_df["Change in Profit"].mean(),2)
max_profit =  int(budget_df["Change in Profit"].max())
min_profit =  int(budget_df["Change in Profit"].min())

max_date = df.loc[max_profit,"Date"]
min_date = df.loc[min_profit,"Date"]


print(f"Total Months: {month_count}")
print(f"Total Profit: {total_profit}")
print(f"Average Change: {avg_profit}")
print(f"Greatest Increase in Profits: {max_date} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_date} (${min_profit})")

with open("output.txt","a") as file:
    print(f"Total Months: {month_count}", file=file)
    print(f"Total Profit: {total_profit}", file=file)
    print(f"Average Change: {avg_profit}",file=file)
    print(f"Greatest Increase in Profits: {max_date} (${max_profit})",file=file)
    print(f"Greatest Decrease in Profits: {min_date} (${min_profit})",file=file)


# import os
# import csv

# budget_csv = os.path.join("Resources","budget_data.csv")

# profit_losses = []

# with open(budget_csv) as csv_file:
#     csv_reader = csv.reader(csv_file,delimiter=",")

#     csv_header = next(csv_reader)
#     total_months = 0
#     total_profit = 0

#     for row in csv_reader:
#         total_months +=1
#         total_profit += int(row[1])

#         profit_losses.append(row[1])

#     print(f"total months: {total_months}")
#     print(f"Total profit: {total_profit}")
    
# print(profit_losses)

#max_profit = max(profit_losses)
    
#print(max_profit)


