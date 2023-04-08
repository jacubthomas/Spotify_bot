import json

def create_playlist(sp, USER_ID):
    playlist = sp.user_playlist_create(user=USER_ID,
                                    name='l!k3d',
                                    public='true',
                                    description='Creating public playlist mirroring liked songs')
    y = json.loads(json.dumps(playlist))

    playlistId = y['id']
    return playlistId

def add_tracks_to_playlist(sp, USER_ID, PLAYLIST_ID, tracks, start, end):

    batch_tracks = tracks[start:end+1]

    sp.user_playlist_add_tracks(user=USER_ID,
                                playlist_id=PLAYLIST_ID,
                                tracks=batch_tracks)
