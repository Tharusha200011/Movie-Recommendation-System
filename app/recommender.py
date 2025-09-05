import pandas as pd
import pickle
import difflib

movies_data = pd.read_csv("data/movies_clean.csv")
similarity = pickle.load(open("models/similarity.pkl", "rb"))

def recommend_movies(movie_name, top_n=10):
    
    list_of_all_titles = movies_data['title'].tolist()
    
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    
    if not find_close_match:
        return []
    
    close_match = find_close_match[0]
    
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    
    recommendations = []
    i = 1
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies_data[movies_data.index==index]['title'].values[0]
        if i <= top_n:
            recommendations.append(title_from_index)
            i += 1
    return recommendations
