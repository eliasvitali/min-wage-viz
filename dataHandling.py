import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

'''
fPath = 'Data/ESRI/London_Borough_Excluding_MHW.shp'
map_df = gpd.read_file(fPath)


df = pd.read_csv('Data/london-borough-profiles.csv', header = 0)
df = df[['Area_name','Happiness_score_2011-14_(out_of_10)', 'Anxiety_score_2011-14_(out_of_10)', 'Population_density_(per_hectare)_2017', 'Mortality_rate_from_causes_considered_preventable_2012/14']]

data_for_map = df.rename(index = str, columns = {
'Area_name': "borough",
'Happiness_score_2011-14_(out_of_10)': "happiness",
'Anxiety_score_2011-14_(out_of_10)': "anxiety",
'Population_density_(per_hectare)_2017': "pop_density_per_hectare",
'Mortality_rate_from_causes_considered_preventable_2012/14': "mortality"})

merged = map_df.set_index('NAME').join(data_for_map.set_index('borough'))

VOI = 'pop_density_per_hectare'
vMin, vMax = 120, 220

fig, ax = plt.subplots(1, figsize = (10, 6) )
merged.plot(column = VOI, cmap = 'Blues', ax = ax)
plt.show()
'''

fPath = 'Data/USA/ne_50m_admin_1_states_provinces.shp'

map_df = gpd.read_file(fPath)
map_df = map_df[~map_df['adm1_code'].str.contains('AUS')]
map_df = map_df[~map_df['adm1_code'].str.contains('BRA')]

pd.set_option('display.max_rows', None)
print(map_df['name_en'])

map_df.plot()

#print(map_df)
#plt.show()
