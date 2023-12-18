from flask import Flask, jsonify
import pandas as pd
from sqlalchemy import create_engine
import ast
import mysql.connector
 
# app = Flask(__name__)
 
 
# config = {
#     'user': 'root',
#     'password': 'francy',
#     'host': 'localhost',
#     'database' : "fil_rouge2"
# }
 
# # Établissez la connexion
# connexion = mysql.connector.connect(**config)
 
# # Créez un objet de curseur pour exécuter des commandes SQL
# curseur = connexion.cursor()

# # @app.route('/')
# # def home():
# #     return "hello"
 
# @app.route('/api/<int:year>', methods=['GET'])
# def get_data(year):
#     query = "SELECT title FROM movies WHERE year = %s;"
#     curseur.execute(query, (year,))
#     results = curseur.fetchall()
#     title_list = [result[0] for result in results]
#     return jsonify({'titles': title_list})


# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:francy@localhost/fil_rouge2'
# db = SQLAlchemy(app)

# class Movie(db.Model):
#     __tablename__ = 'movies'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255))
#     year = db.Column(db.Integer)
#     plot = db.Column(db.Text)
#     gross_earning = db.Column(db.Float)

# # Assurez-vous de créer les tables avant de lancer l'application
# db.create_all()

# @app.route('/api/<int:movie_id>', methods=['GET'])
# def get_movie_info(movie_id):
#     movie = Movie.query.get(movie_id)

#     if movie:
#         movie_info = {
#             'id': movie.id,
#             'title': movie.title,
#             'year': movie.year,
#             'plot': movie.plot,
#             'gross_earning': movie.gross_earning
#         }
#         return jsonify(movie_info)
#     else:
#         return jsonify({'error': 'Film non trouvé'}), 404

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:francy@localhost/fil_rouge2'
# db = SQLAlchemy(app)

# # Créez le contexte de l'application
# with app.app_context():
#     # Assurez-vous de créer les tables avant de lancer l'application
#     db.create_all()

#     # @app.route('/')
#     # def home():
#     #     return "Hello toi"

#     @app.route('/api/<int:movie_id>', methods=['GET'])
#     def get_movie_year(movie_id):
#         movie = Movie.query.get(movie_id)

#         if movie:
#             return jsonify({'title': movie.title, 'year': movie.year})
#         else:
#             return jsonify({'error': 'Film non trouvé'}), 404

#     if __name__ == '__main__':
#         app.run(debug=True)



from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Configuration de la base de données
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'francy',
    'database': 'fil_rouge2'
}

# Créez une connexion à la base de données
conn = mysql.connector.connect(**db_config)

# Créez un curseur
cursor = conn.cursor(dictionary=True)


@app.route('/')
def home():
    return "Hello toi"

@app.route('/api/<int:year>', methods=['GET'])
def get_movies_by_year(year):
    # Définissez la requête SQL pour récupérer les films par année
    query = f"SELECT id, title, plot, gross_earning FROM movies WHERE year = {year}"
    
    # Exécutez la requête
    cursor.execute(query)
    
    # Récupérez les résultats
    results = cursor.fetchall()
    
    # Fermez le curseur
    cursor.close()
    
    # Retournez les résultats en tant que JSON
    return jsonify({'movies': results})

if __name__ == '__main__':
    app.run(debug=True)
