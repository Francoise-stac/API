from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:francy@localhost/fil_rouge2'
db = SQLAlchemy(app)

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    year = db.Column(db.Integer)

@app.before_first_request
def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/')
def home():
    return "Hello toi"

@app.route('/api/<int:movie_id>', methods=['GET'])
def get_movie_year(movie_id):
    try:
        with app.app_context():
            movie = Movie.query.get(movie_id)
        
            if movie:
                return jsonify({'title': movie.title, 'year': movie.year})
            else:
                return jsonify({'error': 'Film non trouvé'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
