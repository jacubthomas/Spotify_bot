# custom imports
import authorize
import create_playlist
import get_liked_tracks

# standard imports
import json
import math
import time

# Spotify id that shows under AccountOverview/Profile/Username
USER_ID = 'jacob.harrington'

# Establish necessary credentials prior to interacting with SpotifyAPI
sp = authorize.main()

'''
Get all liked song IDs and write to file alltracks
'''
tracks = get_liked_tracks.all_from_spotify(sp)
tracks.reverse()
with open('alltracks', 'w') as f:
    for line in tracks:
        f.write(f"{line}\n")

'''
Retrieve all liked song IDs, previously fetched and stored in file `alltracks`
'''
tracks = get_liked_tracks.all_from_file()


'''
Create a playlist and add all songs retrieved from alltracks
'''
PLAYLIST_ID = create_playlist.create_playlist(sp, USER_ID)

'''
Synchronize all at once
'''
total = len(tracks)
iterations = math.ceil(total/50)
floor = math.floor(total/50)
for i in range (0, floor):
    i *= 50
    create_playlist.add_tracks_to_playlist(sp, USER_ID, PLAYLIST_ID, tracks, i, i+49)
    time.sleep(1)

create_playlist.add_tracks_to_playlist(sp, USER_ID, PLAYLIST_ID, tracks, floor*50, total)