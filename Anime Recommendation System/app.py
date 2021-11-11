from io import StringIO
import pickle
import streamlit as st
import requests
import pandas as pd
import pathlib
from pathlib import Path
import numpy as np


def recommend(anime):
    index =animes[animes['title'] == anime].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_anime_names = []
    for i in distances[1:6]:
        recommended_anime_names.append(animes.iloc[i[0]].title)

    return recommended_anime_names

#df = pd.read_csv("AnimeList.csv")
st.header('Anime Recommender System - Genres')
animes = pickle.load(open('animeGenre.pkl','rb'))
similarity = pickle.load(open('similarityGenre.pkl','rb'))

anime_list = animes['title'].values
selected_anime = st.selectbox("Type or select a anime from the dropdown",  anime_list)



if st.button('Show Recommendation'):
    recommended_anime_names = recommend(selected_anime) 
    for i in recommended_anime_names:
        st.write(i)



rate = st.selectbox("How many anime you like from this recommendation?",("0", "1", "2", "3", "4", "5"))
if st.button('Enter value'):
    ratevalue  = int(rate)
    
    reset = Path('reset.txt').read_text()
    resetcount = int(reset)

    count = Path('count.txt').read_text()
    countvalue  = int(count)

    if resetcount == 5:
        accuracy = (countvalue/25)*100
        st.write("Recommendation accuracy is " + str(accuracy) + "%")
        rate  = 0
        pathlib.Path('count.txt').write_text(str(rate))
        a = 0
        pathlib.Path('reset.txt').write_text(str(a))

    else:

        a = resetcount + 1
        rate = ratevalue + countvalue
        st.write(str(a) + ' round with ' + str(rate) + " correct anime recommendation")
        pathlib.Path('count.txt').write_text(str(rate))
        pathlib.Path('reset.txt').write_text(str(a))