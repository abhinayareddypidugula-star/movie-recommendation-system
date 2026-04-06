import streamlit as st

# Page Config
st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬")

st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get recommendations")

# Movie Dataset (Manual List)
movies = [
    {
        "title": "Avatar",
        "genre": "Action Sci-Fi Adventure"
    },
    {
        "title": "Titanic",
        "genre": "Romance Drama"
    },
    {
        "title": "Avengers",
        "genre": "Action Superhero"
    },
    {
        "title": "Batman",
        "genre": "Action Crime"
    },
    {
        "title": "Inception",
        "genre": "Sci-Fi Thriller"
    },
    {
        "title": "Interstellar",
        "genre": "Sci-Fi Adventure"
    },
    {
        "title": "Joker",
        "genre": "Crime Drama"
    },
    {
        "title": "Iron Man",
        "genre": "Action Superhero"
    },
    {
        "title": "Doctor Strange",
        "genre": "Fantasy Action"
    },
    {
        "title": "The Dark Knight",
        "genre": "Action Crime"
    }
]

# Recommendation Function
def recommend(movie_name):
    
    selected_movie = None
    
    for movie in movies:
        if movie["title"] == movie_name:
            selected_movie = movie
            break
    
    if not selected_movie:
        return []
    
    selected_genre = selected_movie["genre"].split()
    
    recommendations = []
    
    for movie in movies:
        if movie["title"] != movie_name:
            movie_genre = movie["genre"].split()
            
            common = set(selected_genre) & set(movie_genre)
            
            if len(common) > 0:
                recommendations.append(movie["title"])
    
    return recommendations[:5]

# Dropdown
movie_names = [movie["title"] for movie in movies]

selected_movie = st.selectbox(
    "Choose a Movie",
    movie_names
)

# Button
if st.button("Recommend Movies"):
    
    results = recommend(selected_movie)
    
    st.subheader("Recommended Movies")
    
    if results:
        for movie in results:
            st.write("👉", movie)
    else:
        st.write("No Recommendations Found")