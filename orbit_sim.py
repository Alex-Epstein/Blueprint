import time
import pygame, pymunk, sys

grav_const = 6.67430 * 0.001

def create_circle_body(space):
    body1 = pymunk.Body(10, 100, body_type = pymunk.Body.DYNAMIC)
    body1.position = (100, 500)
    return body1

def create_circle_shape(space, body1):
    # body1.apply_force_at_local_point((1000*body1.mass, 15), (0, 0))
    shape1 = pymunk.Circle(body1, 80)
    space.add(body1, shape1)
    return shape1

def sun(space):
    sun = pymunk.Body(100000000, 100, body_type = pymunk.Body.STATIC)
    sun.position = (1000, 500)
    sunShape = pymunk.Circle(sun, 200)
    space.add(sun, sunShape)
    return sunShape



def draw_circles(circles, body):

    planet_force = (10 * 100000000) / body.position.get_dist_sqrd((1000, 500))
    pygame.draw.circle(screen, (255,255,0), (1000, 500), 200)
    
    body.apply_force_at_local_point((planet_force * grav_const, 0), (0,0))
    pos_x = int(circles[0].body.position.x)
    pos_y = int(circles[0].body.position.y)
    pygame.draw.circle(screen, (0,0,0), (pos_x, pos_y), 80)

    # pos_x = int(circles[1].body.position.x)
    # pos_y = int(circles[1].body.position.y)
    
    


pygame.init()
screen = pygame.display.set_mode((1600, 800), pygame.RESIZABLE)
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 0)
body = create_circle_body(space)
circles = []
circles.append(create_circle_shape(space, body))
# circles.append(sun(space))
i = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((217, 217, 217))
    draw_circles(circles, body)
    space.step(1/50)
    # body1.apply_force_at_local_point((2*body1.mass*i, 15), (0, 0))
    pygame.display.update()
    pygame.display.set_caption(str((10 * 1000000) / body.position.get_dist_sqrd((1000, 500))*grav_const))
    clock.tick(120)