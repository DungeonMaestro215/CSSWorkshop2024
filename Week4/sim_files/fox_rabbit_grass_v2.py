import pygame
import random
import matplotlib.pyplot as plt

seed = random.randint(1000, 5000)
print(f"Seed: {seed}")
random.seed(seed)


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

new_grass_chance = 0.02 * n_grasses
new_rabbit_chance = 0.20 * n_rabbits
new_fox_chance = 0.05 * n_foxes

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

# Function to move a single animal toward its nearest food source
def move_nearest(animal, food_sources):
    direction = random.choice(["LEFT", "RIGHT", "UP", "DOWN"])
    if len(food_sources) > 0:
        # Find nearest source of food
        nearest_food_source = food_sources[0]
        nearest_distance = abs(animal[0] - nearest_food_source[0]) + abs(animal[1] - nearest_food_source[1])
        for food_source in food_sources:
            distance = abs(animal[0] - food_source[0]) + abs(animal[1] - food_source[1])
            if distance < nearest_distance:
                nearest_food_source = food_source
                nearest_distance = distance
        
        # Move toward nearest source
        distance_x = animal[0] - nearest_food_source[0]
        distance_y = animal[1] - nearest_food_source[1]
        if abs(distance_x) > abs(distance_y):
            if distance_x > 0:
                direction = "LEFT"
            else:
                direction = "RIGHT"
        else:
            if distance_y > 0:
                direction = "UP"
            else:
                direction = "DOWN"

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
        # move_nearest(rabbit, grasses)
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

        if random.random() < new_rabbit_chance / (len(rabbits) + 1) and rabbit[2] > max_rabbit_energy / 2:
            rabbits.append([get_random_x(), get_random_y(), max_rabbit_energy / 2])

# Function to control all foxes
def move_foxes():
    for fox in foxes:
        # Move and lose energy
        # move_nearest(fox, rabbits)
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

        if random.random() < new_fox_chance / (len(foxes) + 1) and fox[2] > max_fox_energy / 2:
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
            if random.random() < new_grass_chance / (len(grasses) + 1):
                grasses.append([get_random_x(), get_random_y(), max_grass_energy])

        # Keep track of populations over time
        grass_pop.append(len(grasses))
        rabbit_pop.append(len(rabbits))
        fox_pop.append(len(foxes))

        if len(rabbits) == 0:
            running = False


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

    # plt.plot(grass_pop, rabbit_pop, 'g-')
    # plt.plot(rabbit_pop, fox_pop, 'y-')
    # plt.plot(fox_pop, grass_pop, 'r-')

    # plt.title("Fox, Rabbit, and Grass Population over Time")
    # plt.xlabel("Population")
    # plt.ylabel("Population")
    # plt.legend()
    # plt.show()

if __name__ == "__main__":
    main()