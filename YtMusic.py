import ytmusicapi 
from MyKeys import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET
from ytmusicapi import YTMusic, OAuthCredentials
import requests 

clientID = GOOGLE_CLIENT_ID
clientSecret = GOOGLE_CLIENT_SECRET
oAuth = ytmusicapi.setup_oauth(client_id=clientID,client_secret=clientSecret,filepath="oauth.json")
ytmusic = YTMusic("oauth.json",oauth_credentials=OAuthCredentials(client_id=clientID,client_secret=clientSecret))
playlistID = ytmusic.create_playlist(title="IT WORKS", description="",privacy_status="Private")
ytmusic.add_playlist_items(playlistId=playlistID, videoIds=["6B3YwcjQ_bU"])
ytmusic.search()


def startYTMusic():
    oAuth = ytmusicapi.setup_oauth(client_id=clientID,client_secret=clientSecret)
    ytmusic = YTMusic("oauth.json", oauth_credentials=OAuthCredentials(client_id=clientID, client_secret= clientSecret))
    


def getPlaylist():
    playlistID = "PLVbT0jgppQfq1u5n-WjYncGE5ES3EQKiX&si=scwZxtyzXBzTNyuW"
    YTMusic.get_playlist(playlistID, None, False,0)

def createPlaylist(oldName =""):
    playlistID = YTMusic.create_playlist(oldName)
    YTMusic.add_playlist_items(playlistID,"o36scmAJE-U&si=GWhHLXLaXgrIsQPe")
