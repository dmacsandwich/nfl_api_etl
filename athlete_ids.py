from api.data_sources.athlete_ids_by_year import AthleteIds
import pandas as pd

team_ids = pd.read_parquet("/Users/JinsooWhang/Desktop/개인적인/Data Eng/projects/nfl_api_etl/etl/data/raw/team_ids.parquet")
team_ids = list(team_ids.team_id)
year_range = [2019,2020,2021,2022]

athlete_data =  AthleteIds().get_athlete_by_id_and_year(years=year_range, team_ids=team_ids)
athlete_ids = []

def get_athlete_ids(data: list[dict])-> list[tuple]:
    
    for team_id in team_ids:
        for position in [0, 1, 2]:
            num_athletes = len(athlete_data[int(team_id)]['athletes'][position]['items'])
            for i in range(num_athletes):
                athlete_ids.append(
                    (
                        athlete_data[int(team_id)]['athletes'][position]['items'][i]['id'],
                        athlete_data[int(team_id)]['athletes'][position]['items'][i]['fullName'],
                        athlete_data[int(team_id)]['athletes'][position]['items'][i]['weight'],
                        athlete_data[int(team_id)]['athletes'][position]['items'][i]['height'],
                        athlete_data[int(team_id)]['athletes'][position]['items'][i]['dateOfBirth']
                    )
                )

    return athlete_ids

athlete_ids_data = get_athlete_ids(athlete_data)
athlete_ids_df = pd.DataFrame(athlete_ids_data, columns=['id', 'fullName', 'weight', 'height', 'dateOfBirth'])

print(athlete_ids_df)
print(len(athlete_ids_df))


# Specify the path to save the Parquet file
parquet_file_path = "etl/data/raw/athlete_ids.parquet"

athlete_ids_df.to_parquet(parquet_file_path)

print(f"Data saved to {parquet_file_path}")





"""
# Open the file in write mode ('w')
with open('myfile.json', 'w') as f:
# Write some text to the file
    f.write(str(athlete_data))
"""