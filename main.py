import pygame
import sys

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
		grid[y].append(False)
		print(y,x)

#makeshift stack that cooridantes of possible options will be pushed to
positions = []

######################################################################
#                          FUNCTIONS                                 # 
######################################################################

#prints block to screen -- called when mazerunner visits a square	
def make_block(x, y): #print block to screen
	pygame.draw.rect(screen, block_color, (x, y, b_width, b_height))

def push(x,y):
	positionsi.append([x,y])

def pop():
	if (positions):
		return positions.pop()
	else:
		return -1

def check(x,y):
	if(x > max_width or x < min_width or y > max_height or y < min_height):
		return True
	if(positions[y][x] == True):
		return True
	else:
		return False

def empty():
	if len(positions) == 0:
		return True
	else:
		return False

def discover(x,y):
	positions[y][x] = True

def create_maze(cur_path):
	discover(cur_path)

######################################################################
#                          MAIN                                      # 
######################################################################

if __name__ == '__main__':
	print("mazerunner beginning...")
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
 
	#creates maze by stacking all options at intersections
	current_x = min_width
	current_y = min_height
	#possible coordinate system
	cur_path = [] 
	push(current_x, current_y)
	while !empty():
		cur_path = pop()
		if(!check):
			discover(cur_path[0], cur_path[1])
		if(!check(cur_path[0]+10,cur_path[1])):#to the right one
			push(current_x+10,current_y)
		if(!check(cur_path[0],cur_path[1]-10)):#up one
			push(current_x,current_y-10)
		if(!check(cur_path[0]-10,cur_path[1])):#to the left one
			push(current_x+10,current_y)	
		if(!check(cur_path[0],cur_path[1]+10)):#down one
			push(current_x+10,current_y)
