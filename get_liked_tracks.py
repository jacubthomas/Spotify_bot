import math
def all_from_spotify(sp):

    track_ids = []

    tracks = sp.current_user_saved_tracks(limit=50)
    total = tracks['total']
    iterations = math.ceil(total/50)

    for i in range(0,iterations):
        i *= 50
        tracks = sp.current_user_saved_tracks(limit=50, offset=i)
        for j, item in enumerate(tracks['items']):
            track = item['track']
            track_ids.append(track['id'])

    return track_ids

'''
Retrieve all liked song IDs, previously fetched and stored in file `alltracks`
'''
def all_from_file():
    tracks_file = open('alltracks', 'r')
    Lines = tracks_file.readlines()
    total = len(Lines)

    tracks = []
    for line in Lines:
        if line.strip():
            tracks.append(line.strip())

    tracks.reverse() # remove this next time pull all tracks
    return tracks

def fifty_from_spotify(sp):

    track_ids = []
    tracks = sp.current_user_saved_tracks(limit=50)

    for j, item in enumerate(tracks['items']):
        track = item['track']
        track_ids.append(track['id'])

    return track_ids