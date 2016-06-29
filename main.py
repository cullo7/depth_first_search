import pygame

######################################################################                          FUNCTIONS                                 # 
#                             SETUP                                  #
######################################################################

(width,height) = (500,400)
background_color = (0,0,0) #black
block_color = (255,255,255) #white

#giving a 10 pixel buffer on sides
b_width = b_height = 10
max_height = min_width = 10
min_height = 380
max_width = 480

#amount of height and width for 10x10 pixel boxe grid
y_count = (height/b_height)-2
x_count = (width/b_width)-2

"""
creating a x_count by y_count grid to keep track of squares already visited
makeshift 2D array will be a list of lists
"""
grid = []
for y in range(y_count):
	grid.append([])
	for x in range(x_count):
		grid[y].append(x)

######################################################################
#                          FUNCTIONS                                 # 
######################################################################

#prints block to screen -- called when mazerunner visits a square	
def make_block(x, y): #print block to screen
	pygame.draw.rect(screen, block_color, (x, y, b_width, b_height))

#creates maze by stacking all options at intersections
def create_maze():
	


screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Mazerunner')
screen.fill(background_color)
make_block(10, 380)

pygame.display.flip() #update screen
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #quit if red X button pressed
			running = False


######################################################################
#                          MAIN                                      # 
######################################################################

if __name__ == '__main__':
	print("mazerunner beginning...")

