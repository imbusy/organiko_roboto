Geometric Inversion
===================

A circle geometric inversion of a simple grid with the radius of the reference circle
expanding and the grid translating diagonally.

https://en.wikipedia.org/wiki/Inversive_geometry

Written for readability, not performance. To generate the frames, type:

    python generate.py

Frames are writen to the `frames/` directory. The output was used to generate a video using
ffmpeg command:

    ffmpeg -framerate 15 -i frames/img%03d.png -c:v mpeg4 geometric_inversion.mp4

Tested using Python 3.5 and requires the Pillow library.
