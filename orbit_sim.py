import pygame, pymunk, sys, copy

CONST_GRAV = 6.67430 * 10**-11      # N m^2 kg^-2
CONST_M_PER_PIXEL = 500_000_000
CONST_M_PER_AU = 150_000_000_000

CONST_RADIUS_SUN_M = 696_000_000
CONST_RADIUS_EARTH_M = 6_378_000
CONST_MASS_SUN_KG = 2e+30
CONST_MASS_EARTH_KG = 6e+24

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
screen_width = screen.get_width()
screen_height = screen.get_height()
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0.0, 0.0)

def create_star(mass_kg = CONST_MASS_SUN_KG, radius_m = CONST_RADIUS_SUN_M, pos_x = screen_width / 2, pos_y = screen_height / 2):
    body = pymunk.Body(mass_kg, 1, pymunk.Body.DYNAMIC)
    body.position = (pos_x, pos_y)
    radius_px = radius_m / CONST_M_PER_PIXEL
    shape = pymunk.Circle(body, radius_px * 8)
    space.add(body, shape)
    return shape

def create_planet(mass_kg = CONST_MASS_EARTH_KG, radius_m = CONST_RADIUS_EARTH_M, pos_x = screen_width / 2 - CONST_M_PER_AU / CONST_M_PER_PIXEL, pos_y = screen_height / 2, velocity_mps = 30000):
    body = pymunk.Body(mass_kg, 1, pymunk.Body.DYNAMIC)
    body.position = (pos_x, pos_y)
    body.velocity = (0, velocity_mps / CONST_M_PER_PIXEL)
    radius_px = radius_m / CONST_M_PER_PIXEL
    if radius_px < 1: radius_px = 1
    shape = pymunk.Circle(body, radius_px * 4)
    space.add(body, shape)
    return shape

def render(star, planet):
    pygame.draw.circle(screen, (255, 255, 0), (int(star.body.position.x), int(star.body.position.y)), int(star.radius))
    pygame.draw.circle(screen, (0, 78, 255), (int(planet.body.position.x), int(planet.body.position.y)), int(planet.radius))

def calculate_gravity(a_body, b_body):
    distance_squared = (((a_body.position.x - b_body.position.x) * CONST_M_PER_PIXEL) ** 2 + ((a_body.position.y - b_body.position.y) * CONST_M_PER_PIXEL) ** 2)
    magnitude = CONST_GRAV * int(a_body.mass) * int(b_body.mass) / distance_squared
    vector = pymunk.Vec2d(b_body.position.x - a_body.position.x, b_body.position.y - a_body.position.y)
    vector_norm = pymunk.Vec2d.normalized(vector)
    return vector_norm * magnitude / CONST_M_PER_PIXEL

def do_physics(star, planet):
    force = calculate_gravity(planet.body, star.body)
    planet.body.apply_force_at_local_point(force)

def rendertrail(trail):
    while len(trail) > 100:
        trail.remove(trail[0])
    for i in range(len(trail)):
        obj = trail[i]
        pygame.draw.circle(screen, (50, 50, 80), (int(obj.body.position.x), int(obj.body.position.y)), obj.radius/2)

def run(star, planet):
    trail = []
    trail_render_speed = 10
    trail_count = 0
    while True:
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30, 30, 30))
        if trail_count < trail_render_speed:
            trail_count += 1
        else:
            trail_count = 0
            trail.append(copy.deepcopy(planet))
        rendertrail(trail)
        render(star, planet)
        pygame.display.update()

        do_physics(star, planet)

        space.step(14400)
        clock.tick(120)

def main():
    star = create_star()
    planet = create_planet(velocity_mps=30000)
    run(star, planet)

if __name__ == "__main__":
    main()
