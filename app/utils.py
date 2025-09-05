import requests

API_KEY = "08ad638a6a535491cbba4b53d72bd552"   
BASE_URL = "https://api.themoviedb.org/3/search/movie"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"

def fetch_movie_details(movie_name):
    """
    Fetch poster, overview, rating, and release year from TMDB.
    Returns a dictionary with keys: poster, overview, rating, year
    """
    url = f"{BASE_URL}?api_key={API_KEY}&query={movie_name}"
    try:
        response = requests.get(url).json()
    except Exception as e:
        print("Request failed:", e)
        return None

    if response.get('results'):
        data = response['results'][0]
        poster_path = data.get('poster_path')
        poster_url = IMAGE_URL + poster_path if poster_path else "https://via.placeholder.com/300x450?text=No+Image"
        overview = data.get('overview', 'No description available')
        rating = data.get('vote_average', 'N/A')
        release_date = data.get('release_date', '')
        year = release_date.split('-')[0] if release_date else 'N/A'

        return {
            'poster': poster_url,
            'overview': overview,
            'rating': rating,
            'year': year
        }

    # fallback if no results
    return {
        'poster': "https://via.placeholder.com/300x450?text=No+Image",
        'overview': "No description available",
        'rating': "N/A",
        'year': "N/A"
    }