"""
Game of Life rules:
  1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
  2. Any live cell with two or three live neighbours lives on to the next generation.
  3. Any live cell with more than three live neighbours dies, as if by over-population.
  4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""

from PIL import Image
from random import randint

grid_width, grid_height = (160, 90)
pixel_size = 8
frame_count = 160

# Initialize the grid with a random set of ones and zeroes. The initial image will be
# different each time.
grid = [[randint(0,1) for y in range(grid_height)] for x in range(grid_width)]

# We need another grid so we do not interfere with the existing grid during updates.
buffer_grid = [[0 for y in range(grid_height)] for x in range(grid_width)]

for frame in range(frame_count):
  # Generate the next image.
  for x in range(grid_width):
    for y in range(grid_height):
      x_left = (x-1) % grid_width
      x_right = (x+1) % grid_width
      y_up = (y-1) % grid_height
      y_down = (y+1) % grid_height

      alive_neighbors = 0

      for point in [
          (x_left, y_up), (x, y_up), (x_right, y_up),
          (x_left, y), (x_right, y),
          (x_left, y_down), (x, y_down), (x_right, y_down)
        ]:
        if grid[point[0]][point[1]] == 1:
          alive_neighbors += 1

      # Use the game rules to figure out of the pixel should be dead (=0) or alive(=1) in the
      # next frame.
      if grid[x][y] == 1:
        if alive_neighbors < 2: # Rule #1
          buffer_grid[x][y] = 0
        elif alive_neighbors > 3: # Rule #3
          buffer_grid[x][y] = 0
        else: # Rule #2
          buffer_grid[x][y] = 1

      if grid[x][y] == 0:
        if alive_neighbors == 3: # Rule #4
          buffer_grid[x][y] = 1
        else:
          buffer_grid[x][y] = 0

  # Swap the two buffers.
  buffer_grid, grid = (grid, buffer_grid)

  # Output the image.
  image = Image.new('RGB', (grid_width*pixel_size, grid_height*pixel_size))
  for x in range(grid_width):
    for y in range(grid_height):
      for offset_x in range(pixel_size):
        for offset_y in range(pixel_size):
          if grid[x][y] == 1:
            image.putpixel((x*pixel_size+offset_x, y*pixel_size+offset_y), (0,0,0))
          else:
            image.putpixel((x*pixel_size+offset_x, y*pixel_size+offset_y), (255, 255, 255))
  image.save('frames/img{0:03d}.png'.format(frame))


