from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

db.create_all()

#CREATE RECORD
book_1 = Book(title='Harry Potter', author='JKR', rating=9.0)
book_2 = Book(title='OuiOui', author='SmartDude', rating=9.0)
db.session.add(book_1)
db.session.add(book_2)
db.session.commit()

# Read All Records
all_books = db.session.query(Book).all()
print(all_books)

# Read A Particular Record By Query
book = Book.query.filter_by(title="Harry Potter").first()
print(book)

# Update A Particular Record By Query
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()
# Read All Records
all_books = db.session.query(Book).all()
print(all_books)

# Delete A Particular Record By PRIMARY KEY
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()
# Read All Records
all_books = db.session.query(Book).all()
print(all_books)

# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
