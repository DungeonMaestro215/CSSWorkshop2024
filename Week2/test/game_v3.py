import pygame
import pygame.freetype
import random

# Global game variables
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Create the player
class Player:
    position = pygame.Vector2(screen_width / 2, screen_height - 130)
    velocity = pygame.Vector2(0, 0)
    speed = 300
    radius = 40
    score = 0
player = Player()

def draw_player():
    # Body
    pygame.draw.circle(screen, "black", player.position, player.radius+5)
    pygame.draw.circle(screen, "red", player.position, player.radius)

    # Eyes
    pygame.draw.circle(screen, "white", player.position + pygame.Vector2(-15, -10), 20)
    pygame.draw.circle(screen, "white", player.position + pygame.Vector2( 15, -10), 20)
    pygame.draw.circle(screen, "black", player.position + pygame.Vector2(-15, -10), 10)
    pygame.draw.circle(screen, "black", player.position + pygame.Vector2( 15, -10), 10)

# Move the player based on keyboard inputs
def move_player(dt):
    player.velocity.x = 0

    # Set player velocity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.velocity.y = -player.speed 
    if keys[pygame.K_DOWN]:
        player.velocity.y = player.speed 
    if keys[pygame.K_LEFT]:
        player.velocity.x = -player.speed 
    if keys[pygame.K_RIGHT]:
        player.velocity.x = player.speed 

    # Gravity
    player.velocity.y += 10

    # Move player
    player.position += player.velocity * dt

    # Keep player in bounds
    if player.position.x < -player.radius:
        player.position.x = screen_width + player.radius
    if player.position.x > screen_width + player.radius:
        player.position.x = -player.radius
    player.position.y = max(0, min(screen_height - 130, player.position.y))

# Draw the ground with some flowers
def draw_ground():
    ground_height = 100
    ground_outline = pygame.Rect(
        0, 
        screen_height - ground_height - 5, 
        screen_width, 
        ground_height)
    ground = pygame.Rect(
        0, 
        screen_height - ground_height, 
        screen_width, 
        ground_height)
    pygame.draw.rect(screen, "black", ground_outline)
    pygame.draw.rect(screen, "green", ground)

    draw_flower(1004, 648)
    draw_flower(1261, 702)
    draw_flower(757, 692)
    draw_flower(411, 701)
    draw_flower(200, 708)

# Draw a single flower centered at (x,y)
def draw_flower(x, y):
    pygame.draw.circle(screen, "black", pygame.Vector2(x-5, y-5), 13)
    pygame.draw.circle(screen, "pink", pygame.Vector2(x-5, y-5), 10)

    pygame.draw.circle(screen, "black", pygame.Vector2(x-5, y+5), 13)
    pygame.draw.circle(screen, "pink", pygame.Vector2(x-5, y+5), 10)

    pygame.draw.circle(screen, "black", pygame.Vector2(x+5, y-5), 13)
    pygame.draw.circle(screen, "pink", pygame.Vector2(x+5, y-5), 10)

    pygame.draw.circle(screen, "black", pygame.Vector2(x+5, y+5), 13)
    pygame.draw.circle(screen, "pink", pygame.Vector2(x+5, y+5), 10)

    pygame.draw.circle(screen, "pink", pygame.Vector2(x, y), 14)
    pygame.draw.circle(screen, "yellow", pygame.Vector2(x, y), 8)

# Draw a single cloud centered at (x,y)
def draw_cloud(x, y):
    pygame.draw.circle(screen, "black", pygame.Vector2(x-30, y+15), 35)
    pygame.draw.circle(screen, "white", pygame.Vector2(x-30, y+15), 30)

    pygame.draw.circle(screen, "black", pygame.Vector2(x-20, y-15), 35)
    pygame.draw.circle(screen, "white", pygame.Vector2(x-20, y-15), 30)

    pygame.draw.circle(screen, "black", pygame.Vector2(x+10, y-5), 35)
    pygame.draw.circle(screen, "white", pygame.Vector2(x+10, y-5), 30)

    pygame.draw.circle(screen, "black", pygame.Vector2(x+15, y+10), 35)
    pygame.draw.circle(screen, "white", pygame.Vector2(x+15, y+10), 30)

    pygame.draw.circle(screen, "white", pygame.Vector2(x-5, y), 30)

    

# Draw and move the clouds; each has an (x,y) position followed by a speed
clouds = [
    # [x, y, speed]
    [100, 50, 100], 
    [250, 100, 300], 
    [450, 200, 500], 
    [700, 75, 150], 
    [900, 150, 200],
    [900, 60, 210],
    ]
def draw_clouds(dt):
    for cloud in clouds:
        draw_cloud(cloud[0], cloud[1])
        cloud[0] += cloud[2] * dt
        if cloud[0] > screen_width + 100:
            cloud[0] = -100

# Draw a coin for the player to pick up
coin_bounds = 200
coin = pygame.Vector2(random.randint(coin_bounds, screen_width - coin_bounds), random.randint(coin_bounds, screen_height - coin_bounds))
def draw_coin():
    # Outlined circle
    pygame.draw.circle(screen, "black", pygame.Vector2(coin.x, coin.y), 25)
    pygame.draw.circle(screen, "yellow", pygame.Vector2(coin.x, coin.y), 20)
    # Fake a letter 'C' on the coin
    pygame.draw.circle(screen, "black", pygame.Vector2(coin.x, coin.y), 15)
    pygame.draw.circle(screen, "yellow", pygame.Vector2(coin.x, coin.y), 10)
    pygame.draw.circle(screen, "yellow", pygame.Vector2(coin.x+10, coin.y), 9)


# Detect if player has touched a coin
def detect_collision():
    if (player.position.distance_to(coin) < player.radius):
        # New coin
        coin.x = max(coin_bounds, min(coin.x + random.randint(-200, 200), screen_width - coin_bounds))
        coin.y = max(coin_bounds, min(coin.y + random.randint(-200, 200), screen_height - coin_bounds))
        # coin.x = random.randint(100, screen_width - 100)
        # coin.y = random.randint(100, screen_height - 100)
        # Get points
        player.score += 10


# Show the player's score
def show_score(game_font):
    text_surface, rect = game_font.render(f"Score: {player.score}", "black")
    screen.blit(text_surface, (40, 50))

def main():
    # Initialize Pygame
    pygame.init()

    # Font for text
    game_font = pygame.freetype.SysFont("Comic Sans MS", 24)

    # Set up screen
    pygame.display.set_caption("Game!")

    # Clock for controlling timing
    clock = pygame.time.Clock()

    # Game parameters
    dt = 0

    # Start game loop
    running = True
    while running:
        # If the 'X' button is pressed...
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen for the next frame
        background_color = "sky blue"
        screen.fill(background_color)

        ### Game rendering here ###
        move_player(dt)
        draw_ground()
        draw_clouds(dt)
        draw_player()
        draw_coin()
        detect_collision()
        show_score(game_font)
        ###########################

        # 'Flip' display to show our scene
        pygame.display.flip()

        # Runs at 60 fps
        # dt is seconds since last frame; used for 'physics' calculations
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()