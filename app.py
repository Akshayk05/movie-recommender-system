from http.client import responses

import streamlit as st
import pickle
import pandas as pd
import requests
import time

# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommend_movies = []
    # recommend_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id  # assuming your DataFrame has 'movie_id' column
        recommend_movies.append(movies.iloc[i[0]].title)
        # recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies #recommend_movies_poster


movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
    'how would you like to be contacted',
    movies['title'].values)

if st.button('Recommend'):
    name=recommend(selected_movie_name)
    cols = st.columns(5)  # You can set 3 or 4 for tighter spacing
    for i in range(len(name)):
        with cols[i]:
            # st.image(posters[i], use_column_width=True)
            st.markdown(f"**{name[i]}**")