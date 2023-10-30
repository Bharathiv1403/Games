import pygame as py
import sys

py.init()

WIDTH, HEIGHT = 1200,800
BACKGROUND_COLOR = (0, 150, 0)  # Green background
BALL_COLOR = (250, 250, 250)    # White cricket ball
BALL_RADIUS = 17

# Create the screen
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Cricket Anime")

# Main game loop
running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    # Fill the background
    screen.fill(BACKGROUND_COLOR)

    # Draw the cricket ball
    py.draw.circle(screen, BALL_COLOR, (WIDTH // 2, HEIGHT // 2), BALL_RADIUS)

    py.display.flip()

# Quit Pygame
py.quit()
sys.exit()
