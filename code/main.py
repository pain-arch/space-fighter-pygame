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
player_rect = player_surf.get_frect(topleft = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0 , WINDOW_HEIGHT)) for _ in range(20)] # Generate random positions for the stars


while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Draw the game
    display_surface.fill('darkgray') # BG color 
    for pos in star_positions:       # Draw the stars on the screen 
      display_surface.blit(star_surf, pos )# Draw the surface
        # Move t
    display_surface.blit(player_surf, player_rect) # Draw the player on the screen
    
   
    
    pygame.display.update() # Update the display
    

# Quit the game
pygame.quit() 