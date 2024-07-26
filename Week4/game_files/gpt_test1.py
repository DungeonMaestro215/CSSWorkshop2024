import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and grid size
screen_width = 800
screen_height = 600
box_size = 20
num_boxes_x = screen_width // box_size
num_boxes_y = screen_height // box_size

# Colors
colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'green': (0, 255, 0),
    'yellow': (255, 255, 0),
    'red': (255, 0, 0),
    'blue': (0, 0, 255)
}

# Set up display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Fox, Rabbit, Grass Simulation')

# Clock for controlling the frame rate
clock = pygame.time.Clock()
simulation_speed = 50

# Function to generate a random position on the grid
def get_random_position():
    return {'x': random.randint(0, num_boxes_x - 1) * box_size,
            'y': random.randint(0, num_boxes_y - 1) * box_size}

# Lists to store entities
grasses = [get_random_position() for _ in range(200)]
rabbits = [{'position': get_random_position(), 'energy': 10} for _ in range(30)]
foxes = [{'position': get_random_position(), 'energy': 50} for _ in range(10)]

# Functions to draw entities
def draw_grass(grasses):
    for grass in grasses:
        pygame.draw.rect(screen, colors['green'], pygame.Rect(grass['x'], grass['y'], box_size, box_size))

def draw_rabbits(rabbits):
    for rabbit in rabbits:
        pygame.draw.rect(screen, colors['yellow'], pygame.Rect(rabbit['position']['x'], rabbit['position']['y'], box_size, box_size))

def draw_foxes(foxes):
    for fox in foxes:
        pygame.draw.rect(screen, colors['red'], pygame.Rect(fox['position']['x'], fox['position']['y'], box_size, box_size))

# Function to move entities randomly
def move_randomly(entity):
    direction = random.choice(['LEFT', 'RIGHT', 'UP', 'DOWN'])
    if direction == 'LEFT' and entity['position']['x'] > 0:
        entity['position']['x'] -= box_size
    elif direction == 'RIGHT' and entity['position']['x'] < (num_boxes_x - 1) * box_size:
        entity['position']['x'] += box_size
    elif direction == 'UP' and entity['position']['y'] > 0:
        entity['position']['y'] -= box_size
    elif direction == 'DOWN' and entity['position']['y'] < (num_boxes_y - 1) * box_size:
        entity['position']['y'] += box_size

# Main simulation loop
def main():
    global grasses, rabbits, foxes
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill(colors['black'])

        # Move rabbits and foxes
        for rabbit in rabbits[:]:
            move_randomly(rabbit)
            rabbit['energy'] -= 1
            for grass in grasses[:]:
                if rabbit['position']['x'] == grass['x'] and rabbit['position']['y'] == grass['y']:
                    rabbit['energy'] = min(rabbit['energy'] + 10, 20)
                    grasses.remove(grass)
                    break
            if rabbit['energy'] <= 0:
                rabbits.remove(rabbit)
            if random.random() < 0.02 and rabbit['energy'] >= 15:  # Rabbit needs energy from at least 1.5 grasses
                rabbits.append({'position': get_random_position(), 'energy': 10})

        for fox in foxes[:]:
            move_randomly(fox)
            fox['energy'] -= 1
            for rabbit in rabbits[:]:
                if fox['position']['x'] == rabbit['position']['x'] and fox['position']['y'] == rabbit['position']['y']:
                    fox['energy'] = min(fox['energy'] + 20, 50)  # Reduce energy gain from rabbits
                    rabbits.remove(rabbit)
                    break
            if fox['energy'] <= 0:
                foxes.remove(fox)
            if random.random() < 0.02 and fox['energy'] > 35:  # Adjust fox reproduction rate
                foxes.append({'position': get_random_position(), 'energy': 50})

        # Grow multiple grass patches randomly
        for _ in range(7):  # Spawn 7 grass patches per loop
            if random.random() < 0.8:  # Increase grass growth rate
                grasses.append(get_random_position())

        # Draw entities
        draw_grass(grasses)
        draw_rabbits(rabbits)
        draw_foxes(foxes)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(simulation_speed)

    pygame.quit()

if __name__ == '__main__':
    main()
