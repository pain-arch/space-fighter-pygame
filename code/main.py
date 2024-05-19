import pygame

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

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Draw the game
    display_surface.fill('gray') # Fill the screen with red
    x += 1 # Move the surface to the right
    display_surface.blit(surf, (x, 150))
    pygame.display.update() # Update the display
    

# Quit the game
pygame.quit() 