from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import requests
import os

MOVIE_API_KEY = os.getenv("moviedb_api")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)


# CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=True)
    ranking = db.Column(db.Integer, unique=False, nullable=True)
    review = db.Column(db.String(250), unique=False, nullable=True)
    img_url = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return '<Movie %r>' % self.title


db.create_all()


class EditForm(FlaskForm):
    """Create "Edit" form with Flask WTF"""
    rating = StringField('Your rating out of 10 (e.g 7.5)')
    review = StringField('Your Review')
    submit = SubmitField('Done')


class AddForm(FlaskForm):
    """Create "Edit" form with Flask WTF"""
    movie_title = StringField('Movie Title')
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    movies_list = db.session.query(Movie).order_by(Movie.rating)
    n = db.session.query(Movie).count()

    for item in movies_list:
        item.ranking = n
        db.session.commit()
        n -= 1
    return render_template("index.html", movies=movies_list)


""" Angela solution
    #This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.rating).all()
    
    #This line loops through all the movies
    for i in range(len(all_movies)):
        #This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)
"""


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        r_params = {
            "api_key": MOVIE_API_KEY,
            "query": request.form["movie_title"],
        }
        themoviedb_url = "https://api.themoviedb.org/3/search/movie"

        r = requests.get(url=themoviedb_url, params=r_params)
        search_result = r.json()
        return render_template("select.html", movies=search_result["results"])

    return render_template("add.html", form=add_form)


@app.route("/populate")
def populate_database():
    if request.args.get('movie_id'):
        r = requests.get(
            url=f"https://api.themoviedb.org/3/movie/{int(request.args.get('movie_id'))}?api_key={MOVIE_API_KEY}")
        search_result = r.json()
        new_db_entry = Movie(title=search_result["original_title"],
                             year=search_result["release_date"],
                             description=search_result["overview"],
                             img_url=f"https://image.tmdb.org/t/p/w500{search_result['poster_path']}")

        db.session.add(new_db_entry)
        db.session.commit()
        return redirect(url_for("edit", movie_id=new_db_entry.id))
    return redirect(url_for("home"))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    edit_form = EditForm()
    movie_id = request.args.get("movie_id")
    movie = Movie.query.get(movie_id)

    if edit_form.validate_on_submit():
        movie.rating = float(request.form["rating"])
        movie.review = request.form["review"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=edit_form, title=movie.title)


@app.route("/delete")
def delete():
    movie_id = request.args.get("movie_id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
