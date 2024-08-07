import pygame
import random
import matplotlib.pyplot as plt

# Initialize Pygame
pygame.init()

# Screen dimensions and grid size
screen_width = 1280
screen_height = 720
box_size = 30
num_boxes_x = screen_width // box_size
num_boxes_y = screen_height // box_size

# Set up display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fox, Rabbit, Grass Simulation")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# functions to generate a random position on the grid
def get_random_x():
    return random.randint(0, num_boxes_x - 1) * box_size
def get_random_y():
    return random.randint(0, num_boxes_y - 1) * box_size

# Simulation parameters
n_grasses = 200
n_rabbits = 25
n_foxes = 5

max_grass_energy = 8
max_rabbit_energy = 20
max_fox_energy = 40

new_grass_chance = 0.04
new_rabbit_chance = 0.20
new_fox_chance = 0.10

simulation_speed = 5

# Create grasses; [x, y, energy]
grasses = []
for i in range(n_grasses):
    grasses.append([get_random_x(), get_random_y(), max_grass_energy])

# Create rabbits; [x, y, energy]
rabbits = []
for i in range(n_rabbits):
    rabbits.append([get_random_x(), get_random_y(), max_rabbit_energy])

# Create foxes; [x, y, energy]
foxes = []
for i in range(n_foxes):
    foxes.append([get_random_x(), get_random_y(), max_fox_energy])

# Functions to draw entities
def draw_grass(grasses):
    for grass in grasses:
        pygame.draw.rect(screen, "green", pygame.Rect(grass[0], grass[1], box_size, box_size))

def draw_rabbits(rabbits):
    for rabbit in rabbits:
        pygame.draw.rect(screen, "yellow", pygame.Rect(rabbit[0], rabbit[1], box_size, box_size))
        pygame.draw.rect(screen, "yellow", pygame.Rect(rabbit[0], rabbit[1], box_size, box_size))

def draw_foxes(foxes):
    for fox in foxes:
        pygame.draw.rect(screen, "red", pygame.Rect(fox[0], fox[1], box_size, box_size))

# Function to move a single rabbits/foxes randomly
def move_randomly(animal):
    direction = random.choice(["LEFT", "RIGHT", "UP", "DOWN"])
    if direction == "LEFT" and animal[0] > 0:
        animal[0] -= box_size
    elif direction == "RIGHT" and animal[0] < (num_boxes_x - 1) * box_size:
        animal[0] += box_size
    elif direction == "UP" and animal[1] > 0:
        animal[1] -= box_size
    elif direction == "DOWN" and animal[1] < (num_boxes_y - 1) * box_size:
        animal[1] += box_size

# Function to control all rabbits
def move_rabbits():
    for rabbit in rabbits:
        # Move and lose energy
        move_randomly(rabbit)
        rabbit[2] -= 1

        # Eat grass
        for grass in grasses:
            if rabbit[0] == grass[0] and rabbit[1] == grass[1]:
                rabbit[2] = min(rabbit[2] + grass[2], max_rabbit_energy)
                grasses.remove(grass)
                break

        if rabbit[2] <= 0:
            rabbits.remove(rabbit)

        if random.random() < new_rabbit_chance and rabbit[2] > max_rabbit_energy / 2:
            rabbits.append([get_random_x(), get_random_y(), max_rabbit_energy / 2])

# Function to control all foxes
def move_foxes():
    for fox in foxes:
        # Move and lose energy
        move_randomly(fox)
        fox[2] -= 1

        # Eat rabbit
        for rabbit in rabbits:
            if fox[0] == rabbit[0] and fox[1] == rabbit[1]:
                fox[2] = min(fox[2] + rabbit[2], max_fox_energy)
                rabbits.remove(rabbit)
                break

        if fox[2] <= 0:
            foxes.remove(fox)

        if random.random() < new_fox_chance and fox[2] > max_fox_energy / 2:
            foxes.append([get_random_x(), get_random_y(), max_fox_energy / 2])

# Main simulation loop
grass_pop = [n_grasses]
rabbit_pop = [n_rabbits]
fox_pop = [n_foxes]
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill("black")

        # Move rabbits and foxes
        move_rabbits()
        move_foxes()

        # Grow grass randomly
        for grass in grasses:
            if random.random() < new_grass_chance:
                grasses.append([get_random_x(), get_random_y(), max_grass_energy])

        # Keep track of populations over time
        grass_pop.append(len(grasses))
        rabbit_pop.append(len(rabbits))
        fox_pop.append(len(foxes))

        # Draw entities
        draw_grass(grasses)
        draw_rabbits(rabbits)
        draw_foxes(foxes)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(simulation_speed)

    pygame.quit()


    # Plots
    plt.plot(grass_pop, 'g-', label="grasses")
    plt.plot(rabbit_pop, 'y-', label="rabbits")
    plt.plot(fox_pop, 'r-', label="foxes")

    plt.title("Fox, Rabbit, and Grass Population over Time")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()