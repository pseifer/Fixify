import spotipy
import configparser
from spotipy.oauth2 import SpotifyOAuth


def load():
    config = configparser.ConfigParser()
    config.read('fixify.ini')

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=config['Fixify']['ClientId'],
            client_secret=config['Fixify']['ClientSecret'],
            redirect_uri=config['Fixify']['RedirectUri'],
            scope="user-library-read,playlist-modify-private,playlist-read-private"))

    return sp, config
