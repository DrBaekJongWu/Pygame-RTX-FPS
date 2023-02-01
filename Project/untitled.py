import pygame
import numpy as np
import math

# Initialize Pygame
pygame.init()

# Set screen size
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
black = (0,0,0)
# Define the scene
# Example: A circle with center (400, 300) and radius 100
circle_center = (400, 300)
circle_radius = 100

# Cast rays for each pixel
for x in range(screen_size[0]):
    for y in range(screen_size[1]):
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
        circle_center = (400, circle_center[1] + 1)
        print(circle_center)
        for x in range(screen_size[0]):
            for y in range(screen_size[1]):
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

# Clean up
pygame.quit()
