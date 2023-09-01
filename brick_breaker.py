import pygame

import sys

# Initialize Pygame
pygame.init()



# Set up display
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Brick Breaker')

# Initialize paddle properties
paddle_width = 100
paddle_height = 20
paddle_color = (0, 128, 255)
paddle_pos = [(window_size[0] - paddle_width) // 2, window_size[1] - 2 * paddle_height]

# Initialize ball properties
ball_diameter = 20
ball_color = (255, 255, 255)
ball_pos = [(window_size[0] - ball_diameter) // 2, window_size[1] // 2]

# Initialize brick properties
brick_rows = 5
brick_cols = 12
brick_width = 62
brick_height = 20
brick_color = (255, 0, 0)
brick_gap = 5

# Create bricks
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        brick = pygame.Rect(col * (brick_width + brick_gap), row * (brick_height + brick_gap), brick_width, brick_height)
        bricks.append(brick)

# Initialize paddle speed
paddle_speed = 3

# Initialize ball speed
ball_speed = [0.5, 0.5]

# Initialize score
score = 0


# Main game loop
while True:
    window.fill((0, 0, 0))  # Clear the screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        paddle_pos[0] -= paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle_pos[0] += paddle_speed

    # Ensure paddle stays within screen bounds
    paddle_pos[0] = max(paddle_pos[0], 0)
    paddle_pos[0] = min(paddle_pos[0], window_size[0] - paddle_width)
    
    # Draw the paddle
    pygame.draw.rect(window, paddle_color, (paddle_pos[0], paddle_pos[1], paddle_width, paddle_height))
    # Draw the ball
    pygame.draw.circle(window, ball_color, ball_pos, ball_diameter // 2)

    # Draw the bricks
    for brick in bricks:
        pygame.draw.rect(window, brick_color, brick)

        # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Ball collision with wall
    if ball_pos[0] <= 0 or ball_pos[0] >= window_size[0] - ball_diameter:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= 0:
        ball_speed[1] = -ball_speed[1]

    # Check if the ball is missed
    if ball_pos[1] >= window_size[1]:
        ball_pos = [(window_size[0] - ball_diameter) // 2, window_size[1] // 2]
        ball_speed = [0.5, 0.5]

    # Ball collision with paddle
    paddle_rect = pygame.Rect(paddle_pos[0], paddle_pos[1], paddle_width, paddle_height)
    ball_rect = pygame.Rect(ball_pos[0], ball_pos[1], ball_diameter, ball_diameter)
    
    if paddle_rect.colliderect(ball_rect):
        ball_speed[1] = -ball_speed[1]

    # Ball collision with bricks
    for brick in bricks[:]:
        if brick.colliderect(pygame.Rect(ball_pos[0], ball_pos[1], ball_diameter, ball_diameter)):
            ball_speed[1] = -ball_speed[1]
            bricks.remove(brick)
            score += 1
    # Display the score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    window.blit(score_text, (10, 10))




    # Update the display
    pygame.display.update()



