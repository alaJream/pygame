# Import and initialize pygame
import pygame
import board
from board import screen, highscore, clock, score
import sprites 
from sprites import Apple, Strawberry, Bomb, Player



apple=Apple()
strawberry=Strawberry()
player=Player()
bomb=Bomb()
# Make a group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)
# make a fruits Group
fruit_sprites = pygame.sprite.Group()
fruit_sprites.add(apple)
fruit_sprites.add(strawberry)


# Create the game loop
running = True
while running:
    
    # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check for event type KEYBOARD
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                print('LEFT')
                player.left()
            elif event.key == pygame.K_RIGHT:
                print('RIGHT')
                player.right()
            elif event.key == pygame.K_UP:
                print('UP')
                player.up()
            elif event.key == pygame.K_DOWN:
                print('DOWN')
                player.down()
        elif event.type == pygame.MOUSEBUTTONUP:
            pygame.event.set_allowed(pygame.KEYDOWN)
            sprites.positive_move = board.positive_move
            sprites.negative_move = board.negative_move
            score = 0
            for entity in all_sprites:
                entity.reset()
                

    # Clear screen
    screen.fill((255, 255, 255))

    # Move and render Sprites
    for entity in all_sprites:
	    entity.move()
	    entity.render(screen)

    # Check for collisions
    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        fruit.reset()
        sprites.positive_move += 0.2
        sprites.negative_move += 0.2
        
        score += 1
        if score > highscore:
            highscore = score
              
    if pygame.sprite.collide_rect(player, bomb):
        for entity in all_sprites:
            if entity == player:
                pass
            else:
                entity.dx = 0
                entity.dy = 0

        pygame.event.set_blocked(pygame.KEYDOWN)

    # Update the window
    pygame.display.flip()
    # tick the clock!
    clock.tick(60)