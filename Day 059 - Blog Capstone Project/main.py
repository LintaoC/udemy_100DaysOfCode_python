from flask import Flask, render_template
from flask import request
import requests
import smtplib
import os

app = Flask(__name__)

r = requests.get(url="https://api.npoint.io/4c3ac473e7db5a14d32c")
blog_posts = r.json()

my_email = os.getenv("mail")
password = os.getenv("password")

def send_email(mail_data):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:New message from my website\n\nName: {mail_data['form_name']}\n\n"
                f"Mail: {mail_data['form_email']}\n\nPhone: {mail_data['form_phone']}\n\n"
                f"Message: {mail_data['form_message']}")


@app.route("/")
def home():
    return render_template("index.html", posts=blog_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        data = request.form
        send_email(data)
        return render_template("contact.html", change_title=True)
    return render_template("contact.html", change_title=False)
            


@app.route("/post/<int:post_id>")
def get_post(post_id):
    requested_post = None
    for post in blog_posts:
        if post["id"] == post_id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)