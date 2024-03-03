import pymunk, pygame, sys

BLACK = pygame.Color(0, 0, 0)

def create_circle(space):
    body = pymunk.Body()
    body.position = (400, 0)
    shape = pymunk.Circle(body, 10)
    space.add(body, shape)
    return shape

def draw_circles(circles):
    for circle in circles:
        pos_x = circle.body.position.x
        pos_y = circle.body.position.y
        pygame.draw.circle(screen, BLACK, (pos_x, pos_y), 10)

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 9.81)
circles = []
circles.append(create_circle(space))