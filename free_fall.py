import pymunk, pygame, sys

def create_circle(space):
    body = pymunk.Body(1, 1, pymunk.Body.DYNAMIC)
    body.position = (400, 0)
    shape = pymunk.Circle(body, 40)
    space.add(body, shape)
    return shape

def draw_circles(circles):
    for circle in circles:
        pos_x = int(circle.body.position.x)
        pos_y = int(circle.body.position.y)
        pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), 40)

def create_bound(space):
    body = pymunk.Body(0, 0, pymunk.Body.STATIC)
    shape = pymunk.Segment(body, (100, 600), (700, 600), 20)
    space.add(body, shape)
    return shape

def draw_bounds(bounds):
    for bound in bounds:
        a_x = int(bound.a.x)
        a_y = int(bound.a.y)
        b_x = int(bound.b.x)
        b_y = int(bound.b.y)
        pygame.draw.line(screen, (0, 0, 0), (a_x, a_y), (b_x, b_y), 20)


pygame.init()
screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 100)
circles = []
circles.append(create_circle(space))
bounds = []
bounds.append(create_bound(space))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    draw_circles(circles)
    draw_bounds(bounds)
    space.step(1.0/60.0)
    pygame.display.update()
    clock.tick(120)