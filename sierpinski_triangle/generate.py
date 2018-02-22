"""
Sierpinski triangle generator.

The sides of the original equilateral triangle are all equal to 1 and the 
coordinates of the three corners of the triangle are (0, 0), (0.5, sqrt(3)/2)
and (1, 0).
"""

from PIL import Image
from math import sqrt, sin, cos, pi, pow

width, height = (1280, 720)
frames = 200

# color for the inside of the triangle
color_1 = (255, 0, 0)
# color outside of the triangle
color_0 = (0, 0, 0)

triangle_height = sqrt(3) / 2

# the three orthogonal vectors of the sides of the triangle
n_1 = (0, 1)
n_2 = (-cos(pi * 30 / 180), sin(pi * 30 / 180))
n_3 = (cos(pi * 30 / 180), sin(pi * 30 / 180))

def dot(v_1, v_2):
  """ Returns the scalar product of vectors. """
  return v_1[0] * v_2[0] + v_1[1] * v_2[1]

INNER = 0
UPPER = 1
LOWER_LEFT = 2
LOWER_RIGHT = 3

def in_which(p):
  """
  Returns the result in which subtriangle the point falls in at
  original scale and translation.
  """
  if dot(p, n_1) > triangle_height / 2:
    return UPPER

  if dot(p, n_3) < triangle_height / 2:
    return LOWER_LEFT

  if dot(p, n_2) < -triangle_height / 2:
    return LOWER_RIGHT

  return INNER

for frame in range(frames):
  # scale at 1 fills the height of the image exactly
  scale = pow(1.03, frame) * 0.5
  image = Image.new('RGB', (width, height))
  for pixel_y in range(height):
    y = triangle_height * (height - pixel_y) / (height * scale)
    for pixel_x in range(width):
      x = triangle_height * pixel_x / (height * scale)

      p = (x, y)

      if dot(p, n_1) < 0 or \
         dot(p, n_2) > 0 or \
         dot(p, n_3) > triangle_height:
        # point is outside of the original large triangle
        image.putpixel((pixel_x, pixel_y), color_0)
        continue

      hit_inner = False
      for i in range(frame//12):
        case = in_which(p)

        if case == INNER:
          hit_inner = True
          image.putpixel((pixel_x, pixel_y), color_0)
          break

        # For these three cases, rescale the subdivided triangle to
        # original size and try again.
        if case == UPPER:
          p = ((p[0] - 0.25) * 2, (p[1] - (triangle_height / 2)) * 2)
        elif case == LOWER_LEFT:
          p = (p[0] * 2, p[1] * 2)
        elif case == LOWER_RIGHT:
          p = ((p[0] - 0.5) * 2, p[1] * 2)

      if not hit_inner:
        image.putpixel((pixel_x, pixel_y), color_1)

  image.save('frames/img{0:03d}.png'.format(frame), compress_level=1)
