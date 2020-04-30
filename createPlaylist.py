# Login to YouTube
# Grab our Liked Videos
# Create a new playlist
# Search for the song in Spotify
# Add this song to the Spotify playlist


import json
import requests
from secrets import spotify_token, spotify_user_id

class createPlaylist:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token


    # Login to YouTube
    def get_youtube_client(self):
        pass


    # Grab our Liked Videos
    def get_liked_videos(self):
        pass


    # Create a new playlist
    def create_playlist(self):
        
        request_body = json.dumps({
            "name": "YouTube liked Videos",
            "description": "All liked Videos from YouTube",
            "public": True
            }
        )

        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type":"application/json",
                "Authorizations":"Bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()

        # Playlist ID
        return response_json["id"]

    # Search for the song in Spotify
    def get_spotify_uri(self):
        pass


    # Add this song to the Spotify playlist
    def add_song_to_playlist(self):
        pass