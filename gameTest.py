import pygame
from gameBar import Bar
# Initialize Pygame/home/bryan
pygame.init()


# Set up the display
screen = pygame.display.set_mode((640, 480))

# Load the sprite image
playerFace = pygame.image.load("redface.png").convert_alpha()
gamebar = Bar(height=50,width=100)
# Create a sprite object
sprite = pygame.sprite.Sprite()
sprite.image = playerFace
sprite.rect = playerFace.get_rect()

# Set the initial position of the sprite
sprite.rect.x = 320
sprite.rect.y = 240

# Set the speed of the sprite (in pixels per frame)
sprite.speed = 1


# Boundaries
left_boundary = 0
right_boundary = 640
top_boundary = 0
bottom_boundary = 480

# Run the game loop
running = True
while running:

    sprite.rect.x += sprite.speed
    sprite.rect.y += sprite.speed

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the sprite's position
    sprite.rect.x += sprite.speed
    sprite.rect.y += sprite.speed

    if sprite.rect.left < left_boundary or sprite.rect.right > right_boundary:
        sprite.speed = -sprite.speed
    if sprite.rect.top < top_boundary or sprite.rect.bottom > bottom_boundary:
        sprite.speed = -sprite.speed

    # Draw the screen
    screen.fill((255, 255, 255))
    screen.blit(sprite.image, sprite.rect)
    pygame.display.flip()

# Quit Pygame
pygame.quit()

