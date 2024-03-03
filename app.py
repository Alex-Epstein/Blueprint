import pygame, pymunk, sys

def create_circle(space):
    body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
    body.position = (400, 0)
    shape = pymunk.Circle(body, 80)
    space.add(body, shape)
    return shape

def draw_circles(circles):
    for circle in circles:
        pos_x = int(circle.body.position.x)
        pos_y = int(circle.body.position.y)
        pygame.draw.circle(screen, (0,0,0), (pos_x, pos_y), 80)

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 500)
circles = []
circles.append(create_circle(space))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((217, 217, 217))
    draw_circles(circles)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)