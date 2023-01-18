import pandas as pd

election_path = "Resources/election_data.csv"

election_df = pd.read_csv(election_path,encoding="utf-8")

total_votes = election_df["Ballot ID"].count()

vote_total_groups = election_df.groupby(["Candidate"])

vote_total_df = vote_total_groups.count()
vote_total_df
