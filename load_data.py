#!/usr/bin/env python3
"""
Standalone data loading script to avoid notebook patching issues
"""

import pandas as pd
import geopandas as gpd
import pickle
from pathlib import Path

SRC_PATH = Path("/Users/yishinn/Documents/GitHub/airbnb_nyc/src")

print("Loading datasets...")

airbnb_nyc_df = pd.read_csv(SRC_PATH / 'AB_NYC_2019.csv')
nypd_shooting_df = pd.read_csv(SRC_PATH / 'NYPD_Shooting_Incident_Data__Historic_.csv')
ny_tree_census_df = pd.read_csv(SRC_PATH / 'new_york_tree_census_2015.csv')
total_population_df = pd.read_csv(SRC_PATH / 'Total Population.csv', header=4)

try:
    arrest_data_df = pd.read_csv(SRC_PATH / 'NYPD_Arrests_Data__Historic_.csv')
except FileNotFoundError:
    arrest_data_df = pd.read_csv(SRC_PATH / 'NYPD_Arrests_Data__Historic_ (1).csv')

nta_pop_df = pd.read_csv(SRC_PATH / 'New_York_City_Population_By_Neighborhood_Tabulation_Areas.csv')
nyc_gdf = gpd.read_file(SRC_PATH / 'nycgeo.json')

# Save all datasets to pickle files
output_dir = Path("/Users/yishinn/Documents/GitHub/airbnb_nyc")

pd.to_pickle(airbnb_nyc_df, output_dir / 'airbnb_nyc_df.pkl')
pd.to_pickle(nypd_shooting_df, output_dir / 'nypd_shooting_df.pkl')
pd.to_pickle(ny_tree_census_df, output_dir / 'ny_tree_census_df.pkl')
pd.to_pickle(total_population_df, output_dir / 'total_population_df.pkl')
pd.to_pickle(arrest_data_df, output_dir / 'arrest_data_df.pkl')
pd.to_pickle(nta_pop_df, output_dir / 'nta_pop_df.pkl')
pd.to_pickle(nyc_gdf, output_dir / 'nyc_gdf.pkl')

print("✅ All datasets loaded and saved!")
print(f"  Airbnb NYC: {airbnb_nyc_df.shape}")
print(f"  NYPD Shooting: {nypd_shooting_df.shape}")
print(f"  NY Tree Census: {ny_tree_census_df.shape}")
print(f"  Total Population: {total_population_df.shape}")
print(f"  Arrest Data: {arrest_data_df.shape}")
print(f"  NTA Population: {nta_pop_df.shape}")
print(f"  NYC Geo: {nyc_gdf.shape}")
