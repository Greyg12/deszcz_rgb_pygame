import pygame
import random

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Define the number of raindrops to simulate
num_raindrops = 100

# Define raindrop speed range
raindrop_speed = 1

# Define raindrop colors
raindrop_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (127,127,9)]

class Raindrop:
    def __init__(self):
        # Initialize raindrop position randomly
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)

        # Set raindrop speed
        self.speed = raindrop_speed

        # Choose a random raindrop color
        self.color = random.choice(raindrop_colors)

    def fall(self):
        # Update the raindrop's y-position based on its speed
        self.y += self.speed

        # If the raindrop falls below the screen, reset its position
        if self.y > screen_height:
            self.y = 0
            self.x = random.randint(0, screen_width)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a background color (optional)
    screen.fill((0, 0, 0))  # Black background

    # Create and manage raindrops
    raindrops = []  # List to store raindrop objects
    for _ in range(num_raindrops):
        raindrops.append(Raindrop())

    # Draw and update each raindrop
    for raindrop in raindrops:
        pygame.draw.line(screen, raindrop.color, (raindrop.x, raindrop.y), (raindrop.x, raindrop.y + 5), 2)  # Draw a line
        raindrop.fall()

    pygame.display.flip()

pygame.quit()