# plug-export


## Purpose
This repository contains two scripts, each of which pulls a specific type of song from a generated `PLUG_PLAYLISTS.json` file. As the YouTube API is slow and cannot handle as many songs as some may have in their Plug playlists, these scripts can help to separate the SoundCloud songs out completely, and the YouTube songs out by playlists, so that they can be sent to their respective websites through the PYE tool.


## Use

### ~~Obtaining `PLUG_PLAYLISTS.json` from PYE~~
It is no longer possible to obtain a new `PLUG_PLAYLISTS.json` file, as plug.dj has been officially shut down already. The rest of this tutorial assumes that you already have a `PLUG_PLAYLISTS.json` file from PYE.

### Including `PLUG_PLAYLISTS.json`
Move or copy your `PLUG_PLAYLISTS.json` file to the directory of the `export-soundcloud.py` and `export-youtube.py` scripts.

### SoundCloud
1. Run the `export-soundcloud.py` file, included in this repository, with Python 3.4+.
2. Assuming everything worked properly, you should receive a confirmation that everything worked properly, and that `PYE_SOUNDCLOUD.json` has been created. If an error appears, please ensure that `PLUG_PLAYLISTS.json` is in this directory.
3. Go to [the PYE site](http://pye.sq10.net/), click on the box shown, select your `PYE_SOUNDCLOUD.json` file, and you're good to go! Make sure to authenticate SoundCloud when prompted to, but don't worry about YouTube - it isn't included at all in this file.
4. Wait for PYE to do its magic, and you're done!

### YouTube
1. Run the `export-youtube.py` file, included in this repository, with Python 3.4+.
2. You will be prompted to choose one of the existing playlists. Type in the playlist's name *exactly*, and press enter.
3. Assuming everything worked properly, you should receive a confirmation that everything worked properly, and that `PYE_YOUTUBE.json` has been created. If an error appears, please ensure that `PLUG_PLAYLISTS.json` is in this directory, and that the playlist inputted exists and was spelled properly (with correct capitalization).
4. Go to [the PYE site](http://pye.sq10.net/), click on the box shown, select your `PYE_YOUTUBE.json` file, and you're good to go! Make sure to authenticate YouTube when prompted to, but don't worry about SoundCloud - it isn't included at all in this file.
4. Wait for PYE to do its magic, and you're done!
