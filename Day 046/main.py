from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = os.environ.get("SPOTIFY_ID")
SPOTIFY_SECRET = os.environ.get("SPOTIFY_SECRET")
SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME")

# ************ CREATION OF THE PLAYLIST *************
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
#                                                client_secret=SPOTIFY_SECRET,
#                                                redirect_uri="http://127.0.0.1:9090",
#                                                scope="playlist-modify-private"))
#
#
# sp.user_playlist_create(SPOTIFY_USERNAME, "Test", False, False, description="Testing stuff")

# ************ GET ALL MY PLAYLIST (TO CHECK IF THE PLAYLIST "TIME MACHINE" EXIST) *************
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                               client_secret=SPOTIFY_SECRET,
                                               redirect_uri="http://127.0.0.1:9090",
                                               scope="playlist-read-private"))


my_playlists = sp.user_playlists(SPOTIFY_USERNAME)

for items in my_playlists["items"]:
    print(items["name"])


year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# ************ SCRAPING THE TOP 100 SONGS FROM GIVEN YEAR *************
url = f"https://www.billboard.com/charts/hot-100/{year}"
r = requests.get(url)
billboard_page = r.text

soup = BeautifulSoup(billboard_page, 'html.parser')
song_titles = soup.find_all("span", class_="chart-element__information__song")
song_titles_list = [title.getText() for title in song_titles]

print(song_titles_list)

