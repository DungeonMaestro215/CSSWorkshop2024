import pygame

# Global game variables
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

def main():
    # Initialize Pygame
    pygame.init()

    # Set up screen
    pygame.display.set_caption("Test Game!")

    # Clock for controlling timing
    clock = pygame.time.Clock()

    # Start game loop
    running = True
    while running:
        # If the 'X' button is pressed...
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen for the next frame
        screen.fill("purple")

        ### Game rendering here ###

        ###########################

        # 'Flip' display to show our scene
        pygame.display.flip()

        # Runs at 60 fps
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()