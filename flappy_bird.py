import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_WIDTH = 80
PIPE_HEIGHT = random.randint(150, 450)
PIPE_GAP = 150

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load images
bird_image = pygame.Surface((30, 30))
bird_image.fill((255, 0, 0))
pipe_image = pygame.Surface((PIPE_WIDTH, SCREEN_HEIGHT))
pipe_image.fill((0, 255, 0))

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = 300
        self.velocity = 0

    def flap(self):
        self.velocity += FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

# Pipe class
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(150, 450)

    def update(self):
        self.x -= 5

    def draw(self):
        # Top pipe
        screen.blit(pipe_image, (self.x, self.height - SCREEN_HEIGHT))
        # Bottom pipe
        screen.blit(pipe_image, (self.x, self.height + PIPE_GAP))

# Game loop
def main():
    bird = Bird()
    pipes = [Pipe()]
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((135, 206, 235))  # Sky color

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        bird.update()

        # Check for pipe generation
        if pipes[-1].x < SCREEN_WIDTH - 200:
            pipes.append(Pipe())

        for pipe in pipes:
            pipe.update()
            pipe.draw()

        # Draw the bird
        screen.blit(bird_image, (bird.x, bird.y))

        # Check for collisions
        for pipe in pipes:
            if bird.x + 30 > pipe.x and bird.x < pipe.x + PIPE_WIDTH:
                if bird.y < pipe.height or bird.y + 30 > pipe.height + PIPE_GAP:
                    running = False

        # If the bird falls below the screen
        if bird.y > SCREEN_HEIGHT or bird.y < 0:
            running = False

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
