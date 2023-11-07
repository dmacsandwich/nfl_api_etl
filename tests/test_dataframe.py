import pandas as pd

team_df = pd.read_parquet("etl/data/raw/team_ids.parquet")
match_df = pd.read_parquet("etl/data/raw/match_ids.parquet")
athlete_df = pd.read_parquet("etl/data/raw/athlete_ids.parquet")

print(len(athlete_df))
print(athlete_df.columns)