# Fixify

Fixify is a collection of [spotipy](https://spotipy.readthedocs.io/en/master/)-based Spotify tools for managing playlists.

### Setup

Create a Spotify [App](https://developer.spotify.com/dashboard/). You'll need your client ID and secret. Also, configure the apps redirect URI to `http://localhost:8888` (default) or whatever you'll set in `fixify.ini`.

Next, create the file `fixify.ini` (you can base this on the provided file `fixify-default.ini` and also consult `fixify-example.ini` for an extended example) and fill in your client ID and secret (and possibly update the redirect URI). You will also need to insert playlist IDs and other configurations in this file (see the sections about the Fixify tools below).

When running any of the scripts below (for the first time), the `spotipy` backend will open a browser tab for requesting the required Spotify permissions.

### `all_albums_to_playlist`

This script emulates the missing play-all-albums-in-library option by generating a playlist from all albums in your library. This is limited to 10.000 songs, i.e., one playlist. The target playlist is `AllAlbumsToPlaylist.Library` in the config. Note, that the playlist is emptied beforehand!

The script also uses `AllAlbumsToPlaylist.Words` and `AllAlbumsToPlaylist.Separators`, two comma separated strings of keywords and separators. If non-empty, any track with any one of the keywords after the first occurrence of any one of the separators are removed from the playlist. If you do not wish to filter any songs, leave these settings empty (e.g., `Words =`).

**Rationale**: I use this to filter unwanted live and demo versions (commonly part of many "extended" editions of albums) with `Words = live,demo,rehearsal`  and `-,(`. It's quite effective. 

### `tagged_to_playlist`

This is a configurable script for smarter playlist management. It allows tagging playlist (descriptions) and then collects all tagged playlist and joins them together in a target playlist. To this end, the settings `TaggedToPlaylist.Playlists` and `TaggedToPlaylist.Tags` are two comma separated lists of playlists and corresponding tags for filling them up. Note, that the component strings in `Tags` need to be prefixed with a `#` in the playlist description. All playlists are emptied beforehand. Local files are ignored (API restriction). No duplicate tracks are kept and duplicates from the input playlists are removed. This is also limited to 10.000 tracks (i.e., one playlist).

**Rationale**: I use this mainly to tag playlists with #download to create a one-button-press playlist for all music I want to download on mobile. But there may be other interesting use cases, such as creating a combined playlist from multiple sub-playlists, similar to a playlist folder - that you can actually play on mobile.

### TODOs ###

Here follows a collection of a few tools I plan to implement. First, as I do not use "like" for songs, a variant of `all_albums_to_playlist` that instead of a playlist adds all songs from albums to liked songs, thereby exceeding the limitation of 10.000 songs. (Using multiple playlists instead does not really make sense if the use case is to shuffle the whole collection).