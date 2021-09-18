import sqlalchemy.exc
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()


@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template("index.html", books=all_books)


@app.route("/edit/<book_id>", methods=["GET", "POST"])
def edit_rating(book_id):
    if request.method == 'POST':
        new_rating = request.form['new_rating']
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = float(new_rating)
        db.session.commit()
        return redirect(url_for('home'))

    edited_book = Book.query.get(book_id)
    return render_template("edit.html", book=edited_book)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Create record
        new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        try:
            db.session.commit()
        except sqlalchemy.exc.StatementError:
            # Display error if the input is not in the correct format
            return render_template("add.html", error=True)
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/delete")
def delete_book():
    book_id = request.args.get('book_id')
    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
