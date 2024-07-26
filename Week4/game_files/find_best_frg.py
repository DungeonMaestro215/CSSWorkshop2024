import pygame
import random
import matplotlib.pyplot as plt
import numpy as np
import itertools

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

new_grass_chance = 0.02
new_rabbit_chance = 0.10
new_fox_chance = 0.02

simulation_speed = 1000

grasses = []
rabbits = []
foxes = []
grass_pop = [n_grasses]
rabbit_pop = [n_rabbits]
fox_pop = [n_foxes]
def reset_sim():
    grasses.clear()
    rabbits.clear()
    foxes.clear()

    grass_pop.clear()
    rabbit_pop.clear()
    fox_pop.clear()

    # Create grasses; [x, y]
    for i in range(n_grasses):
        grasses.append([get_random_x(), get_random_y(), max_grass_energy])

    # Create rabbits; [x, y, energy]
    for i in range(n_rabbits):
        rabbits.append([get_random_x(), get_random_y(), max_rabbit_energy])

    # Create foxes; [x, y, energy]
    for i in range(n_foxes):
        foxes.append([get_random_x(), get_random_y(), max_fox_energy])

# Functions to draw entities
def draw_grass(grasses):
    for grass in grasses:
        pygame.draw.rect(screen, "green", pygame.Rect(grass[0], grass[1], box_size, box_size))

def draw_rabbits(rabbits):
    for rabbit in rabbits:
        pygame.draw.rect(screen, "yellow", pygame.Rect(rabbit[0], rabbit[1], box_size, box_size))

def draw_foxes(foxes):
    for fox in foxes:
        pygame.draw.rect(screen, "red", pygame.Rect(fox[0], fox[1], box_size, box_size))

# Function to move a single rabbits/foxes randomly
def move_randomly(entity):
    direction = random.choice(["LEFT", "RIGHT", "UP", "DOWN"])
    if direction == "LEFT" and entity[0] > 0:
        entity[0] -= box_size
    elif direction == "RIGHT" and entity[0] < (num_boxes_x - 1) * box_size:
        entity[0] += box_size
    elif direction == "UP" and entity[1] > 0:
        entity[1] -= box_size
    elif direction == "DOWN" and entity[1] < (num_boxes_y - 1) * box_size:
        entity[1] += box_size

# Function to control all rabbits
def move_rabbits():
    for rabbit in rabbits:
        # Move and lose energy
        move_randomly(rabbit)
        rabbit[2] -= 1

        # Eat grass
        for grass in grasses:
            if rabbit[2] < max_rabbit_energy - grass[2] and rabbit[0] == grass[0] and rabbit[1] == grass[1]:
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
            if fox[2] < max_fox_energy - rabbit[2] and fox[0] == rabbit[0] and fox[1] == rabbit[1]:
                fox[2] = min(fox[2] + rabbit[2], max_fox_energy)
                rabbits.remove(rabbit)
                break

        if fox[2] <= 0:
            foxes.remove(fox)

        if random.random() < new_fox_chance and fox[2] > max_fox_energy / 2:
            foxes.append([get_random_x(), get_random_y(), max_fox_energy / 2])

# Main simulation loop
def run_sim():
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

        if len(grasses) == 0 or len(grasses) > 2000 or len(rabbits) == 0 or len(foxes) == 0:
            running = False
        elif len(fox_pop) > 1000:
            running = False
            print("Good run:")
            print(new_grass_chance)
            print(new_rabbit_chance)
            print(new_fox_chance)
            print()

        # Draw entities
        draw_grass(grasses)
        draw_rabbits(rabbits)
        draw_foxes(foxes)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(simulation_speed)



def main():
    global n_grasses, n_rabbits, n_foxes, max_grass_energy, max_rabbit_energy, max_fox_energy, new_grass_chance, new_rabbit_chance, new_fox_chance

    n_grasses_range = [150]
    n_rabbits_range = [25]
    n_foxes_range = [5] 
    max_grass_energy_range = np.arange(6, 20, 4)
    max_rabbit_energy_range = np.arange(10, 30, 5)
    max_fox_energy_range = np.arange(30, 50, 5)
    new_grass_chance_range = np.arange(0.01, 0.1, 0.02)
    new_rabbit_chance_range = np.arange(0.01, 0.1, 0.02)
    new_fox_chance_range = np.arange(0.01, 0.1, 0.02)
    options = list(itertools.product(n_grasses_range, n_rabbits_range, n_foxes_range, max_grass_energy_range, max_rabbit_energy_range, max_fox_energy_range, new_grass_chance_range, new_rabbit_chance_range, new_fox_chance_range))
    print(len(options))

    for option in options:
        n_grasses = option[0]
        n_rabbits = option[1]
        n_foxes = option[2]

        max_grass_energy = option[3]
        max_rabbit_energy = option[4]
        max_fox_energy = option[5]

        new_grass_chance = option[6]
        new_rabbit_chance = option[7]
        new_fox_chance = option[8]
        print(option)
        reset_sim()
        run_sim()


    pygame.quit()

if __name__ == "__main__":
    main()