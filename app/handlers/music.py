from spotipy.oauth2 import SpotifyOAuth
import os
import spotipy
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id = SPOTIFY_CLIENT_ID,
            client_secret= SPOTIFY_CLIENT_SECRET,
            redirect_uri= SPOTIFY_REDIRECT_URI,
            scope= "user-read-playback-state,user-modify-playback-state,playlist-read-private"
))