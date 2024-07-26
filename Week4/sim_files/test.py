import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Grass, Rabbit, and Fox Drawing")

# Colors
GREEN = (34, 139, 34)
BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
DARK_ORANGE = (255, 140, 0)

# Draw functions
def draw_grass(surface, center, box_size):
    x, y = center
    width = box_size
    height = box_size // 2

    pygame.draw.rect(surface, GREEN, (x - width // 2, y - height // 2, width, height))
    pygame.draw.line(surface, GREEN, (x, y - height // 2), (x, y - height), 5)
    pygame.draw.line(surface, GREEN, (x - width // 4, y - height // 2), (x - width // 4, y - height), 5)
    pygame.draw.line(surface, GREEN, (x + width // 4, y - height // 2), (x + width // 4, y - height), 5)

def draw_rabbit(surface, center, box_size):
    x, y = center
    body_width = box_size // 2
    body_height = box_size // 3
    ear_width = body_width // 4
    ear_height = body_height // 2
    eye_radius = ear_width // 2

    pygame.draw.ellipse(surface, WHITE, (x - body_width // 2, y - body_height // 2, body_width, body_height))
    pygame.draw.rect(surface, WHITE, (x - ear_width, y - body_height - ear_height, ear_width, ear_height))
    pygame.draw.rect(surface, WHITE, (x, y - body_height - ear_height, ear_width, ear_height))
    pygame.draw.circle(surface, BLACK, (x - ear_width // 2, y - body_height // 4), eye_radius)
    pygame.draw.circle(surface, BLACK, (x + ear_width // 2, y - body_height // 4), eye_radius)

def draw_fox(surface, center, box_size):
    x, y = center
    body_width = box_size // 2
    body_height = box_size // 3
    ear_width = body_width // 4
    ear_height = body_height // 2
    eye_radius = ear_width // 3
    tail_length = body_width // 2

    pygame.draw.ellipse(surface, ORANGE, (x - body_width // 2, y - body_height // 2, body_width, body_height))
    pygame.draw.polygon(surface, ORANGE, [(x - body_width // 2, y), (x - body_width // 2 - tail_length, y), (x - body_width // 2, y - body_height // 4)])
    pygame.draw.polygon(surface, DARK_ORANGE, [(x - ear_width, y - body_height // 2), (x - ear_width - ear_width, y - body_height - ear_height), (x - ear_width + ear_width // 2, y - body_height - ear_height)])
    pygame.draw.polygon(surface, DARK_ORANGE, [(x + ear_width, y - body_height // 2), (x + ear_width + ear_width, y - body_height - ear_height), (x + ear_width - ear_width // 2, y - body_height - ear_height)])
    pygame.draw.circle(surface, BLACK, (x - ear_width // 2, y - body_height // 4), eye_radius)
    pygame.draw.circle(surface, BLACK, (x + ear_width // 2, y - body_height // 4), eye_radius)

def main():
    clock = pygame.time.Clock()
    box_size = 100  # Size parameter for the drawings
    grass_center = (200, 300)
    rabbit_center = (400, 300)
    fox_center = (600, 300)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(GRAY)
        
        draw_grass(screen, grass_center, box_size)
        draw_rabbit(screen, rabbit_center, box_size)
        draw_fox(screen, fox_center, box_size)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
