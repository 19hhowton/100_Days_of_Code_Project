from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/22980569028cbfc903db"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route("/post/<num>") #0, 1, 2 @input 1, but it's 0 
def get_article(num):
    blog_url = "https://api.npoint.io/22980569028cbfc903db"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("post.html", post=all_posts[int(num) - 1])

if __name__ == "__main__":
    app.run(debug=True)
