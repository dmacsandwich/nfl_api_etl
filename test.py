import pandas as pd

test = pd.read_parquet('etl/data/raw/match_ids.parquet')
print(test.head())