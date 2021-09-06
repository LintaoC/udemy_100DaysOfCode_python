from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        function()
        return f"<b>{function()}</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        function()
        return f"<em>{function()}</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        function()
        return f"<u>{function()}</u>"
    return wrapper_function


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1><p>This is a paragraph!</p><img src="https://media2.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif?cid=790b7611d63f372f1a25a7491a388efe5450f0de52e5b7cb&rid=giphy.gif&ct=g" width=200>'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

# @app.route('/username/<name>/1')
@app.route('/username/<name>/')
def greet(name):
    return f"<p>Hello, {name}!!</p>"

@app.route('/path/<path:name>')
def path(name):
    return f"<p>Hello, {name}!!</p>"

@app.route('/mv/<name>/<int:number>')
def multiple_var(name, number):
    return f"<p>Hello, {name}, you are the number {number}!!</p>"

if __name__ == "__main__":
    app.run(debug=False)