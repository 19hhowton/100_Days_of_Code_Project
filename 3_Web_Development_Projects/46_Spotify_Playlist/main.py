import os
from dotenv import load_dotenv 
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests


################################################## SET UP ##################################################
load_dotenv("46_Spotify_Playlist\.env")

CLIENT_ID = os.getenv("CLIENT_ID")
SECRET = os.getenv("SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
# USER_ID = os.getenv("USER_ID")
# scope_selection = 'playlist-modify-public'
# scope_selection="playlist-modify-private"
scope_selection="user-library-read playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope_selection,
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=SECRET
    )
)

user_id = sp.current_user()["id"]

################################################## CREATE MUSIC LISTS ##################################################
year = input("What year you would like to travel to (in YYYY-MM-DD format): ") 

#1998-02-21
Url = f"https://www.billboard.com/charts/hot-100/{year}/"
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

################################################## CREATE PLAYLIST ##################################################
playlist_name = f"Top Hits from {year}"  
my_playlist = sp.user_playlist_create(user=f"{user_id}", name=playlist_name, public=False,
                                      description="Top Tracks from back in...")

playlist_id = my_playlist["id"]

sp.playlist_add_items(playlist_id, items=track_uri_list)
