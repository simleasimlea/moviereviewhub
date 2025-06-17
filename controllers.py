from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Movie

main = Blueprint('main', __name__)

@main.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@main.route('/add', methods=['GET', 'POST'])
def add():
    print("Request method is:", request.method)
    if request.method == 'POST':

        new_movie = Movie(
            title=request.form['title'],
            director=request.form['director'],
            review=request.form['review']
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add.html')




