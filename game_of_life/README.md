Conway's Game of Life
=====================

Written for readability, not performance. To generate the frames, type:

    python generate.py

Frames are writen to the `frames/` directory. The output was used to generate a video using
ffmpeg command:

    ffmpeg -framerate 25 -i frames/img%03d.png game_of_life.mp4

Tested using Python 3.5 and requires the Pillow library.