import pygame
import random

# Global game variables
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Initial Settings
start_x = screen_width / 2
start_y = screen_height / 2
speed = 500
radius = 40
body_part_positions = [pygame.Vector2(start_x, start_y)]
body_part_velocities = [pygame.Vector2(0,0)]
coin = pygame.Vector2(random.randint(0, screen_width), random.randint(0, screen_height))

# Get user input
def get_input(direction):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != "Down":
        return "Up"
    if keys[pygame.K_DOWN] and direction != "Up":
        return "Down"
    if keys[pygame.K_LEFT] and direction != "Right":
        return "Left"
    if keys[pygame.K_RIGHT] and direction != "Left":
        return "Right"

    return direction

# Draw the fancy snake head
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

# Draw the entire snake
def draw_player():
    for i in range(len(body_part_positions)-1, -1, -1):
        if i == 0:
            # First body part is the head
            draw_head(body_part_positions[i])
        else:
            pygame.draw.circle(screen, "red", body_part_positions[i], radius)


# Move the player based on keyboard inputs
def move_player(direction, dt):
    # Set velocity of the head based on player input
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

    return direction

# See if the head of the player has collided with anything
# Return True if the game is over, otherwise return False
def detect_collisions():
    # Coin
    if body_part_positions[0].distance_to(coin) < radius:
        # Pick a new random spot for the coin
        coin.x = random.randint(0, screen_width)
        coin.y = random.randint(0, screen_height)

        # Grow the snake
        body_part_positions.append(body_part_positions[len(body_part_positions)-1].copy())
        body_part_velocities.append(body_part_positions[len(body_part_velocities)-1].copy())
    
    # Another body part (skip the first few parts, as they are really close to the head)
    for i in range(5, len(body_part_positions)):
        if body_part_positions[0].distance_to(body_part_positions[i]) < radius:
            game_over_screen()
            return True

    # Edges of the screen
    if body_part_positions[0].x < 0 or body_part_positions[0].y < 0 or body_part_positions[0].x > screen_width or body_part_positions[0].y > screen_height:
        game_over_screen()
        return True

    return False

# Draw the coin
def draw_coin():
    # Outlined circle
    pygame.draw.circle(screen, "black", pygame.Vector2(coin.x, coin.y), 25)
    pygame.draw.circle(screen, "yellow", pygame.Vector2(coin.x, coin.y), 20)
    # Fake a letter 'C' on the coin
    pygame.draw.circle(screen, "black", pygame.Vector2(coin.x, coin.y), 15)
    pygame.draw.circle(screen, "yellow", pygame.Vector2(coin.x, coin.y), 10)
    pygame.draw.circle(screen, "yellow", pygame.Vector2(coin.x+10, coin.y), 9)

# Game over screen
def game_over_screen():
    font = pygame.font.SysFont('arial', 50)
    text = font.render('Game Over', True, "red")
    text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2))
    text2 = font.render('Press "R" to restart', True, "red")
    text_rect2 = text.get_rect(center=(screen_width / 2, screen_height / 2 + 50))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)

    game_over = True
    while game_over:
        # If the 'X' button is pressed...
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            body_part_positions.clear()
            body_part_positions.append(pygame.Vector2(start_x, start_y))
            body_part_velocities.clear()
            body_part_velocities.append(pygame.Vector2(0,0))
            coin.x = random.randint(0, screen_width)
            coin.y = random.randint(0, screen_height)

            # TODO: Need to make restarting actually work. Need to blit the screen surface? or something?
            # also text that says press 'R' to restart
            # also add a score counter
            # also simplify and clean up code
            game_over = False
        continue

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
    game_over = False
    while running:
        # If the 'X' button is pressed...
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen for the next frame
        background_color = "black"
        screen.fill(background_color)

        ### Game rendering here ###
        direction = get_input(direction)
        detect_collisions()
        move_player(direction, dt)
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