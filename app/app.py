import streamlit as st
from recommender import recommend_movies
from utils import fetch_movie_details

st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommendation System")

movie_name = st.text_input("Enter a movie you like:")

if st.button("Recommend"):
    recommendations = recommend_movies(movie_name, top_n=10)
    
    if recommendations:
        for rec in recommendations:
            details = fetch_movie_details(rec)
            cols = st.columns([1, 3])
            with cols[0]:
                st.image(details['poster'], use_container_width=150)
            with cols[1]:
                st.subheader(f"{rec} ({details['year']})")
                st.write(f"**Rating:** ⭐ {round(details['rating'], 1)}")
                st.write(f"**Description:** {details['overview']}")
    else:
        st.warning("Movie not found in database.")
