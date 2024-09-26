import requests

blog_url = "https://api.npoint.io/22980569028cbfc903db"
response = requests.get(url=blog_url)
all_posts = response.json()
print(all_posts[0]['title'])