import pygame
import numpy as np
import math

# Initialize Pygame
pygame.init()

# Set screen size
screen_size = (1024, 1024)
screen = pygame.display.set_mode(screen_size)
black = (0,0,0)
# Define the scene
# Example: A circle with center (400, 300) and radius 100
circle_center = (512, 512)
circle_radius = 50

# Cast rays for each pixel
for x in range(0,screen_size[0],3):
    for y in range(0,screen_size[1],3):
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
    if(key[pygame.K_DOWN]):
        screen.fill(black)
        circle_center = (circle_center[0] , circle_center[1] + 5)
        print(circle_center)
    if(key[pygame.K_RIGHT]):
        screen.fill(black)
        circle_center = (circle_center[0] + 5, circle_center[1] + 0)
    if(key[pygame.K_LEFT]):
        screen.fill(black)
        circle_center = (circle_center[0] - 5, circle_center[1] + 0)
    for x in range(0,screen_size[0],3):
        for y in range(0,screen_size[1],3):
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
print("Bello")
# Clean up
pygame.quit()