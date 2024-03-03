import pygame
import pymunk
import pymunk.pygame_util
import math


pygame.init()

area = pygame.display.set_mode().get_rect() # Default to screen resolution
WIDTH, HEIGHT = area[2], area[3]
window = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

def draw(space, window, draw_options):
	window.fill("white")
	space.debug_draw(draw_options)
	pygame.display.update()


def create_pendulum(space):
	# values inputted
	r = 80 #cm  
	m = 1000 #grams 
	l = 350 #cm
	A = 40 #degrees
	T = -1 #seconds

	bob_x = (l * math.sin(math.radians(A)))
	bob_y = (l * math.cos(math.radians(A))) 

	print(bob_x, bob_y)

	rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
	rotation_center_body.position = (WIDTH/2, HEIGHT/5)

	body = pymunk.Body()
	body.position = (WIDTH/2, HEIGHT/5)
	line = pymunk.Segment(body, (0, 0), (bob_x, bob_y), 5) # draws line relative to body (static point)
	bob = pymunk.Circle(body, r, (bob_x, bob_y)) # puts the bob at the end of the line
	line.friction = 1
	bob.friction = 1
	line.mass = 8
	bob.mass = 30
	bob.elasticity = 0.95
	rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (0, 0), (0, 0))
	space.add(bob, line, body, rotation_center_joint)

def run(window, width, height):
	run = True
	clock = pygame.time.Clock()
	fps = 60
	dt = 1 / fps

	space = pymunk.Space()
	space.gravity = (0, 981) # cm/s^2 ? 

	create_pendulum(space)

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

# Calculations
if __name__ == "__main__":
	run(window, WIDTH, HEIGHT) # runs pygame simulation