
# coding: utf-8

# In[ ]:

# not latlong
golf = pd.read_csv("Golf_Courses.csv")
golf.head()

#no latlong
#not needed
cons_grant = pd.read_csv("Hamilton_Heritage_Conservation_Grant_Program_Recipients.csv")
cons_grant.head()

#no latlong
#not needed
prop_grant = pd.read_csv("Hamilton_Heritage_Property_Grant_Program_Recipients.csv")
prop_grant.head()

#no location
heritage_props = pd.read_csv("Heritage_Properties.csv")
heritage_props.head()

#no loc
licensed_public_halls = pd.read_csv("Licensed_Public_Halls.csv")
licensed_public_halls.head()

#no loc
live_music = pd.read_csv("Live_Music_Venues.csv")
live_music.head()

#latlong not in columns
urban_design = pd.read_csv("Urban_Design_Architecture_Awards_Recipients.csv")
urban_design.head()


# In[ ]:

##print("jhex")
#time.sleep(5)


# In[ ]:

a = 5
b = 4
#[a, b, 2] = [3, 5, 2]


# In[ ]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
#sns 


# In[ ]:

df = pd.read_csv("School_Crossing_Guard_Locations.csv")
df.columns


# In[ ]:

a = df[:]


# In[ ]:

a = "b"
def


# In[ ]:

import requests
import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
#sns 
#df = pd.read_csv(io.StringIO(file.text))
#print(df.head())


# In[ ]:

import requests
import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
#sns 
#df = pd.read_csv(io.StringIO(file.text))
#print(df.head())


arenas_link = requests.get('https://opendata.arcgis.com/datasets/2d543c2f199c4f3bb52c5edc1c389c3f_3.csv')
arenas = pd.read_csv(io.StringIO(arenas_link.text))

beaches_link = requests.get('https://opendata.arcgis.com/datasets/223fbe172aa5490986ba0899e45939f8_5.csv')
beaches = pd.read_csv(io.StringIO(beaches_link.text))

campgrounds_link = requests.get('https://opendata.arcgis.com/datasets/90e0023d8f2c481e85037869bfa6cb50_9.csv')
campgrounds = pd.read_csv(io.StringIO(campgrounds_link.text))

city_waterfalls_link = requests.get('https://opendata.arcgis.com/datasets/51c6d946f91249828bc1c594ce1b27d1_16.csv')
city_waterfalls = pd.read_csv(io.StringIO(city_waterfalls_link.text))

educational_institutions_link = requests.get('https://opendata.arcgis.com/datasets/cccae6f029334927856da6e20a50561f_19.csv')
educational_institutions = pd.read_csv(io.StringIO(educational_institutions_link.text))

libraries_link = requests.get('https://opendata.arcgis.com/datasets/67a54ea25d944cf7b66750ba57da822c_1.csv')
libraries = pd.read_csv(io.StringIO(libraries_link.text))

museums_and_galleries_link = requests.get('https://opendata.arcgis.com/datasets/6728810fb847489985d4b735502205a0_2.csv')
museums_and_galleries = pd.read_csv(io.StringIO(museums_and_galleries_link.text))

park_amenities_link = requests.get('https://opendata.arcgis.com/datasets/332d57db20494adaaa8ab7cad3ea7726_4.csv')
park_amenities = pd.read_csv(io.StringIO(park_amenities_link.text))

place_of_worship_link = requests.get('https://opendata.arcgis.com/datasets/a4c3f339c6a440b888db7589431a3c57_7.csv')
places_of_worship = pd.read_csv(io.StringIO(place_of_worship_link.text))

public_art_and_monuments_link = requests.get('https://opendata.arcgis.com/datasets/a0bcdf73598c424d9e7ef72861dca71c_10.csv')
public_art_and_monuments = pd.read_csv(io.StringIO(public_art_and_monuments_link.text))

recreation_and_community_centres_link = requests.get('https://opendata.arcgis.com/datasets/272667665de646768db14e9fa1676405_11.csv')
recreation_and_community_centres = pd.read_csv(io.StringIO(recreation_and_community_centres_link.text))

sobi_hubs_link = requests.get('https://opendata.arcgis.com/datasets/b5fb1c2cbccc4513ad4cac3671905ccc_18.csv')
sobi_hubs = pd.read_csv(io.StringIO(sobi_hubs_link.text))

