import pygame, pymunk
import pymunk.pygame_util

pygame.init()
window = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

def draw(space, window, draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()

def run(window):
    run = True
    fps = 60
    dt = 1 / fps
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0, 981)

    draw_options = pymunk.pygame_util.DrawOptions(window)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(space, window, draw_options)
        space.step(dt)
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    run(window)