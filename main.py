from etl.football_team_id import get_team_ids

team_ids = get_team_ids(data=team_ids_data)

#TODO separate logic into etl format. Below should be
import pandas as pd
team_ids_df = pd.DataFrame(team_ids, columns=['team_id', 'team_name'])

print(team_ids_df)