spray_pads_link = requests.get('https://opendata.arcgis.com/datasets/d99a1dbd4f3f47b6ac3f19b2761bdf0c_15.csv')
spray_pads = pd.read_csv(io.StringIO(spray_pads_link.text))

tourism_points_of_interest_link = requests.get('https://opendata.arcgis.com/datasets/e09cca59a8584cc28e7879bd6b0ce7f4_0.csv')
tourism_points_of_interest = pd.read_csv(io.StringIO(tourism_points_of_interest_link.text))


'''
for i in range(len(arenas)):
    arenas['ADDRESS'][i] = ('Address: ' + arenas['ADDRESS'][i] + '\nCommunity: ' + arenas['COMMUNITY'][i] + '\nPhone: ' + arenas['PHONE'][i])

arenas.rename(columns={'ADDRESS':'DESCRIPTION'}, inplace=True)

arenas = arenas[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]



beaches.rename(columns={'WATER_SOURCE':'DESCRIPTION'}, inplace=True)

beaches = beaches[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]

print(beaches.head())



for i in range(len(city_waterfalls)):
    city_waterfalls['CLUSTER_AREA'][i] = ('Area: ' + city_waterfalls['CLUSTER_AREA'][i] + '\nAlternate Name: ' + str(city_waterfalls['ALTERNATE_NAME'][i]) + '\nHeight: ' + str(city_waterfalls['HEIGHT_IN_M'][i]) + 'm' + '\nWidth: ' + str(city_waterfalls['WIDTH_IN_M'][i]) + 'm')

city_waterfalls.rename(columns={'CLUSTER_AREA':'DESCRIPTION'}, inplace=True)

city_waterfalls = city_waterfalls[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]
print(city_waterfalls.head())



for i in range(len(educational_institutions)):
    educational_institutions['ADDRESS'][i] = ('Address: ' + educational_institutions['ADDRESS'][i] + '\nCommunity: ' + educational_institutions['COMMUNITY'][i] + '\nCategory: ' + educational_institutions['CATEGORY'][i] + '\nSchool Board: ' + str(educational_institutions['SCHOOL_BOARD'][i]))

educational_institutions.rename(columns={'ADDRESS':'DESCRIPTION'}, inplace=True)

educational_institutions = educational_institutions[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]
print(educational_institutions.head())



for i in range(len(libraries)):
    libraries['HOLDINGS'][i] = ('Holdings: ' + str(libraries['HOLDINGS'][i]) + '\nCirculation: ' + str(libraries['CIRCULATION'][i]))

libraries.rename(columns={'HOLDINGS':'DESCRIPTION'}, inplace=True)

libraries = libraries[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]

print(libraries.head())



for i in range(len(campgrounds)):
    campgrounds['LOCATION'][i] = ('Address: ' + campgrounds['LOCATION'][i] + '\nURL: ' + campgrounds['URL'][i])

campgrounds.rename(columns={'LOCATION':'DESCRIPTION'}, inplace=True)

campgrounds = campgrounds[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]

print(campgrounds.head())



for i in range(len(museums_and_galleries)):
    museums_and_galleries['OBJECTID'][i] = ('N/A')

museums_and_galleries.rename(columns={'OBJECTID':'DESCRIPTION'}, inplace=True)

museums_and_galleries = museums_and_galleries[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]
print(museums_and_galleries.head())



for i in range(len(park_amenities)):
    park_amenities['TYPE'][i] = (str(park_amenities['TYPE'][i]) + 'ball')
    park_amenities['REC_AREA'][i] = ('Recreational Area: ' + str(park_amenities['REC_AREA'][i]) + 'Ownership: ' + str(park_amenities['OWNERSHIP'][i]))

park_amenities.rename(columns={'TYPE':'NAME'}, inplace=True)
park_amenities.rename(columns={'REC_AREA':'DESCRIPTION'}, inplace=True)

park_amenities = park_amenities[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]
print(park_amenities.head())



for i in range(len(places_of_worship)):
    places_of_worship['DENOMINATION'][i] = ('Denomination: ' + places_of_worship['DENOMINATION'][i] + '\nAddress: ' + places_of_worship['ADDRESS'][i] + '\nCommunity: ' + places_of_worship['COMMUNITY'][i])

places_of_worship.rename(columns={'DENOMINATION':'DESCRIPTION'}, inplace=True)

places_of_worship = places_of_worship[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]
print(places_of_worship.head())
'''
print(2)



# In[ ]:




# In[ ]:

