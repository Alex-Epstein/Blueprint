import pymunk, pygame, sys

BLACK = pygame.Color("black")
GREY = pygame.Color("grey")
WHITE = pygame.Color("white")

pygame.init()
screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 98.1)

def create_projectile(space, mass=10, moment=100, x=400, y=0, radius=40):
    body = pymunk.Body(mass, moment, pymunk.Body.DYNAMIC)
    body.position = (x, y)
    shape = pymunk.Circle(body, radius)
    space.add(body, shape)
    body.apply_force_at_local_point((random.randrange(-100 * mass, 100 * mass), 0))
    return shape