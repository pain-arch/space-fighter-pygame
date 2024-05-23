import pygame
from os.path import join
from random import randint

# Initialize the game
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Fighter Game') # Set the window title
running = True

# surface
surf = pygame.Surface((100, 200))
surf.fill('orange')
x = 100 # x position of the surface


# imports the player and star images
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = 1 # 1: right, -1: left, 0: no movement  

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0 , WINDOW_HEIGHT)) for _ in range(20)] # Generate random positions for the stars

meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

leaser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
leaser_rect = leaser_surf.get_rect(bottomleft = (20, WINDOW_HEIGHT - 20))


while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Draw the game
    display_surface.fill('darkgray') # BG color 
    for pos in star_positions:       # Draw the stars on the screen 
      display_surface.blit(star_surf, pos )# Draw the surface
      
    display_surface.blit(meteor_surf, meteor_rect) # Draw the meteor on the screen
    display_surface.blit(leaser_surf, leaser_rect) # Draw the leaser on the screen  
    
    # Player movement
    player_rect.x += player_direction * 0.4

    if player_rect.right > WINDOW_WIDTH or player_direction < 0:
       player_rect.left *= -1


    display_surface.blit(player_surf, player_rect) # Draw the player on the screen
    pygame.display.update() # Update the display
    

# Quit the game
pygame.quit() 