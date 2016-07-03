import pygame, time, random

# Possible Improvements #
# split project into smaller files
# implement a class
# have changing block be a different color from white
#

###################################################################### 
#                             SETUP                                  #
######################################################################

(width,height) = (510,410)
background_color = (0,0,0) #black
block_color = (255,255,255) #white

#giving a 10 pixel buffer on sides
b_width = b_height = 10
min_height = min_width = 10
max_height = 390
max_width = 490

finish  = 0

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

pygame.init() # initialize pygame display and modules

######################################################################
#                          FUNCTIONS                                 # 
######################################################################

#prints block to screen -- called when mazerunner visits a square	
def make_block(x, y): #print block to screen
	pygame.draw.rect(screen, block_color, (x, y, b_width, b_height))
	# makes starting square red
	if x == 10 and y == 390:
		pygame.draw.rect(screen, (255,0,0), (x-10, y, b_width, b_height))
	
	# checks if program has hit top panel, if so green square signals what will be end of maze
	if x == 490 and finish == 0:
		pygame.draw.rect(screen, (0,255,0), (x+10, y, b_width, b_height))
		global finish
		finish = 1 #change so no other variable is end
	
	# checks if program has hit top panel, if so green square signals what will be end of maze
	if y == 10 and finish == 0:	
		pygame.draw.rect(screen, (0,255,0), (x, y-10, b_width, b_height))
		global finish # get global variable
		finish = 1 # change so no other square can be the end

# push to 'stack''
def push(x,y,DIR):
	positions.append([x,y, DIR])

# pop from stack
def pop():
	if (positions): # check if anyhting is in stack
		return positions.pop()
	else:
		return -1

# check if points are out of bounds
def check_point(x, y):
	return not (x > max_width or x < min_width or y > max_height or y < min_height)

# check if next space can be moved into
def move_to(x, y, direction):
	 # change from graphical position to index of boolean values
	index_x = to_index_x(x)	
	index_y = to_index_y(y)

	# if out of bounds exit
	if not check_point(x,y):
		print("FAIL - OOB")
		return False
	
	# if the position has already been visited
	if(grid[index_y][index_x]):
		print("FAIL - EXISTS")
		return False
	
	"""
		The next few lines of code check the surroundings of the square being moved into and colored
		white. The function takes in a parameter for the direction the previous block was so that 
		we only have to check certain blocks (opposite to the way we came). The point is checked
		to be in the bounds, then that it is in a certain direction then if it exists already. If 
		all these paremters are true for a certain black the function returns false and this path 
		is no longer a possibility. left in Fail messages for debugging.
	"""
	if(check_point(x-10,y) and  direction != "RIGHT" and grid[index_y][index_x-1] == True):
		print("FAIL - BOUNDARY_EXISTS")
		return False
	
	if(check_point(x-10,y-10) and  direction != "RIGHT" and direction != "DOWN" and grid[index_y+1][index_x-1] == True):
		print("FAIL - BOUNDARY_EXISTS")
		return False
	
	if(check_point(x,y-10) and  direction != "DOWN" and grid[index_y+1][index_x] == True):
		print("FAIL - BOUNDARY_EXISTS")
		return False
	
	if(check_point(x+10,y-10) and  direction != "LEFT" and direction != "DOWN" and grid[index_y+1][index_x+1] == True):
		print("FAIL - BOUNDARY_EXISTS")
		return False
	
	if(check_point(x+10,y) and  direction != "LEFT" and grid[index_y][index_x+1] == True):
		print("FAIL - BOUNDARY_EXISTS")
		return False
	
	if(check_point(x+10,y+10) and  direction != "LEFT"  and direction != "UP" and grid[index_y-1][index_x+1] == True):
		print("FAIL - BOUNDARY_EXISTS")
		return False
	
	if(check_point(x,y+10) and  direction != "UP"  and grid[index_y-1][index_x] == True):
		print("FAIL - BOUNDARY_EXISTS")
		return False
	
	if(check_point(x-10,y+10) and  direction != "RIGHT" and direction != "UP" and grid[index_y-1][index_x-1] == True):
		print("FAIL - BOUNDARY_EXISTS")
		return False
	
	# if no error is caught it is a viable path
	else:
		print("SUCCESS")
		return True

# check if no possible options
def empty():
	return len(positions) == 0

# mark as visited and draw block
def discover(x,y):
	make_block(x, y)
	x = to_index_x(x)
	y = to_index_y(y)
	grid[y][x] = True

# map graphics to index val
def to_index_x(x):
	return (x/10)-1

def to_index_y(y):
	return 39 - (y/10)

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
	#creates maze by stacking all options at intersections
	current_x = min_width
	current_y = max_height
	#possible coordinate system
	cur_path = [] 
	push(current_x, current_y, "UP") # add beginning of path
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: #quit if red X button pressed
				running = False
		
		while not empty():
				cur_path = pop()
				print(cur_path[0],"<current>", cur_path[1], "dir ", cur_path[2] )	
				if(move_to(cur_path[0], cur_path[1], cur_path[2])): # if current block is viable option
					
					discover(cur_path[0], cur_path[1])	

					temp_list = []
					count = 0 # used to exapand array for later iteration

					# check all possible options at each intersection

					if(move_to(cur_path[0]+10,cur_path[1], "RIGHT")):#to the right one
						count +=1
						temp_list.append((cur_path[0]+10,cur_path[1], "RIGHT"))
					
					if(move_to(cur_path[0],cur_path[1]-10, "UP")):#up one
						count +=1
						temp_list.append((cur_path[0],cur_path[1]-10, "UP"))
					
					if(move_to(cur_path[0]-10,cur_path[1], "LEFT")):#to the left one
						count +=1
						temp_list.append((cur_path[0]-10,cur_path[1], "LEFT"))

					if(move_to(cur_path[0],cur_path[1]+10, "DOWN")):#down one
						count +=1
						temp_list.append((cur_path[0],cur_path[1]+10, "DOWN"))
					
					# iterate through and add to stack randomly
					while len(temp_list) != 0:
						rand_num = random.randint(0, len(temp_list)-1) # get random index
						push(temp_list[rand_num][0], temp_list[rand_num][1], temp_list[rand_num][2])
						temp_list.pop(rand_num)

					pygame.display.flip() #update screen
	pygame.display.flip() 
