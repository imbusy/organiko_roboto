Sierpinski Triangle
===================

https://en.wikipedia.org/wiki/Sierpinski_triangle

Written for readability, not performance. To generate the frames, type:

    python generate.py

Frames are writen to the `frames/` directory. The output was used to generate a video using
ffmpeg command:

    ffmpeg -framerate 25 -i frames/img%03d.png -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p sierpinski_triangle.mp4

Tested using Python 3.6 and requires the Pillow library.
