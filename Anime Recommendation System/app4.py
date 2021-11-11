from io import StringIO
import pickle
import streamlit as st
import requests
import pandas as pd
import pathlib
from pathlib import Path
import numpy as np


def get_similar_anime(anime):

    if anime not in pivort.index:
        return None, None

    else:
        sim_animes = similarity.sort_values(by=anime, ascending=False).index[1:]
        sim_score = similarity.sort_values(by=anime, ascending=False).loc[:, anime].tolist()[1:]

        return sim_animes, sim_score



#df = pd.read_csv("AnimeList.csv")
st.header('Anime Recommender System - User Rating')

animes = pickle.load(open('anime_itembased.pkl','rb'))
similarity = pickle.load(open('similarity_itembased.pkl','rb'))
pivort = pickle.load(open('pivot_itembased.pkl','rb'))

anime_list = animes['name'].values
selected_anime = st.selectbox("Type or select a anime from the dropdown",  anime_list)



if st.button('Show Recommendation'):
    animes, score = get_similar_anime(selected_anime)
    for x,y in zip(animes[:10], score[:5]):
        print("{} with similarity of {}".format(x, y))
        st.write(("{}".format(x)))



rate = st.selectbox("How many anime you like from this recommendation?",("0", "1", "2", "3", "4", "5"))
if st.button('Enter value'):
    ratevalue  = int(rate)
    
    reset = Path('reset4.txt').read_text()
    resetcount = int(reset)

    count = Path('count4.txt').read_text()
    countvalue  = int(count)

    if resetcount == 5:
        accuracy = (countvalue/25)*100
        st.write("Recommendation accuracy is " + str(accuracy) + "%")
        rate  = 0
        pathlib.Path('count4.txt').write_text(str(rate))
        a = 0
        pathlib.Path('reset4.txt').write_text(str(a))

    else:

        a = resetcount + 1
        rate = ratevalue + countvalue
        st.write(str(a) + ' round with ' + str(rate) + " correct anime recommendation")
        pathlib.Path('count4.txt').write_text(str(rate))
        pathlib.Path('reset4.txt').write_text(str(a))