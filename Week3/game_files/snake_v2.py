import pygame
import random

# Global game variables
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Create the player
start_x = screen_width / 2
start_y = screen_height / 2
speed = 300
radius = 40
body_part_positions = [pygame.Vector2(start_x, start_y)]
body_part_velocities = [pygame.Vector2(0,0)]
coin = pygame.Vector2(random.randint(0, screen_width), random.randint(0, screen_height))

def draw_head(pos):
    pygame.draw.circle(screen, "tan", pos + (-37, 0), 15)
    pygame.draw.circle(screen, "tan", pos + ( 37, 0), 15)

    pygame.draw.circle(screen, "red",   pos, radius)
    pygame.draw.circle(screen, "white", pos + (-10, -15), 20)
    pygame.draw.circle(screen, "white", pos + ( 10, -15), 20)
    pygame.draw.circle(screen, "black", pos + (-10, -15), 10)
    pygame.draw.circle(screen, "black", pos + ( 10, -15), 10)

    pygame.draw.circle(screen, "green", pos + (-25, 0), 10)
    pygame.draw.circle(screen, "green", pos + ( 25, 0), 10)

def draw_player():
    for i in range(len(body_part_positions)-1, -1, -1):
        if i == 0:
            draw_head(body_part_positions[i])
        else:
            pygame.draw.circle(screen, "red", body_part_positions[i], radius)


# Move the player based on keyboard inputs
def move_player(direction, dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = "Up"
    if keys[pygame.K_DOWN]:
        direction = "Down"
    if keys[pygame.K_LEFT]:
        direction = "Left"
    if keys[pygame.K_RIGHT]:
        direction = "Right"

    if direction == "Up":
        body_part_velocities[0].x = 0
        body_part_velocities[0].y = -speed 
    if direction == "Down":
        body_part_velocities[0].x = 0
        body_part_velocities[0].y = speed 
    if direction == "Left":
        body_part_velocities[0].x = -speed 
        body_part_velocities[0].y = 0
    if direction == "Right":
        body_part_velocities[0].x = speed 
        body_part_velocities[0].y = 0
    
    for i in range(len(body_part_positions)):
        if i != 0:
            x1 = body_part_positions[i].x
            y1 = body_part_positions[i].y
            x2 = body_part_positions[i-1].x
            y2 = body_part_positions[i-1].y
            body_part_velocities[i] = pygame.Vector2(x2-x1, y2-y1) * speed / 100

        body_part_positions[i] += body_part_velocities[i] * dt

    if body_part_positions[0].distance_to(coin) < radius:
        eat_coin()

    return direction


def grow_player():
    body_part_positions.append(body_part_positions[len(body_part_positions)-1].copy())
    body_part_velocities.append(body_part_positions[len(body_part_velocities)-1].copy())

def eat_coin():
    grow_player()
    coin.x = random.randint(0, screen_width)
    coin.y = random.randint(0, screen_height)

def draw_coin():
    # Outlined circle
    pygame.draw.circle(screen, "black", pygame.Vector2(coin.x, coin.y), 25)
    pygame.draw.circle(screen, "yellow", pygame.Vector2(coin.x, coin.y), 20)
    # Fake a letter 'C' on the coin
    pygame.draw.circle(screen, "black", pygame.Vector2(coin.x, coin.y), 15)
    pygame.draw.circle(screen, "yellow", pygame.Vector2(coin.x, coin.y), 10)
    pygame.draw.circle(screen, "yellow", pygame.Vector2(coin.x+10, coin.y), 9)


def main():
    # Initialize Pygame
    pygame.init()

    # Set up screen
    pygame.display.set_caption("Game!")

    # Clock for controlling timing
    clock = pygame.time.Clock()

    # Game parameters
    dt = 0
    direction = "Down"

    # Start game loop
    running = True
    while running:
        # If the 'X' button is pressed...
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen for the next frame
        background_color = "black"
        screen.fill(background_color)

        ### Game rendering here ###
        direction = move_player(direction, dt)
        draw_player()
        draw_coin()
        ###########################

        # 'Flip' display to show our scene
        pygame.display.flip()

        # Runs at 60 fps
        # dt is seconds since last frame; used for 'physics' calculations
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()