import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from math import floor, ceil

#List of states FIPS codes
states = [f'{i:0>2}' for i in range(1, 57)]
omits  = [f'{i:0>2}' for i in [3, 7, 14 ,43, 52]]

#Omit Territories
for state in omits:
    states.remove(state)

#Load in Data
counties_path = 'Data/counties/UScounties.shp'
minwage_path  = 'Data/minwagedata.csv'
rentdata_path = 'Data/County_MedianRentalPrice_1Bedroom.csv'

map_data  = gpd.read_file(counties_path)
rent_data = pd.read_csv(rentdata_path)
wage_data = pd.read_csv(minwage_path)

#Cut and reshape Data
rent_data['StateCodeFIPS'] = rent_data['StateCodeFIPS'].astype(str)
rent_data['MunicipalCodeFIPS'] = rent_data['MunicipalCodeFIPS'].astype(str)
rent_data['StateCodeFIPS'] = rent_data['StateCodeFIPS'].apply('{0:0>2}'.format)
rent_data['MunicipalCodeFIPS'] = rent_data['MunicipalCodeFIPS'].apply('{0:0>3}'.format)
rent_data['FIPS'] = rent_data['StateCodeFIPS'].map(str) + rent_data['MunicipalCodeFIPS']
rent_data = rent_data[['RegionName', 'StateCodeFIPS', 'FIPS', '2019-12']]
wage_data['FIPS'] = wage_data['FIPS'].apply('{0:0>2}'.format)

rent_data = rent_data.rename(index = str, columns = {'StateCodeFIPS': 'STATE_FIPS', '2019-12': 'RENT'})
wage_data = wage_data.rename(index = str, columns = {'FIPS': 'STATE_FIPS'})

#Merge Dataframes

merged = map_data.merge(rent_data, on = 'FIPS')
del merged['STATE_FIPS_y']
merged = merged.rename(index = str, columns = {'STATE_FIPS_x': 'STATE_FIPS'})
merged = merged.merge(wage_data, on = 'STATE_FIPS')
del merged['statename']
del merged['RegionName']
merged = merged.rename(index = str, columns = {'minwage': 'MIN_WAGE'})
