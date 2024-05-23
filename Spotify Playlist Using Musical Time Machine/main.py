import json
from pprint import pprint

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""


# response = requests.get(
#     "https://www.billboard.com/charts/hot-100/2000-08-12/")
#
# with open("./song_list.txt", "w", encoding="utf-8") as sink:
#     sink.write(response.text)
# print("Done ...")

def create_spotipy_instance(scope_name):
    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET,
                                                     scope=scope_name, redirect_uri="http://example.com"))


# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# with open("./song_list.txt") as source:
#     html_cache = source.read()
#
# soup = BeautifulSoup(html_cache, "html.parser")
#
# h3_element_list = soup.select(selector="div ul li ul li h3")
# song_titles = [h3.get_text().strip() for h3 in soup.select(selector="div ul li ul li h3")]
#
# print(song_titles)
# print(len(song_titles))
#
# scope = "playlist-read-private"
# sp = create_spotipy_instance(scope)
# user_playlists = sp.current_user_playlists()
# pprint(user_playlists)
# item_list = user_playlists["items"]
#
# # Check for existing playlist name Top 100 Songs
# playlist_exists = False
# for item in item_list:
#     if len(item_list) != 0 and item["name"] == "Top 100 Songs":
#         playlist_exists = True
#
# # Create a user_playlist of Top 100 Songs in spotify if id does not exist
# if not playlist_exists:
#     scope = "playlist-modify-private"
#     sp = create_spotipy_instance(scope)
#     user_id = sp.me()['id']
#     name = "Top 100 Songs"
#     description = "Playlist containing top 100 songs of a particular date in past"
#
#     results = sp.user_playlist_create(user_id, name, public=False, description=description)
#     print(results)
#
# # Search for all the song titles inside our song_titles list and generate a list of song_URI
# uri_list = []
# for title in song_titles:
#     results = sp.search(q=f'track: {title} year: 2000', type='track', limit=1, offset=0, market=None)
#     uri = results['tracks']['items'][0]['uri']
#     uri_list.append(uri)
#
# print(uri_list)
# print(len(uri_list))
##########################################################
# Check for existing playlist named 2000-08-12 Billboard 100 in spotify
scope = "playlist-read-private"
sp = create_spotipy_instance(scope)
user_playlists = sp.current_user_playlists()
item_list = user_playlists["items"]

playlist_exists = False
for item in item_list:
    if len(item_list) != 0 and item["name"] == "2000-08-12 Billboard 100":
        playlist_exists = True

if not playlist_exists:
    scope = "playlist-modify-private"
    sp = create_spotipy_instance(scope)
    user_id = sp.me()['id']
    name = "2000-08-12 Billboard 100"
    description = "Playlist containing top 100 songs of a particular date in past."

    results = sp.user_playlist_create(user_id, name, public=False, description=description)
    pprint(results["id"])
    # sp.playlist_add_items(playlist_id, items, position=None)

    # # Create a user_playlist of Top 100 Songs in spotify if id does not exist
    # if not playlist_exists:
    #     scope = "playlist-modify-private"
    #     sp = create_spotipy_instance(scope)
    #     user_id = sp.me()['id']
    #     name = "Top 100 Songs"
    #     description = "Playlist containing top 100 songs of a particular date in past"

    results = sp.user_playlist_create(user_id, name, public=False, description=description)
    print(results)
