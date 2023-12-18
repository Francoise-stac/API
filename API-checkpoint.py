from flask import Flask, jsonify
import pandas as pd


app = Flask(__name__)
df = pd.DataFrame({'item_id':["12","13","14"], 'name':['douze', 'treize', 'quatorze']})
@app.route('/')
def home():
    return "hello toi"
@app.route('/api/<int:item_id>', methods=['GET'])
def get_data(item_id):
    item_id = str(item_id)
    return jsonify({'name': df[df.item_id == item_id].name.item()})
if __name__ == '__main__':
    app.run(debug=True)
    
    
    from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:francy@localhost/fil_rouge2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    year = db.Column(db.Integer)

# Créez le contexte de l'application
with app.app_context():
    # Créez la table
    db.create_all()

# Exemple de données pour la démonstration
sample_data = [
    {'title': 'Film 1', 'year': 1987},
    {'title': 'Film 2', 'year': 1987},
    {'title': 'Film 3', 'year': 1988},
]

for data in sample_data:
    movie = Movie(title=data['title'], year=data['year'])
    db.session.add(movie)

db.session.commit()

@app.route('/')
def home():
    return "Hello toi"

@app.route('/api/<int:year>', methods=['GET'])
def get_movies_by_year(year):
    movies = Movie.query.filter_by(year=year).all()
    movie_list = [{'title': movie.title, 'year': movie.year} for movie in movies]
    return jsonify({'movies': movie_list})

if __name__ == '__main__':
    app.run(debug=True)
