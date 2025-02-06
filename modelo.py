import pandas as pd

# Cargar datos
movies = pd.read_csv("ml-1m/movies.dat", sep="::", engine="python", names=["movieId", "title", "genres"], encoding="ISO-8859-1")
users = pd.read_csv("ml-1m/users.dat", sep="::", engine="python", names=["userId", "gender", "age", "occupation", "zipCode"], encoding="ISO-8859-1")

# Diccionarios de categorías
age_categories = {
    1: "Under 18", 18: "18-24", 25: "25-34",
    35: "35-44", 45: "45-49", 50: "50-55", 56: "56+"
}

occupation_categories = {
    0: "Other", 1: "Academic/Educator", 2: "Artist", 3: "Clerical/Admin",
    4: "College/Grad Student", 5: "Customer Service", 6: "Doctor/Health Care",
    7: "Executive/Managerial", 8: "Farmer", 9: "Homemaker", 10: "K-12 Student",
    11: "Lawyer", 12: "Programmer", 13: "Retired", 14: "Sales/Marketing",
    15: "Scientist", 16: "Self-Employed", 17: "Technician/Engineer",
    18: "Tradesman/Craftsman", 19: "Unemployed", 20: "Writer"
}

# Función de recomendación por género
def recommend_by_genre(genre):
    filtered_movies = movies[movies['genres'].str.contains(genre, na=False)]
    return filtered_movies[['title']].head(5).to_dict(orient="records")

# Función de recomendación por usuario
def recommend_by_user(age_category, gender, occupation_category):
    try:
        age_numeric = next((k for k, v in age_categories.items() if v == age_category), None)
        occupation_numeric = next((k for k, v in occupation_categories.items() if v == occupation_category), None)

        if age_numeric is None or occupation_numeric is None:
            return [{"title": "Datos no válidos"}]

        filtered_users = users[
            (users["age"] == age_numeric) & 
            (users["gender"] == gender) & 
            (users["occupation"] == occupation_numeric)
        ]
        
        if not filtered_users.empty:
            return movies.sample(5)[['title']].to_dict(orient="records")
        else:
            return [{"title": "No hay recomendaciones disponibles"}]
    except Exception as e:
        return [{"title": f"Error: {str(e)}"}]
