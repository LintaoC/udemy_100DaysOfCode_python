from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = os.environ.get("SPOTIFY_ID")
SPOTIFY_SECRET = os.environ.get("SPOTIFY_SECRET")
SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME")
PLAYLIST_NAME = "Time Machine"

# ************ CREATION OF THE PLAYLIST *************

def create_playlist():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                                   client_secret=SPOTIFY_SECRET,
                                                    redirect_uri="http://127.0.0.1:9090",
                                                    scope="playlist-modify-private"))
    
    
    sp.user_playlist_create(SPOTIFY_USERNAME, PLAYLIST_NAME, False, False, description="UDEMY Day 046 Spotify Time Machine")

# ************ GET ALL MY PLAYLIST (AND CHECK IF THE PLAYLIST "Time Machine" EXIST) *************

def check_for_playlist(name):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                                   client_secret=SPOTIFY_SECRET,
                                                   redirect_uri="http://127.0.0.1:9090",
                                                   scope="playlist-read-private"))
    
    my_playlists = sp.user_playlists(SPOTIFY_USERNAME)
    
    for items in my_playlists["items"]:
        if name == items["name"]:
            print(f"Playlist ID: {items['id']}")
            return True
        else:
            return False
        
# ************ get the song ID from a song title + year *************        
def get_song_list_uri():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                                   client_secret=SPOTIFY_SECRET,
                                                   redirect_uri="http://127.0.0.1:9090",
                                                   scope="user-read-private"))
        
    search_result = sp.search(q="one more time year:2001", type="track")
    print(search_result["tracks"]["items"][0]["uri"])
    

# ************ Add a list of track to the playlist *************        
def add_track_to_playlist():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                                   client_secret=SPOTIFY_SECRET,
                                                   redirect_uri="http://127.0.0.1:9090",
                                                   scope="playlist-modify-private"))
        
    sp.user_playlist_add_tracks(SPOTIFY_USERNAME, "1JJQpB7iHuAApaeJRVvUQR",["spotify:track:0DiWol3AO6WpXZgp0goxAV"])
    

# ************ Remove a list of track to the playlist *************        
def remove_track_to_playlist():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                                   client_secret=SPOTIFY_SECRET,
                                                   redirect_uri="http://127.0.0.1:9090",
                                                   scope="playlist-modify-private"))
        
    sp.user_playlist_remove_all_occurrences_of_tracks(SPOTIFY_USERNAME, "1JJQpB7iHuAApaeJRVvUQR",["spotify:track:0DiWol3AO6WpXZgp0goxAV"])


# If the "Time Machine" playlist do not exist, we create it. 
if check_for_playlist(PLAYLIST_NAME):
    print("No need to create a new playlist")
else:
    create_playlist()
    print("I create the time machine playlist")

get_song_list_uri()
#add_track_to_playlist()
remove_track_to_playlist()

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# ************ SCRAPING THE TOP 100 SONGS FROM GIVEN YEAR *************
url = f"https://www.billboard.com/charts/hot-100/{year}"
r = requests.get(url)
billboard_page = r.text

soup = BeautifulSoup(billboard_page, 'html.parser')
song_titles = soup.find_all("span", class_="chart-element__information__song")
song_titles_list = [title.getText() for title in song_titles]

print(song_titles_list)
