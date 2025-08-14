import requests
import YTMusic
from flask import Flask, request, jsonify

spotifyURL = "https://api.spotify.com."

def main():
    YTMusic.startYTMusic()
    YTMusic.createPlaylist("Ts works")
