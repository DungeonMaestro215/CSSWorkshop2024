import pygame

pygame.init()

# Screen dimensions and grid size
screen_width = 1280
screen_height = 720

# Set up display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Drawing!")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

box_size = 30
# Remember: [x, y, energy]
grass = [60, 60, 8]
rabbit = [100, 100, 15]
fox = [60, 100, 40]

# Your drawing!
def draw():
    # Grass
    pygame.draw.rect(screen, "green", pygame.Rect(grass[0], grass[1], box_size, box_size))

    # Rabbit
    pygame.draw.rect(screen, "yellow", pygame.Rect(rabbit[0], rabbit[1], box_size, box_size))

    # Fox
    pygame.draw.rect(screen, "red", pygame.Rect(fox[0], fox[1], box_size, box_size))


# Display Drawing
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill("black")

        # Draw entities
        draw()

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()