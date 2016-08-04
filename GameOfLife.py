import pygame
import time

pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 200,   0,   0)
GREY     = ( 170, 170, 170)

size = (800, 640)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game of Life v0.1")

done = False

# Timing
clock = pygame.time.Clock()
fps = 60

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("hej doe")
            done = True

        # Game logic goes here

        # First, clear the screen (no drawing commands above this)
        screen.fill(GREY)

        # Drawing goes here
        pygame.draw.rect(screen, RED, [50, 50, 50, 50], 3)

        # Update
        pygame.display.flip()

        # fps
        clock.tick(fps)

pygame.quit()