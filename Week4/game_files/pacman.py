import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and grid size
screen_width = 400
screen_height = 400
box_size = 20
num_boxes = screen_width // box_size

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pacman Game')

# Clock for controlling the frame rate
clock = pygame.time.Clock()
pacman_speed = 10

# Initial pacman position and direction
pacman = {'x': 10 * box_size, 'y': 10 * box_size}
direction = 'RIGHT'

# Generate pellets (food)
num_pellets = 30
pellets = []
for _ in range(num_pellets):
    pellet = {
        'x': random.randint(0, num_boxes - 1) * box_size,
        'y': random.randint(0, num_boxes - 1) * box_size
    }
    pellets.append(pellet)

def draw_pacman(pacman):
    pygame.draw.circle(screen, yellow, (pacman['x'] + box_size // 2, pacman['y'] + box_size // 2), box_size // 2)

def draw_pellets(pellets):
    for pellet in pellets:
        pygame.draw.circle(screen, white, (pellet['x'] + box_size // 2, pellet['y'] + box_size // 2), box_size // 4)

def move_pacman(direction, pacman):
    if direction == 'LEFT':
        pacman['x'] -= box_size
    elif direction == 'RIGHT':
        pacman['x'] += box_size
    elif direction == 'UP':
        pacman['y'] -= box_size
    elif direction == 'DOWN':
        pacman['y'] += box_size

def check_collision(pacman, pellets):
    for pellet in pellets:
        if pacman['x'] == pellet['x'] and pacman['y'] == pellet['y']:
            pellets.remove(pellet)
            return True
    return False

def check_wall_collision(pacman):
    if pacman['x'] < 0 or pacman['x'] >= screen_width or pacman['y'] < 0 or pacman['y'] >= screen_height:
        return True
    return False

def game_over_screen():
    font = pygame.font.SysFont('arial', 50)
    text = font.render('Game Over', True, red)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)

def main():
    global direction
    running = True
    score = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'

        screen.fill(black)
        move_pacman(direction, pacman)

        if check_wall_collision(pacman):
            game_over_screen()
            running = False

        if check_collision(pacman, pellets):
            score += 1

        draw_pacman(pacman)
        draw_pellets(pellets)
        pygame.display.flip()
        clock.tick(pacman_speed)

    pygame.quit()

if __name__ == '__main__':
    main()
