from src.fixify import load


def add_tracks(sp, playlist, target_playlist):
    '''Add all (new) tracks from one playlist to another.'''

    tracks = sp.playlist_items(playlist)
    while tracks:
        the_tracks = []
        for track in tracks['items']:
            # Filter local files.
            if not track['is_local']:
                the_tracks.append(track['track']['id'])
        # Remove (dublicates)
        sp.playlist_remove_all_occurrences_of_items(
            target_playlist, the_tracks)
        # Add items
        sp.playlist_add_items(target_playlist, list(set(the_tracks)))
        if tracks['next']:
            tracks = sp.next(tracks)
        else:
            tracks = None


def add_filtered_user_playlists(sp, filter, target_playlist):
    '''Add all tracks from one playlist to another, if filter matches.'''

    playlists = sp.current_user_playlists()

    while playlists:
        for playlist in playlists['items']:
            if filter in playlist['description']:
                add_tracks(sp, playlist['id'], target_playlist)
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None


def main():

    # Load Spotify.
    (sp, config) = load()

    # Load the target playlists.
    playlists = config['TaggedToPlaylist']['Playlists'].split(',')

    # Load the tags.
    tags = config['TaggedToPlaylist']['Tags'].split(',')

    # Empty the target playlists.
    for target in playlists:
        sp.playlist_replace_items(target, [])

    # Add the (tagged) user playlists to EasyDownload.
    for tag, target in zip(playlists, tags):
        add_filtered_user_playlists(sp, "#"+tag, target)


if __name__ == '__main__':
    main()
