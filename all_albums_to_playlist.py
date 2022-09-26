from src.fixify import load
import itertools


def exclude(track, words, separators):
    '''Heuristic for exclusion of live tracks.'''

    def mkfilter(keyword, separator):
        return keyword in ' '.join(track.lower().split(separator)[1:])

    ws = words.split(',')
    ss = separators.split(',')

    for (w, s) in itertools.product(ws, ss):
        if mkfilter(w, s):
            return True
    return False


def add_album(sp, album, playlist, words, separators):
    '''Add all tracks of an album to a playlist.'''

    the_tracks = []
    for track in album['tracks']['items']:
        if not exclude(track['name'], words, separators):
            the_tracks.append(track['id'])
    sp.playlist_add_items(playlist, the_tracks)


def add_user_albums(sp, playlist, words, separators):
    '''Add all user albums to a playlist.'''

    albums = sp.current_user_saved_albums()

    while albums:
        for album in albums['items']:
            add_album(sp, album['album'], playlist, words, separators)

        if albums['next']:
            albums = sp.next(albums)
        else:
            albums = None


def main():

    # Load Spotify.
    (sp, config) = load()

    # Load the library from the configuration.
    library = config['AllAlbumsToPlaylist']['Playlist']

    # Load the Filters
    words = config['AllAlbumsToPlaylist']['Words']
    separators = config['AllAlbumsToPlaylist']['Separators']

    # Empty the library.
    sp.playlist_replace_items(library, [])

    # Add all albums to the playlist.
    add_user_albums(sp, library, words, separators)


if __name__ == '__main__':
    main()