df1= pd.read_csv("Arenas.csv")
df2= pd.read_csv("Beaches.csv")
df3= pd.read_csv("Campgrounds.csv")
df4= pd.read_csv("City_Waterfalls.csv")
df5= pd.read_csv("Educational_Institutions.csv")
df6= pd.read_csv("Libraries.csv")
df7= pd.read_csv("Museums_and_Galleries.csv")
df8= pd.read_csv("Park_Amenities.csv")
df9= pd.read_csv("Places_of_Worship.csv")
df10= pd.read_csv("Public_Art_and_Monuments.csv")
df11= pd.read_csv("Recreation_and_Community_Centres.csv")
df12= pd.read_csv("SoBi_Hubs.csv")
df13= pd.read_csv("Spray_Pads.csv")
df14= pd.read_csv("Tourism_Points_of_Interest.csv")


# In[ ]:

for i in range(len(arenas)):
    arenas['ADDRESS'][i] = ('Address: ' + arenas['ADDRESS'][i] + '\nCommunity: ' + arenas['COMMUNITY'][i] + '\nPhone: ' + arenas['PHONE'][i])

arenas.rename(columns={'ADDRESS':'DESCRIPTION'}, inplace=True)

arenas = arenas[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]


# In[ ]:



beaches.rename(columns={'WATER_SOURCE':'DESCRIPTION'}, inplace=True)

beaches = beaches[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]


# In[ ]:


for i in range(len(campgrounds)):
    campgrounds['LOCATION'][i] = ('Address: ' + campgrounds['LOCATION'][i] + '\nURL: ' + campgrounds['URL'][i])

campgrounds.rename(columns={'LOCATION':'DESCRIPTION'}, inplace=True)

campgrounds = campgrounds[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]


# In[ ]:

for i in range(len(city_waterfalls)):
    city_waterfalls['CLUSTER_AREA'][i] = ('Area: ' + city_waterfalls['CLUSTER_AREA'][i] + '\nAlternate Name: ' + str(city_waterfalls['ALTERNATE_NAME'][i]) + '\nHeight: ' + str(city_waterfalls['HEIGHT_IN_M'][i]) + 'm' + '\nWidth: ' + str(city_waterfalls['WIDTH_IN_M'][i]) + 'm')

city_waterfalls.rename(columns={'CLUSTER_AREA':'DESCRIPTION'}, inplace=True)

city_waterfalls = city_waterfalls[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]


# In[ ]:



for i in range(len(educational_institutions)):
    educational_institutions['ADDRESS'][i] = ('Address: ' + educational_institutions['ADDRESS'][i] + '\nCommunity: ' + educational_institutions['COMMUNITY'][i] + '\nCategory: ' + educational_institutions['CATEGORY'][i] + '\nSchool Board: ' + str(educational_institutions['SCHOOL_BOARD'][i]))

educational_institutions.rename(columns={'ADDRESS':'DESCRIPTION'}, inplace=True)

educational_institutions = educational_institutions[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]


# In[ ]:


for i in range(len(libraries)):
    libraries['HOLDINGS'][i] = ('Holdings: ' + str(libraries['HOLDINGS'][i]) + '\nCirculation: ' + str(libraries['CIRCULATION'][i]))

libraries.rename(columns={'HOLDINGS':'DESCRIPTION'}, inplace=True)

libraries = libraries[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]


# In[ ]:


for i in range(len(museums_and_galleries)):
    museums_and_galleries['OBJECTID'][i] = ('N/A')

museums_and_galleries.rename(columns={'OBJECTID':'DESCRIPTION'}, inplace=True)

museums_and_galleries = museums_and_galleries[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]


# In[ ]:


for i in range(len(park_amenities)):
    park_amenities['TYPE'][i] = (str(park_amenities['TYPE'][i]) + 'ball')
    park_amenities['REC_AREA'][i] = ('Recreational Area: ' + str(park_amenities['REC_AREA'][i]) + 'Ownership: ' + str(park_amenities['OWNERSHIP'][i]))

park_amenities.rename(columns={'TYPE':'NAME'}, inplace=True)
park_amenities.rename(columns={'REC_AREA':'DESCRIPTION'}, inplace=True)

park_amenities = park_amenities[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]


# In[ ]:


for i in range(len(places_of_worship)):
    places_of_worship['DENOMINATION'][i] = ('Denomination: ' + places_of_worship['DENOMINATION'][i] + '\nAddress: ' + places_of_worship['ADDRESS'][i] + '\nCommunity: ' + places_of_worship['COMMUNITY'][i])

