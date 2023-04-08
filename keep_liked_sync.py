import authorize
import get_liked_tracks

USER_ID = 'jacob.harrington'
PLAYLIST_ID = '3S230lxqByD0irKKQU1ny3'
sp = authorize.main()

# function for gathering all liked songs from file
tracks = get_liked_tracks.all_from_file()

# function for gathering 50 most recent songs from spotify
potential_new_adds = get_liked_tracks.fifty_from_spotify(sp)

print(len(potential_new_adds))

# # function for comparing most recent with liked, finding new adds to be synchronized
new_adds = []

for t in potential_new_adds:
    if t not in tracks:
        new_adds.append(t.strip())

range_of_newly_added = len(new_adds)
print(f'range_of_newly_added: {range_of_newly_added}')
print(f'tracks: {len(tracks)}')

# # function to synchronize new adds (should already exist)
sp.user_playlist_add_tracks(user=USER_ID,
                            playlist_id=PLAYLIST_ID,
                            tracks=new_adds)

sp.user_playlist_reorder_tracks(user=USER_ID,
                                playlist_id=PLAYLIST_ID,
                                range_start=len(tracks),
                                range_length=range_of_newly_added,
                                insert_before=0)

with open ('alltracks', 'a') as file:
    for t in new_adds:
        print(t)
        file.write(f'{t}\n')
