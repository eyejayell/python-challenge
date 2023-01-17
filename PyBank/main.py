import pandas as pd

budget_path = "Resources/budget_data.csv"

budget_df = pd.read_csv(budget_path,encoding="utf-8")
budget_df.head()

budget_df["Change in Profit"] = budget_df["Profit/Losses"].diff()
budget_df.head()

df = budget_df.set_index("Change in Profit")
df.head()

month_count = len(budget_df["Date"].unique())
total_profit =  df["Profit/Losses"].sum()
avg_profit = budget_df["Change in Profit"].mean()
max_profit =  budget_df["Change in Profit"].max()
min_profit =  budget_df["Change in Profit"].min()

max_date = df.loc[max_profit,"Date"]
min_date = df.loc[min_profit,"Date"]


print(f"Total Months: {month_count}")
print(f"Total Profit: {total_profit}")
print(f"Average Change: {avg_profit}")
print(f"Greatest Increase in Profits: {max_date} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_date} (${min_profit})")


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


