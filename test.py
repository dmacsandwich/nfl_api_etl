import pandas as pd

test = pd.read_parquet('etl/data/raw/athlete_ids.parquet')
print(test.head())