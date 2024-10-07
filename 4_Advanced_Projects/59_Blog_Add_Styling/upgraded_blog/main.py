from flask import Flask, render_template
import requests
from post import Post

#https://www.npoint.io/docs/607b901b39eb60f3737f

posts = requests.get("https://api.npoint.io/607b901b39eb60f3737f").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["image_url"], post["date"], post["author"])
    post_objects.append(post_obj)
print(post_objects)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/contact')
def contact_page():
    return render_template("contact.html")

@app.route('/<num>')
def article_page(num):
    requested_post = None
    for post in post_objects:
        if post.id == int(num):
            requested_post = post
    return render_template("post.html", article=requested_post)

if __name__ == "__main__":
    app.run(debug=True)