import os
from dotenv import load_dotenv 
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests

load_dotenv("46_Spotify_Playlist\.env")

CLIENT_ID = os.getenv("CLIENT_ID")
SECRET = os.getenv("SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="user-library-read"))


Url = "https://www.billboard.com/charts/hot-100/1998-02-21/"
response = requests.get(url=Url)

soup = BeautifulSoup(response.text, "html.parser")

song_section = soup.find_all(name="ul", class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max")

songs = []
for section in song_section:
    song_name = section.find(name="h3", id="title-of-a-story")
    songs.append(" ".join((song_name.string).split()))

artists = []
for section in song_section:
    artist_name = section.span
    artists.append(" ".join((artist_name.string).split()))

track_uri_list = []
for i in range(0, len(artists)):
    try:
        search_query = f'track:{songs[i]} artist:{artists[i]}'
        results = sp.search(q=search_query, limit=1, type='track')
        track_uri_string = results["tracks"]["items"][0]["uri"]
        track_uri = track_uri_string.split(":")
        track_uri_list.append(track_uri[2])
    except:
        pass

print(track_uri_list)