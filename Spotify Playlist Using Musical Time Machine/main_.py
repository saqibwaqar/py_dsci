import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
USER_PLAYLIST_ENDPOINT = os.environ.get("USER_PLAYLIST_ENDPOINT")

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]
billboard_search_url = f"https://www.billboard.com/charts/hot-100/{date}/"

# Scrape top 100 song titles into list
html_response = requests.get(url=billboard_search_url).text
soup = BeautifulSoup(html_response, "html.parser")
song_titles = [h3.get_text().strip() for h3 in soup.select(selector="div ul li ul li h3")]
print(f"Scraped titles: {song_titles}")
print(f"Scraped list size:{len(song_titles)}")

# Search for all the song titles inside song_titles list and generate a list of song_URIs
scope_name = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET,
                                               scope=scope_name, redirect_uri="http://example.com", show_dialog=True,
                                               cache_path="./token.txt"))
uri_list = []
for title in song_titles:
    results = sp.search(q=f'track:{title} year:{year}', type='track')
    try:
        uri = results['tracks']['items'][0]['uri']
        uri_list.append(uri)
    except IndexError:
        print(f"{title} does not exist in Spotify. Skipped")

print(f"Total URIs found:{len(uri_list)}")

# Create new playlist and add tracks
user_id = sp.me()['id']
name = f"{date} Billboard 100"
description = f"Playlist containing top 100 songs for the date {date}."

results = sp.user_playlist_create(user=user_id, name=name, public=False, description=description)
playlist_id = results["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=uri_list)
