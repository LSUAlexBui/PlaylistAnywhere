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

playlist_url = "https://open.spotify.com/playlist/47ijO8ixCB6ZZGMId8JHPY?si=63de8bff12164177"
remove = "https://open.spotify.com/playlist/"
playlist_id = playlist_url.replace(remove, "")
api_playlist_url = "https://api.spotify.com/v1/playlists/" + playlist_id

playlist = {
        "title": "",
        "coverArt": {
            "url": "",
            "width": 640,
            "height": 640
        },
        "description": "",
        "tracks": [],
        "artists": []       
    }



class SpotifyMusic:
    
    playlist = {
        "title": "",
        "coverArt": {
            "url": "",
            "width": 640,
            "height": 640
        },
        "description": "",
        "tracks": [],
        "artists": []       
    }
    def get_playlist(url, headers):
        playlist_response = requests.get(url, headers=headers)
        if playlist_response.status_code != 200:
            print(f"Error fetching playlist: {playlist_response.status_code}")
            return
        print(playlist_response.json())
        json_data1 = playlist_response.json()
        return json_data1
    json_data1 = get_playlist(api_playlist_url, headers)

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
                SpotifyMusic.playlist["tracks"].append(name)
            artists_list = track.get('artists')
            if artists_list and len(artists_list) > 0:
                artist_name = artists_list[0].get('name')
                if artist_name:
                    SpotifyMusic.playlist["artists"].append(artist_name)
        SpotifyMusic.playlist["coverArt"]["url"] = ""
        images = json_data.get("images", [])
        SpotifyMusic.playlist["coverArt"]["url"] = images[0]["url"]
        SpotifyMusic.playlist["title"] = json_data.get("name", "")
        SpotifyMusic.playlist["description"] = json_data.get("description", "")
    def createPlaylist(self.playlistdata =()):



        
                    
    
    

    def login(client_id, response_type, redirect_uri):
        login_url = f"https://accounts.spotify.com/authorize?client_id={client_id}&response_type={response_type}&redirect_uri={redirect_uri}"
        return login_url
    print("Login URL:", login(client_id, response_type, redirect_uri))
SpotifyMusic.extract_artists_and_songs(SpotifyMusic.json_data1)
print("Artists:", SpotifyMusic.playlist["artists"])
print("Songs:", SpotifyMusic.playlist["tracks"])
print(SpotifyMusic.playlist["coverArt"]["url"])
print(SpotifyMusic.playlist["description"])
