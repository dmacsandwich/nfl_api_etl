import pandas as pd

athlete_df = pd.read_parquet("etl/data/raw/athlete_ids.parquet")
match_df = pd.read_parquet("etl/data/raw/match_ids.parquet")
team_df = pd.read_parquet("etl/data/raw/team_ids.parquet")


# Merge for home team
nfl_df = match_df.merge(team_df, left_on='home_team_id', right_on='team_id', how='left')
nfl_df = nfl_df.rename(columns={'team_name': 'home_team_name'}).drop(columns='team_id')

# Merge for away team
nfl_df = nfl_df.merge(team_df, left_on='away_team_id', right_on='team_id', how='left')
nfl_df = nfl_df.rename(columns={'team_name': 'away_team_name'}).drop(columns='team_id')

# Merge for passing leader name
nfl_df = nfl_df.merge(athlete_df[['id', 'fullName']], left_on='passing_leader_id', right_on='id', how='left')
nfl_df = nfl_df.rename(columns={'fullName':'passing_leader_name'}).drop(columns='id_y')

# Merge for rushing leader name
nfl_df = nfl_df.merge(athlete_df[['id', 'fullName']], left_on='rushing_leader_id', right_on='id', how='left')
nfl_df = nfl_df.rename(columns={'fullName':'rushing_leader_name'}).drop(columns='id')

# Merge for receiving leader name
nfl_df = nfl_df.merge(athlete_df[['id', 'fullName']], left_on='receiving_leader_id', right_on='id', how='left')
nfl_df = nfl_df.rename(columns={'fullName':'receiving_leader_name'}).drop(columns='id')

# Merge for passing leader team name
nfl_df = nfl_df.merge(team_df, left_on='passing_leader_team_id', right_on='team_id', how='left')
nfl_df = nfl_df.rename(columns={'team_name':'passing_leader_team_name'}).drop(columns='team_id')

# # Merge for rushing leader team name
nfl_df = nfl_df.merge(team_df, left_on='rushing_leader_team_id', right_on='team_id', how='left')
nfl_df = nfl_df.rename(columns={'team_name':'rushing_leader_team_name'}).drop(columns='team_id')

# # Merge for receiving leader team name
nfl_df = nfl_df.merge(team_df, left_on='receiving_leader_team_id', right_on='team_id', how='left')
nfl_df = nfl_df.rename(columns={'team_name':'receiving_leader_team_name'}).drop(columns='team_id')

columns_to_reorder = ['id_x', 'name', 'date', 'season_year', 'type_of_season', 'week_number',
       'attendance', 'venue_id', 'venue_name', 'city', 
       'passing_leader_id', 'passing_leader_name', 'passing_leader_team_id', 'passing_leader_team_name', 'passing_leader_value', 
       'rushing_leader_id', 'rushing_leader_name', 'rushing_leader_team_id', 'rushing_leader_team_name', 'rushing_leader_value', 
       'receiving_leader_id', 'receiving_leader_name', 'receiving_leader_team_id', 'receiving_leader_team_name', 'receiving_leader_value', 
       'home_team_id', 'home_team_name', 'home_score', 
       'away_team_id', 'away_team_name', 'away_score' ]

columns_to_rename = {'id_x':'match_id'}

nfl_df = nfl_df[columns_to_reorder].rename(columns_to_rename)

nfl_df.to_parquet(path=r'etl/data/raw/nfl_df.parquet')