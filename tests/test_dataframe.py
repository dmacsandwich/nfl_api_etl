import pandas as pd

team_df = pd.read_parquet("etl/data/raw/team_ids.parquet")
match_df = pd.read_parquet("etl/data/raw/match_ids.parquet")
athlete_df = pd.read_parquet("etl/data/raw/athlete_ids.parquet")
nfl_df = pd.read_parquet("etl/data/raw/nfl_df.parquet")

print(len(nfl_df))
print(nfl_df.head())