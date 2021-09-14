from flask import Flask, render_template
import requests

app = Flask(__name__)

r = requests.get(url="https://api.npoint.io/4c3ac473e7db5a14d32c")
blog_posts = r.json()


@app.route("/")
def home():
    return render_template("index.html", posts=blog_posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:post_id>")
def get_post(post_id):
    requested_post = None
    for post in blog_posts:
        if post["id"] == post_id:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)