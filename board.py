# constants.py
import pygame
from random import randint

# Get the clock
clock = pygame.time.Clock()

# Configure the screen
screen = pygame.display.set_mode([500, 500])
lanes = [93, 218, 343]
positive_move = (randint(0, 200) / 100) + 1
negative_move = ((randint(0, 200) / 100) + 1) * -1

#text
score = 0
highscore = 0