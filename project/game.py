"""
#Let’s do some kind of FPS with an inbuilt engine designed to draw onto the screen and
#calculate which 3d object should be on said screen with ray casting and tracing
#for shadows and just for fun we can make the code extra complicated
#don’t forget to optimize as much as possible because python is slow
#finally, don’t forget to start simple and once it works, start making it more
#complex, I’ll make the textures, just tell me once you want to create one.

alr come here
import pygame
pygame.init()
pygame.display.init()

RESOLUTION = 0.0001

screen = pygame.display.set_mode(1000, 1000)

class Engine:
    def __init__(self, objects, camera):
        self.objects = objects
        #we can make object types like whether an object is a light or not
        self.camera = camera
        #camera will be the position of the camera and where we will begin ray casting.
    def raycast(self, resolution):
        #we require an angle to start this ray casting at, theta = 0 
        #we can increment a theta to start said ray casting and set another angle to increment y
        #angles for ray casting.
        for i in self.objects:
            #objects will be a list of the objects in the game and their positions.
            #now we can basically draw
            #we could make it more complex by only finding corners, and makes it easier
            #to put in textures, but you can make it simpler by just doing basic ray tracing first.
          theta += resolution
 

"""
'''
import pygame
import numpy as np
import math

# Initialize Pygame
pygame.init()

# Set screen size
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
black = (0,0,0)
# Define the scene
# Example: A circle with center (400, 300) and radius 100
circle_center = (0, 0, 100)
circle_radius = 50
camera = (0, 0, 0)
light = (0, 0, 0)
# Cast rays for each pixel
for x in range(0,screen_size[0],2):
    for y in range(0,screen_size[1],2):
        # Calculate intersection point with circle
        dist = math.sqrt((x - circle_center[0])**2 + (y - circle_center[1])**2)
        if dist <= circle_radius:
            # Ray intersects with circle

            # Determine shading based on distance from center
            shading = (circle_radius - dist) / circle_radius
            diffuse_color = int(shading * 255)

            # Draw pixel
            color = (diffuse_color, diffuse_color, diffuse_color)
            screen.set_at((x, y), color)

# Render scene
pygame.display.flip()

# Wait for user to close the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    if(key[pygame.K_UP]):
        screen.fill(black)
        circle_center = (circle_center[0] , circle_center[1] - 5)
        print(circle_center)
    if(key[pygame.K_DOWN]):
        screen.fill(black)
        circle_center = (circle_center[0] , circle_center[1] + 5)
        print(circle_center)
    if(key[pygame.K_RIGHT]):
        screen.fill(black)
        circle_center = (circle_center[0] + 5, circle_center[1] + 0)
        print(circle_center)
    if(key[pygame.K_LEFT]):
        screen.fill(black)
        circle_center = (circle_center[0] - 5, circle_center[1] + 0)
        print(circle_center)
    for x in range(0,screen_size[0],2):
        for y in range(0,screen_size[1],2):
            # Calculate intersection point with circle
            dist = math.sqrt((x - circle_center[0])**2 + (y - circle_center[1])**2)
            if dist <= circle_radius:
                        # Ray intersects with circle

                        # Determine shading based on distance from center
                shading = (circle_radius - dist) / circle_radius
                diffuse_color = int(shading * 255)

                        # Draw pixel
                color = (diffuse_color, diffuse_color, diffuse_color)
                screen.set_at((x, y), color)

            # Render scene
    pygame.display.flip()
print("HELLO")
# Clean up
pygame.quit()
'''
'''
import pygame
import math
import numpy as np

# Initialize Pygame
pygame.init()

# Set screen size
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)

# Define the scene
# Example: A sphere with center (400, 300, 100) and radius 100
sphere_center = (400, 300, 100)
sphere_radius = 100

# Cast rays for each pixel
for x in range(0, screen_size[0] + 1, 2):
    for y in range(0, screen_size[1] + 1, 2):
        # Calculate ray direction
        ray_dir = (x - screen_size[0]/2, y - screen_size[1]/2, screen_size[0]/2)
        ray_dir = ray_dir / np.linalg.norm(ray_dir)

        # Calculate intersection point with sphere
        a = ray_dir[0]**2 + ray_dir[1]**2 + ray_dir[2]**2
        b = 2 * (ray_dir[0] * (x - sphere_center[0]) + ray_dir[1] * (y - sphere_center[1]) + ray_dir[2] * (0 - sphere_center[2]))
        c = (x - sphere_center[0])**2 + (y - sphere_center[1])**2 + (0 - sphere_center[2])**2 - sphere_radius**2
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            # Ray intersects with sphere
            t = (-b - math.sqrt(discriminant)) / (2 * a)
            intersection_point = (x + t * ray_dir[0], y + t * ray_dir[1], t * ray_dir[2])

            # Determine shading based on intersection point
            # Example: Diffuse shading based on dot product of light direction and normal
            light_dir = (1, 1, 1)
            light_dir = light_dir / np.linalg.norm(light_dir)
            normal = (intersection_point[0] - sphere_center[0], intersection_point[1] - sphere_center[1], intersection_point[2] - sphere_center[2])
            normal = normal / np.linalg.norm(normal)
            diffuse_shading = max(0, light_dir[0] * normal[0] + light_dir[1] * normal[1] + light_dir[2] * normal[2])
            diffuse_color = int(diffuse_shading * 255)

            # Draw pixel
            color = (diffuse_color, diffuse_color, diffuse_color)
            screen.set_at((x, y), color)

# Render scene
pygame.display.flip()

# Wait for user to close the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Clean up
pygame.quit()
'''
import numpy as np
import pygame
from matplotlib import pyplot as plt
pygame.init()
map = [[1, 1, 1, 1, 1, 1, 1], 
       [1, 0, 1, 0, 0, 0, 1],
       [1, 0, 1, 1, 1, 0, 1], 
       [1, 0, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1]]
#PI shortcut
pi = np.pi
#camera position and angle
cx, cy = (1, 1)
exitx, exity = (1,3)
rot = pi / 4
while True:
  for i in range(60):
    #index in player FOV
    roti = rot + np.deg2rad(
      i - 30)  #SUBRACT BY HALF OF RANGE OR ELSE IT BREAKS!!!!!
    #Initial ray pos
    x, y = (cx, cy)
    #Sin and Cos functions to determine ray length
    sin, cos = (
      0.02 * np.sin(roti), 0.02 * np.cos(roti)
    )  #multiply by 2/100 to decrease increment size to prevent pass throughs
    n = 0
    while True:
      #updating ray size and direction
      x, y = (x + cos, y + sin)
      n = n + 1
      if map[int(x)][int(y)] != 0:
        h = 1 / (n * 0.02)
        break
    plt.vlines(i, -h/2, h/2, lw=8)
  plt.axis("off")
  plt.tight_layout()
  plt.axis([0, 60, -1, 1])
  plt.draw()
  plt.pause(0.0001)
  plt.clf()
  x, y = (cx, cy)
  for event in pygame.event.get():
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        x, y = (x + 0.3*np.cos (rot), y + 0.3*np.sin (rot) )
    elif key[pygame.K_DOWN]:
        x, y = (x - 0.3*np.cos (rot) , y - 0.3*np.sin(rot) )
    elif key[pygame.K_LEFT]:
        rot = rot - np.pi/12
    elif key[pygame.K_RIGHT]:
        rot = rot + np.pi/12
    elif key[pygame.K_ESCAPE]:
        break
  if map [int (x)] [int (y) ] == 0:
    
    if int(cx) == exitx and int(cy) == exity:
      break
    cx, cy = (x,y)
  
plt.close()
