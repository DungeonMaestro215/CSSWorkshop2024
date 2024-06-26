import pygame
import random

# Screen dimensions and grid size
screen_width = 400
screen_height = 400
box_size = 20
num_boxes = screen_width // box_size

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Create screen
screen = pygame.display.set_mode((screen_width, screen_height))

def generate_food():
    return {
        'x': random.randint(0, num_boxes - 1) * box_size,
        'y': random.randint(0, num_boxes - 1) * box_size
    }

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, green if segment == snake[0] else white, pygame.Rect(segment['x'], segment['y'], box_size, box_size))

def draw_food(food):
    pygame.draw.rect(screen, red, pygame.Rect(food['x'], food['y'], box_size, box_size))

def move_snake(direction, snake):
    head = snake[0].copy()
    if direction == 'LEFT':
        head['x'] -= box_size
    elif direction == 'RIGHT':
        head['x'] += box_size
    elif direction == 'UP':
        head['y'] -= box_size
    elif direction == 'DOWN':
        head['y'] += box_size
    snake.insert(0, head)
    return snake

def check_collision(snake):
    head = snake[0]
    if head['x'] < 0 or head['x'] >= screen_width or head['y'] < 0 or head['y'] >= screen_height:
        return True
    for segment in snake[1:]:
        if head == segment:
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
    # Initialize Pygame
    pygame.init()

    # Set up display
    pygame.display.set_caption('Snake Game')

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()
    snake_speed = 15

    # Initial snake and food positions
    snake = [{'x': 10 * box_size, 'y': 10 * box_size}]
    direction = 'RIGHT'
    food = generate_food()


    running = True
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
        snake = move_snake(direction, snake)

        if snake[0]['x'] == food['x'] and snake[0]['y'] == food['y']:
            food = generate_food()
        else:
            snake.pop()

        if check_collision(snake):
            game_over_screen()
            running = False

        draw_snake(snake)
        draw_food(food)
        pygame.display.flip()
        clock.tick(snake_speed)

    pygame.quit()

if __name__ == '__main__':
    main()
