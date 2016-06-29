import pygame

(width,height) = (300,200)
background_color = (0,0,0)
block_color = (255,255,255)
b_width = b_height = 10

def make_block(x, y):
	pygame.draw.rect(screen, block_color, (x, y, b_width, b_height))

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Mazerunner')
screen.fill(background_color)
make_block(0, 190)

pygame.display.flip()
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False



