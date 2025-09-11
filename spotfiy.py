import json
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from clientKeys import client_id, client_secret, redirect_uri, scope

class SpotifyMusic:

    spotifyurl = "https://api.spotify.com"

    #get input on these variables
    public = True


    auth_url = "https://accounts.spotify.com/api/token"
    sp_oauth = SpotifyOAuth(client_id, client_secret, redirect_uri, scope)
    token_info = None


    code = sp_oauth.get_auth_response()
    token_info = sp_oauth.get_access_token(code=code, as_dict=True)

    print("Token scopes:", token_info.get('scope'))
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope
    ))

    user_id = sp.current_user()['id']

    # headers = {
    #     "Content-Type": "application/x-www-form-urlencoded"
    # }
    # data = {
    #     "grant_type": "client_credentials","client_id": client_id,"client_secret": client_secret
    # }

    # response = requests.post(auth_url, headers=headers, data=data)
    # resp_json = response.json()
    # print(resp_json)

    headers = {"Authorization": f"Bearer {token_info['access_token']}"}

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
    @staticmethod
    def get_playlist(url, headers):
        playlist_response = requests.get(url, headers=headers)
        if playlist_response.status_code != 200:
            print(f"Error fetching playlist: {playlist_response.status_code}")
            return
        print(playlist_response.json())
        json_data1 = playlist_response.json()
        return json_data1
    json_data1 = get_playlist(api_playlist_url, headers)
    @staticmethod
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
        if images and "url" in images[0]:
            SpotifyMusic.playlist["coverArt"]["url"] = images[0]["url"]
        else:
            SpotifyMusic.playlist["coverArt"]["url"] = ""
        SpotifyMusic.playlist["title"] = json_data.get("name", "")
        SpotifyMusic.playlist["description"] = json_data.get("description", "")
    def createPlaylist(playlist, user_id):
        new_playlist = SpotifyMusic.sp.user_playlist_create(user=user_id, 
                                       name=playlist["title"], 
                                       public=True, 
                                       description=playlist["description"])
        return new_playlist 
    def addSongs(playlist, new_playlist):
         track_uris = []
         for track in playlist["tracks"]:
             results = SpotifyMusic.sp.search(q=track, type='track', limit=1)
             items = results.get('tracks', {}).get('items', [])
             if items:
                 track_uris.append(items[0]['uri'])
         if track_uris:
             SpotifyMusic.sp.playlist_add_items(playlist_id=new_playlist['id'], items=track_uris)
         else:
             print("No tracks found to add.")
         return




SpotifyMusic.extract_artists_and_songs(SpotifyMusic.json_data1)
print("Artists:", SpotifyMusic.playlist["artists"])
print("Songs:", SpotifyMusic.playlist["tracks"])
print(SpotifyMusic.playlist["coverArt"]["url"])
print(SpotifyMusic.playlist["description"])
new_playlist = SpotifyMusic.createPlaylist(SpotifyMusic.playlist, SpotifyMusic.user_id)
SpotifyMusic.addSongs(SpotifyMusic.playlist, new_playlist)
