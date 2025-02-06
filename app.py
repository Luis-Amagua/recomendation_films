from flask import Flask, render_template, request
from modelo import recommend_by_genre, recommend_by_user, age_categories, occupation_categories

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    if request.method == "POST":
        if "genre" in request.form:
            genre = request.form["genre"]
            recommendations = recommend_by_genre(genre)
        elif "age" in request.form and "gender" in request.form and "occupation" in request.form:
            try:
                age_category_key = int(request.form["age"])
                gender = request.form["gender"]
                occupation_category_key = int(request.form["occupation"])
                
                # Obtener los valores correctos
                age_category = age_categories.get(age_category_key, "Unknown")
                occupation_category = occupation_categories.get(occupation_category_key, "Unknown")
                
                recommendations = recommend_by_user(age_category, gender, occupation_category)
            except ValueError:
                recommendations = [{"title": "Error en los datos ingresados"}]

    return render_template("index.html", recommendations=recommendations, 
                           age_categories=age_categories, 
                           occupation_categories=occupation_categories)

if __name__ == "__main__":
    app.run(debug=True)
