import pandas as pd

budget_path = "Resources/budget_data.csv"

budget_df = pd.read_csv(budget_path,encoding="utf-8")

#creating column demonstrating the change in amount of profit/losses

budget_df["Change in Profit"] = budget_df["Profit/Losses"].diff()

df = budget_df.set_index("Change in Profit")

#Swapping between df and budget_df here because there was an issue using df with the "Change in Profit" column - is this because the index was set to a column added after the CSV import?

#creating variables to store total months and total profit, as well as average profit and max and min change

month_count = len(budget_df["Date"].unique())
total_profit =  df["Profit/Losses"].sum()
avg_profit = round(budget_df["Change in Profit"].mean(),2)
max_profit =  int(budget_df["Change in Profit"].max())
min_profit =  int(budget_df["Change in Profit"].min())

#creating variables to store the dates of the max and min change in profits

max_date = df.loc[max_profit,"Date"]
min_date = df.loc[min_profit,"Date"]

#printing out to terminal and to text file

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

