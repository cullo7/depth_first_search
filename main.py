import pygame, sys, time

# TODO
# multiple files
# random direction at intersection
#

###################################################################### 
#                             SETUP                                  #
######################################################################

(width,height) = (500,400)
background_color = (0,0,0) #black
block_color = (255,255,255) #white

#giving a 10 pixel buffer on sides
b_width = b_height = 10
min_height = min_width = 10
max_height = 380
max_width = 480

#amount of height and width for 10x10 pixel boxe grid
y_count = (max_height/b_height)
x_count = (max_width/b_width)

"""
creating a x_count by y_count grid to keep track of squares already visited
makeshift 2D array will be a list of lists
"""
grid = []
for y in range(y_count):
	grid.append([])
	for x in range(x_count):
		grid[y].append(False)

#makeshift stack that cooridantes of possible options will be pushed to
positions = []

pygame.init() 

######################################################################
#                          FUNCTIONS                                 # 
######################################################################

#prints block to screen -- called when mazerunner visits a square	
def make_block(x, y): #print block to screen
	pygame.draw.rect(screen, block_color, (x, y, b_width, b_height))
	print "in make block"

def push(x,y):
	positions.append([x,y])

def pop():
	if (positions):
		return positions.pop()
	else:
		return -1

def move_to(x,y):
	x = (x/10)-1
	y = (38 - (y/10))-1
	print("x ", x)
	print("y ", y)
	print("height ", len(grid))
	print("width ", len(grid[0]))
	if(x > max_width or x < min_width or y > max_height or y < min_height):
		return False
	if(grid[y][x] == True):
		return False
	else:
		return True

def empty():
	return len(positions) == 0

def discover(x,y):
	make_block(x, y)
	#adjusting to index the array
	x = (x/10)-1
	y = 38 - (y/10)
	grid[y][x] = True

######################################################################
#                          MAIN                                      # 
######################################################################

if __name__ == '__main__':
	print("mazerunner beginning...")
	screen = pygame.display.set_mode((width,height))
	pygame.display.set_caption('Mazerunner')
	screen.fill(background_color)

	pygame.display.flip() #update screen
	running = True
	s = True
	#creates maze by stacking all options at intersections
	current_x = min_width/10
	current_y = min_height/10
	#possible coordinate system
	cur_path = [] 
	push(current_x, current_y)

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: #quit if red X button pressed
				running = False
		
		while not empty():
				cur_path = pop()
				print (cur_path[0]," ",cur_path[1])
				s = not s
				if(s):
					screen.fill((0,0,0))
				else:
					screen.fill((255,255,255))
				if move_to(cur_path[0], cur_path[1]):
					discover(cur_path[0], cur_path[1])	
				if(move_to(cur_path[0]+10,cur_path[1])):#to the right one
					push(current_x+10,current_y)
				
				if(move_to(cur_path[0],cur_path[1]-10)):#up one
					push(current_x,current_y-10)
				
				if(move_to(cur_path[0]-10,cur_path[1])):#to the left one
					push(current_x+10,current_y)	
				
				if(move_to(cur_path[0],cur_path[1]+10)):#down one
					push(current_x+10,current_y)
				print ("yo")
				time.sleep(2)
				pygame.display.flip()
		pygame.display.flip()

