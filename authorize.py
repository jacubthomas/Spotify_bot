import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def main ():
    # ingest credentials from file in same directory, named `spotify_credentials`
    # important to keep these in a separate file, so as to safeguard your private info
    credentials_file = open('spotify_credentials', 'r')
    Lines = credentials_file.readlines()
    CLIENT_ID = Lines[0].strip()
    CLIENT_SECRET = Lines[1].strip()
    REDIRECT_URI = Lines[2].strip()
    USER_ID = 'jacob.harrington'

    spotifyClientCredentials = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

    sp = spotipy.Spotify(client_credentials_manager=spotifyClientCredentials)

    token = spotipy.util.prompt_for_user_token(username=USER_ID,
                                            scope='playlist-modify-private playlist-modify-public',
                                            client_id=CLIENT_ID,
                                            client_secret=CLIENT_SECRET,
                                            redirect_uri=REDIRECT_URI)

    sp.__init__(auth=token,client_credentials_manager=spotifyClientCredentials)

    return sp