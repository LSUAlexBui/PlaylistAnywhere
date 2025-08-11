import requests

spotifyurl = "https://api.spotify.com"

client_id = "0d266fae9d834656bc19c86dabf686f8"
client_secret = "f036bf3c228b4ce899a1d3e9089f85f2"

auth_url = "https://accounts.spotify.com/api/token"
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials","client_id": client_id,"client_secret": client_secret
}

response = requests.post(auth_url, headers=headers, data=data)
print(response.json())

