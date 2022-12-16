import pygame
import random
import time


if __name__ == '__main__':
    pygame.init()
    width, height = 800, 800
    screen = pygame.display.set_mode((width, height))
    screen.fill((255, 255, 255))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(10):
                    coords = (random.randint(0, 800), random.randint(0, 800))
                    radius = random.randint(0, 200)
                    pygame.draw.circle(screen, pygame.Color('yellow'), coords, radius)
        pygame.display.flip()
    pygame.quit()
