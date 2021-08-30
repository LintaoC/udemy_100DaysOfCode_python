from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = os.environ.get("SPOTIFY_ID")
SPOTIFY_SECRET = os.environ.get("SPOTIFY_SECRET")
SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME")
PLAYLIST_NAME = "Time Machine"


def create_playlist():
    """CREATION OF THE PLAYLIST"""
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                                   client_secret=SPOTIFY_SECRET,
                                                   redirect_uri="http://127.0.0.1:9090",
                                                   scope="playlist-modify-private",
                                                   cache_path=".cache"))

    sp.user_playlist_create(SPOTIFY_USERNAME, PLAYLIST_NAME, False, False,
                            description="UDEMY Day 046 Spotify Time Machine")


def check_for_playlist(name):
    """GET ALL MY PLAYLIST (AND CHECK IF THE PLAYLIST "Time Machine" EXIST)"""
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                                   client_secret=SPOTIFY_SECRET,
                                                   redirect_uri="http://127.0.0.1:9090",
                                                   scope="playlist-read-private",
                                                   cache_path=".cache"))

    my_playlists = sp.user_playlists(SPOTIFY_USERNAME)

    for items in my_playlists["items"]:
        if name == items["name"]:
            print(f"Playlist ID: {items['id']}")
            return True, items['id']
        else:
            return False


def get_song_list_uri(track_name, track_year):
    """get the song ID from a song title + year"""
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                                   client_secret=SPOTIFY_SECRET,
                                                   redirect_uri="http://127.0.0.1:9090",
                                                   scope="user-read-private",
                                                   cache_path=".cache"))

    search_result = sp.search(q=f"{track_name} year:{track_year - 1}-{track_year}", type="track")
    return search_result["tracks"]["items"][0]["uri"]


def add_track_to_playlist(spotify_playlist_id, track_list):
    """Add a list of track to the playlist"""
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                                   client_secret=SPOTIFY_SECRET,
                                                   redirect_uri="http://127.0.0.1:9090",
                                                   scope="playlist-modify-private",
                                                   cache_path=".cache"))

    # Replacing the old playlist with the new one
    sp.playlist_replace_items(spotify_playlist_id, track_list)


# If the "Time Machine" playlist do not exist, we create it.
check_playlist = check_for_playlist(PLAYLIST_NAME)

if not check_playlist:
    create_playlist()
    playlist_id = check_for_playlist(PLAYLIST_NAME)[1]  # Getting the playlist ID
    print("I create the time machine playlist")
else:
    playlist_id = check_playlist[1]
    print("No need to create a new playlist")

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# ************ SCRAPING THE TOP 100 SONGS FROM GIVEN YEAR *************
url = f"https://www.billboard.com/charts/hot-100/{year}"
r = requests.get(url)
billboard_page = r.text

soup = BeautifulSoup(billboard_page, 'html.parser')
song_tracks = soup.find_all("span", class_="chart-element__information__song")
song_tracks_list = [title.getText() for title in song_tracks]

year = year.split("-")  # Getting the year from the date to refine the URI search
song_uri_list = []

# ************ Get song URI and adding them to a list *************
for track in song_tracks_list:
    try:
        song_uri_list.append(get_song_list_uri(track, int(year[0])))
    except IndexError:
        print("not found")

# ************ Add the tracks to the playlist *************
add_track_to_playlist(playlist_id, song_uri_list)
