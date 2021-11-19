import pygame
pygame.init()
from apple import Apple
from strawberry import Strawberry
from player import Player


screen = pygame.display.set_mode([500, 500])









# -------------------------------------------



# Make an instance of GameObject
apple = Apple()

# make instance of Player
player = Player()

# Making instance of strawberry
strawberry = Strawberry()

# Get the clock
clock = pygame.time.Clock()


# Create the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()
  # Clear screen
  screen.fill((255, 255, 255))
  # Draw apple
  apple.move()
  apple.render(screen)
  # Draw player 
  player.move()
  player.render(screen)
  # Drawing stawberry
  strawberry.move()
  strawberry.render(screen)
  # Update the window
  pygame.display.flip()

  # tick the clock!
  clock.tick(30)

