from json import loads, dumps
from sys import exit

try:
    plug = loads(open("PLUG_PLAYLISTS.json").read())
except FileNotFoundError:
    exit("\"PLUG_PLAYLISTS.json\" not found. Please add it to the same directory as this script.")

final_playlists = {}

try:
    playlist = input("Which playlist would you like to export? {playlists} ".format(
        playlists='/'.join(['['+pl+']' for pl in plug['playlists'].keys()])))
except KeyError:
    exit("Unknown playlist.")

print("Doing magic...")

final_playlists[playlist] = []
for song in plug['playlists'][playlist]:
    if song['type'] == 1:
        final_playlists[playlist].append(song)

final = plug.copy()
final['playlists'] = final_playlists

open("PYE_YOUTUBE.json", 'w').write(dumps(final))

print("Done. Saved to PYE_YOUTUBE.json.")
