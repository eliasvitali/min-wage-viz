import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from math import floor, ceil

states = [f'{i:0>2}' for i in range(1, 57)]
omits  = [f'{i:0>2}' for i in [3, 7, 14 ,43, 52]]

for state in omits:
    states.remove(state)

counties_path = 'Data/counties/UScounties.shp'
minwage_path  = 'Data/minwagedata.csv'
rentdata_path = 'Data/County_MedianRentalPrice_1Bedroom.csv'

map_data  = gpd.read_file(counties_path)
rent_data = pd.read_csv(rentdata_path)
wage_data = pd.read_csv(minwage_path)

