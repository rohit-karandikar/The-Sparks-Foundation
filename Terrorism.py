import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from itertools import chain
df = pd.read_csv("globalterrorismdb_0718dist.csv",low_memory=False)
def draw_map(m, scale=0.2):    
    m.shadedrelief(scale=scale)
    lats = m.drawparallels(np.linspace(-90, 90, 13))
    lons = m.drawmeridians(np.linspace(-180, 180, 13))   
    lat_lines = chain(*(tup[1][0] for tup in lats.items()))
    lon_lines = chain(*(tup[1][0] for tup in lons.items()))
    all_lines = chain(lat_lines, lon_lines)       
    for line in all_lines:
        line.set(linestyle='-', alpha=0.3, color='w')
print(df.head())
print(df.describe())

city = df["city"]
unique = list(dict.fromkeys(city))
count = [0] * len(unique)
count_city = pd.DataFrame({'City':unique, 'count':count})
for i in range(len(df)):
    index = unique.index(city[i])
    count_city.iloc[index,1] = count_city.iloc[index,1] + 1
count_city = count_city.drop([2])
count_city = count_city.sort_values(by='count',ascending=False)
print(count_city.head())

attack_type = df["attacktype1_txt"] + df["attacktype2_txt"] + df["attacktype3_txt"] 
unique = list(dict.fromkeys(attack_type))
count = [0] * len(unique)
count_attack_type = pd.DataFrame({'Attack_type':unique, 'count':count})
for i in range(len(df)):
    index = unique.index(attack_type[i])
    count_attack_type.iloc[index,1] = count_attack_type.iloc[index,1] + 1
count_attack_type = count_attack_type.sort_values(by='count',ascending=False)
count_attack_type = count_attack_type.drop([0])
fig = plt.figure()
plt.bar(count_attack_type["Attack_type"].astype('|S'),count_attack_type["count"])
plt.show()

attack_group = df["gname"] + df["gname2"] + df["gname3"] 
unique = list(dict.fromkeys(attack_group))
count = [0] * len(unique)
count_attack_group = pd.DataFrame({'Attack_Group':unique, 'count':count})
for i in range(len(df)):
    index = unique.index(attack_group[i])
    count_attack_group.iloc[index,1] = count_attack_group.iloc[index,1] + 1
count_attack_group = count_attack_group.sort_values(by='count',ascending=False)
count_attack_group = count_attack_group.drop([0])
fig = plt.figure()
plt.barh(count_attack_group["Attack_Group"].astype('|S80'),count_attack_group["count"])
plt.show()

fig = plt.figure(figsize=(8, 6), edgecolor='w')
m = Basemap(projection='cyl', resolution=None,
            llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, )
from itertools import chain
draw_map(m)
m.scatter(df["longitude"],df["latitude"],s=0.5)
plt.show()