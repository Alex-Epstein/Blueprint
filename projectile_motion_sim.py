import pymunk, pygame, sys, random

BLACK = pygame.Color("black")
GREY = pygame.Color("grey")
WHITE = pygame.Color("white")

def init():
    pygame.init()
    screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
    width = screen.get_width()
    height = screen.get_height()
    clock = pygame.time.Clock()
    space = pymunk.Space()
    space.gravity = (0, 98.1)
    return screen, width, height, clock, space

def create_projectile(space, mass=10, moment=100, x=400, y=0, v_x=0, v_y=0, radius=40):
    body = pymunk.Body(mass, moment, pymunk.Body.DYNAMIC)
    body.position = (x, y)
    body.velocity = (v_x, v_y)
    shape = pymunk.Circle(body, radius)
    space.add(body, shape)
    return shape

def draw_circles(screen, circles):
    for circle in circles:
        pygame.draw.circle(screen, GREY, (int(circle.body.position.x), int(circle.body.position.y)), int(circle.radius))

def run(screen, width, height, clock, space, circles):
    while True:
        width = screen.get_width()
        height = screen.get_height()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for _ in range(5):
                    circles.append(create_projectile(space, x=random.randint(0, width), y=random.randint(0, height), v_x=random.randint(0, 100), v_y=-random.randint(0, 200), radius=10))

        screen.fill((255, 255, 255))
        draw_circles(screen, circles)
        space.step(1.0/60.0)
        pygame.display.update()
        pygame.display.set_caption("fps: " + str(clock.get_fps()) + " " + str(width) + " " + str(height))
        clock.tick(120)


def main():
    screen, width, height, clock, space = init()
    circles = []
    circles.append(create_projectile(space, x=50, y=200, v_x=100, v_y=-200, radius=10))
    run(screen, width, height, clock, space, circles)

if __name__ == "__main__":
    main()