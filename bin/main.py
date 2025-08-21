import pygame

def main():
    pygame.init()
    
    # Set up the display
    width, height = 1920, 1080
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("My Pygame Window")
    
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill the screen with a color
        screen.fill((0, 0, 0))  # Black background
        
        # Update the display
        pygame.display.flip()
    
    pygame.quit()