#!/usr/bin/env python
# coding: utf-8

# ## Imports, API functions

# In[29]:


import sys
import twitter
import requests
import pandas as pd
import datetime as dt

from keys import keys
api = twitter.Api(**keys)


# In[2]:


URL_CAT_FACT = "https://catfact.ninja/fact"
URL_VELIB_STATUS = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json"
URL_VELIB_STATIONS = "https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_information.json"

def get_cat_fact():
    """Returns a random catfact as a string
    Example:
    get_cat_fact() 
    -> 'Approximately 24 cat skins can make a coat.'
    """
    url_base = URL_CAT_FACT
    params = {"max_length": 260}
    response = requests.get(url_base, params)
    return response.json()["fact"]

def get_velib_df():
    response = requests.get(URL_VELIB_STATUS)
    velib_df = (pd.DataFrame(response.json()["data"]["stations"])
                    .set_index("stationCode"))
    return velib_df

def get_stations_df():
    response = requests.get(URL_VELIB_STATIONS)
    stations_df = (pd.DataFrame(response.json()["data"]["stations"])
                   .set_index("station_id"))
    return stations_df


# ## Testing APIs

# In[3]:


#%%time
#cat_fact = get_cat_fact()
#print(cat_fact)


# In[4]:


#%%time
#velib_df = get_velib_df()
#velib_df.sample(2)


# In[5]:


#%%time
#stations_df = get_stations_df()
#stations_df.sample(2)


# ## Post functions

# In[17]:


def status_station(i):
    """
    global velib_df, stations_df are properly formatted pandas dataframes
    i is the station code (int)
    returns a string
    Example:
    status_station(12009)
    -> '🚲 Charenton - Diderot : 8 🟩 - 3 🟦 - 7 🅿️'
    """
    station = velib_df.loc[str(i),:] # row of the df
    station_id = station['station_id']
    nom_station = stations_df.loc[station_id,:]["name"]
    dispos = station['num_bikes_available']
    mecas = station['num_bikes_available_types'][0]['mechanical']
    elecs = station['num_bikes_available_types'][1]['ebike']
    parks = station['num_docks_available']
    return f"""🚲 {nom_station} :\n     {mecas} 🟩 - {elecs} 🟦 - {parks} 🅿️"""


# In[18]:


def post_message(user_id, home_stations_list, day_stations_list, morning = 'True'):
    """
    global api is an instance of twitter api
    user_id in Twitter's user id, int
    home_stations_list and day_stations_list are lists of int
    morning is a boolean
    tweets 
    """
    home_stations_txt = '\n'.join([status_station(i) for i in home_stations_list])
    day_stations_txt = '\n'.join([status_station(i) for i in day_stations_list])
    cat_fact_text = '😺 ' + get_cat_fact() + ' 😺'
    if morning:
        start_txt = """👋 Good morning!"""
        end_txt = '☀️ Have a splendid day ☀️'
    else:
        start_txt = """👋 How was your day?"""
        end_txt = '🌙 See you tomorrow 🌙'

    api.PostDirectMessage(start_txt, user_id = user_id)
    api.PostDirectMessage(home_stations_txt if morning 
                              else day_stations_txt, user_id = user_id)
    api.PostDirectMessage(cat_fact_text, user_id = user_id)
    api.PostDirectMessage(day_stations_txt if morning 
                              else home_stations_txt, user_id = user_id)
    api.PostDirectMessage(end_txt, user_id = user_id)


# ## Script

# In[19]:


velib_df = get_velib_df()
stations_df = get_stations_df()

etienne_id = 115890590
etienne_home_stations = [12008, 12009, 12106, 12011,]
etienne_day_stations = [3003, 11043, 11047, 3002]

peppe_id = 454228402
peppe_home_stations = [12009, 12106, 12011]
peppe_day_stations = [13055, 13050, 13016, 13054]

morning = dt.datetime.now().hour <= 12


# In[20]:


if sys.argv[1] == "etienne":
    post_message(etienne_id, etienne_home_stations, 
                     etienne_day_stations, morning = morning)
elif sys.argv[1] == "etienne": 
    post_message(peppe_id, peppe_home_stations, 
                     peppe_day_stations, morning = morning)
else: print(error)

