import pygame

# Global game variables
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Create the player
class Player:
    position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    speed = 300
player = Player()

def draw_player():
    # Body
    diameter = 40


    pygame.draw.circle(screen, "tan", player.position + (-37, 0), 15)
    pygame.draw.circle(screen, "tan", player.position + ( 37, 0), 15)

    pygame.draw.circle(screen, "red",   player.position, diameter)
    pygame.draw.circle(screen, "white", player.position + (-10, -15), 20)
    pygame.draw.circle(screen, "white", player.position + ( 10, -15), 20)
    pygame.draw.circle(screen, "black", player.position + (-10, -15), 10)
    pygame.draw.circle(screen, "black", player.position + ( 10, -15), 10)

    pygame.draw.circle(screen, "green", player.position + (-25, 0), 10)
    pygame.draw.circle(screen, "green", player.position + ( 25, 0), 10)

# Move the player based on keyboard inputs
def move_player(dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.position.y -= player.speed * dt
    if keys[pygame.K_DOWN]:
        player.position.y += player.speed * dt
    if keys[pygame.K_LEFT]:
        player.position.x -= player.speed * dt
    if keys[pygame.K_RIGHT]:
        player.position.x += player.speed * dt

def main():
    # Initialize Pygame
    pygame.init()

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
        background_color = "black"
        screen.fill(background_color)

        ### Game rendering here ###
        move_player(dt)
        draw_player()
        ###########################

        # 'Flip' display to show our scene
        pygame.display.flip()

        # Runs at 60 fps
        # dt is seconds since last frame; used for 'physics' calculations
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()