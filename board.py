import pygame
pygame.init

lanes = [93, 218, 343]
screen = pygame.display.set_mode([500, 500])
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

center = SCREEN_WIDTH / 2
middle = center - 32
left = center / 2 - 25
right =  SCREEN_WIDTH - (center / 2) - 25
x_lanes = [left, middle, right]

center_horizontal = SCREEN_HEIGHT / 2
center_horizontal_lane = center_horizontal - 32
top = center_horizontal / 2 - 25
bottom = SCREEN_HEIGHT - (center_horizontal / 2) - 25
y_lanes = [top, center_horizontal_lane, bottom]

speed_increase_value = 0.1