import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

'''
data_for_map = df.rename(index = str, columns = {
'Area_name': "borough",
'Happiness_score_2011-14_(out_of_10)': "happiness",
'Anxiety_score_2011-14_(out_of_10)': "anxiety",
'Population_density_(per_hectare)_2017': "pop_density_per_hectare",
'Mortality_rate_from_causes_considered_preventable_2012/14': "mortality"})
'''

#fPath = 'Data/USA/ne_50m_admin_1_states_provinces.shp'
fPath = 'Data/counties/tl_2017_us_county.shp'
df = pd.read_csv('Data/1bed_rent_data.csv', header = 0)
df = df[['RegionName', '2019-11']]

map_df = gpd.read_file(fPath)
map_df = map_df[~map_df['adm1_code'].str.contains('AUS')]
map_df = map_df[~map_df['adm1_code'].str.contains('BRA')]

map_df = map_df[ ['iso_3166_2', 'name', 'latitude', 'longitude', 'geometry'] ]

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

merged = map_df.set_index('name').join(df.set_index('RegionName'))

VOI = '2019-11'
fig, ax = plt.subplots(1, figsize = (10, 6) )
merged.plot(column = VOI, cmap = 'Blues', ax = ax)
plt.show()
#[print(i) for i in map_df.columns.tolist()]

#map_df.plot()
#plt.show()
