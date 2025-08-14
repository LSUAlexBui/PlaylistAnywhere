import json
import requests
from clientKeys import client_id, client_secret, redirect_uri, response_type

spotifyurl = "https://api.spotify.com"


auth_url = "https://accounts.spotify.com/api/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials","client_id": client_id,"client_secret": client_secret
}

response = requests.post(auth_url, headers=headers, data=data)
resp_json = response.json()
print(resp_json)

authorization = f"{resp_json['token_type']} {resp_json['access_token']}"
headers = {
    "Authorization": authorization
}

playlist_url = "https://open.spotify.com/playlist/1sfIs6G2KpBwueBLVzEmWr?si=858b887bb6db41fc"
remove = "https://open.spotify.com/playlist/"
playlist_id = playlist_url.replace(remove, "")
api_playlist_url = "https://api.spotify.com/v1/playlists/" + playlist_id

def get_playlist(url, headers):
    playlist_response = requests.get(url, headers=headers)
    if playlist_response.status_code != 200:
        print(f"Error fetching playlist: {playlist_response.status_code}")
        return
    print(playlist_response.json())
    json_data1 = playlist_response.json()
    return json_data1
json_data1 = get_playlist(api_playlist_url, headers)
artist = []
songName = []

def extract_artists_and_songs(json_data):
    if not json_data or 'tracks' not in json_data or 'items' not in json_data['tracks']:
        print("No tracks/items found in playlist data.")
        return
    for item in json_data['tracks']['items']:
        track = item.get('track')
        if not track:
            continue
        name = track.get('name')
        if name:
            songName.append(name)
        artists_list = track.get('artists')
        if artists_list and len(artists_list) > 0:
            artist_name = artists_list[0].get('name')
            if artist_name:
                artist.append(artist_name)

extract_artists_and_songs(json_data1)

print("Artists:", artist)
print("Songs:", songName)

def login(client_id, response_type, redirect_uri):
    login_url = f"https://accounts.spotify.com/authorize?client_id={client_id}&response_type={response_type}&redirect_uri={redirect_uri}"
    return login_url
print("Login URL:", login(client_id, response_type, redirect_uri))
