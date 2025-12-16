import ytmusicapi 
from MyKeys import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET
from ytmusicapi import YTMusic, OAuthCredentials
import json

clientID = GOOGLE_CLIENT_ID
clientSecret = GOOGLE_CLIENT_SECRET
oAuth = ytmusicapi.setup_oauth(client_id=clientID,client_secret=clientSecret,filepath="oauth.json",open_browser=True)
ytmusic = YTMusic("oauth.json",oauth_credentials=OAuthCredentials(client_id=clientID,client_secret=clientSecret))


class YoutubeMusic:
    verificationCode = ""
    oldPlaylist = {
        'title': "",
        'coverArt': {
            'url': '',
            'height': 1200,
            'width': 1200
        },
        'description': "",
        'tracks': [],
        'artists': [],
    }
    def init(self):
        oAuth = ytmusicapi.setup_oauth(client_id=clientID,client_secret=clientSecret,open_browser=True)
        ytmusic = YTMusic("oauth.json", oauth_credentials=OAuthCredentials(client_id=clientID, client_secret= clientSecret))


    def getPlaylist(self, to_apple_music = False,playlistID =""):
        playlist = ytmusic.get_playlist(playlistID, None, False,0)
        YoutubeMusic.oldPlaylist["title"] = playlist["title"]
        YoutubeMusic.oldPlaylist["description"] = playlist["description"]
        YoutubeMusic.oldPlaylist['songCount'] = playlist['trackCount']
        YoutubeMusic.oldPlaylist['coverArt']['url'] = playlist['thumbnails'][2]['url']
        if to_apple_music == False:
            for i, track in enumerate(playlist['tracks']):
                YoutubeMusic.trackList.append(track['title'])
            for i, artist in enumerate(track['artists']):
                name = ""
                if len(name) == 0:
                    name = artist['name']
                else:
                    name = name + ' ' + artist['name']
                YoutubeMusic.oldPlaylist["artists"].append(name)
        else:
            for i, track in enumerate(playlist['tracks']):
                if track['videoType'] == "None":
                    continue
                else:
                    YoutubeMusic.trackList.append(track['title'])
                    for i, artist in enumerate(track['artists']):
                        name = ""
                        if len(name) == 0:
                            name = artist['name']
                        else:
                            name = name + ' ' + artist['name']
                YoutubeMusic.oldPlaylist['tracks'].append(name)
        return YoutubeMusic.oldPlaylist            

    def createPlaylist(self,playlistData ={}):
        playlistID = YTMusic.create_playlist(title=playlistData['title'],description=['description'],)
        songIDList = []
        for i in range(playlistData['tracks']):
            search = ytmusic.search(query=playlistData['artists'][i] +" "  + playlistData['tracks'][i],filter="songs", limit= 1 )
            name = ""
            for i, artist in enumerate(search[0]['artists']):
                if len(name) == 0:
                    name = artist['name']
                else:
                    name = name + " " + artist['name']
            song = search[0]['title']
            if  artist != playlistData['artist'] and song != playlistData['tracks']:
                continue
            else: 
                songIDList.append(ytmusic.search(query=playlistData['artists'][i] +" "  + playlistData['tracks'][i],filter="songs" ))
        ytmusic.add_playlist_items(playlistId=playlistID,videoIds=songIDList)
        
            
