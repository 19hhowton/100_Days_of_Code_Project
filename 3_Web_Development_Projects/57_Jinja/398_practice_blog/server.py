from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    curr_year = datetime.today().year
    return render_template("index.html", curr_year=curr_year)

@app.route("/blog")
def get_blog_page():
    blog_url = "https://api.npoint.io/22980569028cbfc903db"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/22980569028cbfc903db"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)