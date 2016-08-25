"""
Geometric inversion maps each point P_1 on a plane to another point P_2 on the plane that is
an "inverse" of the first point with respect to some reference circle with center O such that
OP_1 * OP_2 = R^2 where OP_x is the distance from the center of the reference circle to point
P_x and R is the radius of the reference circle.

For this visualization, we will assume that the reference circle is at the origin (0,0).
"""

from PIL import Image
from math import sqrt

width, height = (1280, 720)
radius = 100
frames = 300

# Store the intermediate results in a buffer.
buffer = [[(0,0,0) for y in range(height)] for x in range(width)]

def invert(x, y):
  """Calculate the inverse of a point at x and y and return the point as a tuple."""
  distance_from_origin = sqrt(x*x+y*y)
  new_distance = radius*radius/distance_from_origin
  factor = new_distance/distance_from_origin
  
  return (x*factor, y*factor)

for frame in range(frames):
  # Animate the radius up to 90.
  radius = min(90, 10 + frame)
  
  for pixel_y in range(height):
    y = pixel_y - int(height/2)
    for pixel_x in range(width):
      x = pixel_x - int(width/2)
      
      # The origin is mapped to a point at infinity so it does not make sense to invert it.
      if (x, y) == (0,0):
        continue
        
      (inv_x, inv_y) = invert(x, y)
      
      buffer[pixel_x][pixel_y] = (0,0,0)
      
      # Animate the grid by translating it diagonally.
      square_x = int(((inv_x+frame*0.5)/10)%2)
      square_y = int(((inv_y+frame*0.5)/10)%2)
      
      if (square_x + square_y)%2 == 1:
        buffer[pixel_x][pixel_y] = (191+64*square_x, 64+120*square_y, 100+20*square_y)
    
  # Output the image.
  image = Image.new('RGB', (width, height))
  for x in range(width):
    for y in range(height):
      image.putpixel((x, y), buffer[x][y])
  image.save('frames/img{0:03d}.png'.format(frame))
