from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/22980569028cbfc903db").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)
print(post_objects)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)

@app.route("/post/<int:num>") 
def get_article(num):
    requested_post = None
    for post in post_objects:
        if post.id == num:
            requested_post = post
    print(requested_post)
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
