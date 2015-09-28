from json import loads, dumps
from sys import exit

try:
    plug = loads(open("PLUG_PLAYLISTS.json").read())
except FileNotFoundError:
    exit("\"PLUG_PLAYLISTS.json\" not found. Please add it to the same directory as this script.")

final_playlists = {}

print("Doing magic...")

for playlist in plug['playlists']:
    final_playlists[playlist] = []
    for song in plug['playlists'][playlist]:
        if song['type'] == 2:
            final_playlists[playlist].append(song)
    if final_playlists[playlist] == []:
        final_playlists.pop(playlist)

final = plug.copy()
final['playlists'] = final_playlists

open("PYE_SOUNDCLOUD.json", 'w').write(dumps(final))

print("Done. Saved to PYE_SOUNDCLOUD.json.")
