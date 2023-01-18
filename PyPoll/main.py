import pandas as pd

election_path = "Resources/election_data.csv"

election_df = pd.read_csv(election_path,encoding="utf-8")


total_votes = election_df["Ballot ID"].count()

#create dataframe grouping candidates by number of votes

vote_total_groups = election_df.groupby(["Candidate"], as_index=False)

vote_total_df = vote_total_groups.count()
del vote_total_df["County"]
#percentage formatting found here: https://stackoverflow.com/questions/51355282/add-percentage-column-to-panda-dataframe-with-percent-sign
vote_total_df["Percentage"] = ((vote_total_df["Ballot ID"] / vote_total_df["Ballot ID"].sum()) * 100).round(3).astype(str) + "%"

vote_total_df = vote_total_df[["Candidate","Percentage","Ballot ID"]]

#find winner using a sorted dataframe

winner_df = vote_total_df.sort_values("Ballot ID", ascending=False)
winner_df = winner_df.reset_index(drop=True)

winner = winner_df["Candidate"].values[0]

print(winner)
#print results to terminal and to text file

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(vote_total_df.to_string(header=False,index=False))
print("-------------------------")
print(f"Winner: {winner}")

with open("output.txt","a") as file:
    print("Election Results",file=file)
    print("-------------------------",file=file)
    print(f"Total Votes: {total_votes}",file=file)
    print("-------------------------",file=file)
    vote_total_text = vote_total_df.to_string(header=False, index=False)
    file.write(vote_total_text)
    print("",file=file)
    print("-------------------------",file=file)
    print(f"Winner: {winner}",file=file)
