from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap
import os


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app


SECRET_KEY = os.urandom(32)


class UsernameForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


# app = Flask(__name__)
app = create_app()
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = UsernameForm()
    login_form.validate_on_submit()

    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=False)