places_of_worship.rename(columns={'DENOMINATION':'DESCRIPTION'}, inplace=True)

places_of_worship = places_of_worship[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]


# In[ ]:


for i in range(len(public_art_and_monuments)):
    public_art_and_monuments['DESCRIPTION'][i] = ('Address: ' + public_art_and_monuments['STREET'][i] + '\nDescription: ' + public_art_and_monuments['DESCRIPTION'][i])

public_art_and_monuments.rename(columns={'ARTWORK_TITLE':'NAME'}, inplace=True)

public_art_and_monuments = public_art_and_monuments[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]


# In[ ]:


for i in range(len(recreation_and_community_centres)):
    recreation_and_community_centres['OBJECTID'][i] = ('N/A')

recreation_and_community_centres.rename(columns={'OBJECTID':'DESCRIPTION'}, inplace=True)

recreation_and_community_centres = recreation_and_community_centres[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]


# In[ ]:


for i in range(len(sobi_hubs)):
    sobi_hubs['DESCRIPTION'][i] = ('Address: ' + sobi_hubs['ADDRESS'][i] + '\nDescription' + str(sobi_hubs['DESCRIPTION'][i]))

sobi_hubs = sobi_hubs[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]


# In[ ]:


for i in range(len(spray_pads)):
    spray_pads['ADDRESS'][i] = ('Address: ' + spray_pads['ADDRESS'][i] + '\nOwner: ' + spray_pads['OWNER'][i] + '\nPhone: ' + spray_pads['PHONE'][i])

spray_pads.rename(columns={'ADDRESS':'DESCRIPTION'}, inplace=True)

spray_pads = spray_pads[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]


# In[ ]:


for i in range(len(tourism_points_of_interest)):
    tourism_points_of_interest['DESCRIPTION'][i] = ('Address: ' + str(tourism_points_of_interest['ADDRESS'][i]) + '\nDescription: ' + str(tourism_points_of_interest['DESCRIPTION'][i]) + '\nPhone: ' + str(tourism_points_of_interest['PHONE'][i]) + '\nEmail: ' + str(tourism_points_of_interest['EMAIL'][i]) + '\nWebsite: ' + str(tourism_points_of_interest['URL'][i]))

tourism_points_of_interest.rename(columns={'TITLE':'NAME'}, inplace=True)

tourism_points_of_interest = tourism_points_of_interest[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]


# In[ ]:

alldata = arenas
alldata = alldata.append(beaches)
print(len(alldata))
alldata.to_csv("ALL_DATA.csv")
alldata = alldata.append(campgrounds)
print(len(alldata))
alldata = alldata.append(city_waterfalls)
print(len(alldata))
alldata = alldata.append(educational_institutions)
print(len(alldata))
alldata = alldata.append(libraries)
print(len(alldata))
alldata = alldata.append(museums_and_galleries)
print(len(alldata))
alldata = alldata.append(park_amenities)
print(len(alldata))
alldata = alldata.append(places_of_worship)
print(len(alldata))
alldata = alldata.append(public_art_and_monuments)
print(len(alldata))
alldata = alldata.append(recreation_and_community_centres)
print(len(alldata))
alldata = alldata.append(sobi_hubs)
print(len(alldata))
alldata = alldata.append(spray_pads)
print(len(alldata))
alldata = alldata.append(tourism_points_of_interest)
print(len(alldata))
print(4 * 5)
alldata.to_csv("ALL_DATA2.csv")




# In[ ]:

events = pd.read_csv("todays_events_reformatted.csv")
events.rename(columns={'latitude':'LATITUDE','longitude':'LONGITUDE','name':'NAME','description':'DESCRIPTION'}, inplace=True)
events = events[['LATITUDE','LONGITUDE','NAME','DESCRIPTION']]


# In[ ]:

alldata = alldata.append(events)


# In[ ]:

usrlat = 43.269
usrlong = -79.884

inp = alldata[:1]
results = pd.DataFrame(inp)

hyp = 0
#sum = 0
for index, row in alldata.iterrows():
    hyp = ((usrlat - row["LATITUDE"]) ** 2 + (usrlong - row["LONGITUDE"]) ** 2) ** 0.5
    if (hyp <= 0.01):
        results = results.append(row)
        
#for index, row in arenas.iterrows():
 #   print(type(row['LATITUDE']))
results = results[1:]
results.to_csv("RESULTS.csv")

