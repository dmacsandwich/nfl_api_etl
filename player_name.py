from api.nfl_api import NflApi
from api.urls import ATHLETE_IDS
from football_team_id import team_ids_df
import pandas as pd
import polars as pl


athlete_data =  NflApi().get_data_from_url(url = ATHLETE_IDS)


def get_athlete_ids(data: list[dict])-> list[tuple]:
    athlete_ids = []

    for position in [0, 1, 2]:
        num_athletes = len(athlete_data['athletes'][position]['items'])
        for i in range(num_athletes):
            athlete_ids.append(
                (
                    athlete_data['athletes'][position]['items'][i]['id'],
                    athlete_data['athletes'][position]['items'][i]['fullName'],
                    athlete_data['athletes'][position]['items'][i]['weight'],
                    athlete_data['athletes'][position]['items'][i]['height'],
                    athlete_data['athletes'][position]['items'][i]['dateOfBirth']
                )
            )

    return athlete_ids

athlete_ids_data = get_athlete_ids(athlete_data)
athlete_ids_df = pd.DataFrame(athlete_ids_data, columns=['id', 'fullName', 'weight', 'height', 'dateOfBirth'])


# Convert the Pandas DataFrame to a Polars DataFrame
polars_df = pl.DataFrame(athlete_ids_df)

# Specify the path to save the Parquet file
parquet_file_path = "datasets/athlete_ids.parquet"

# Save the Polars DataFrame to Parquet format
polars_df.write_parquet(parquet_file_path)


print(f"Data saved to {parquet_file_path}")



