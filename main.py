import pygame, sys, time, random

# TODO
# multiple files
# random direction at intersection
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

def push(x,y,DIR):
	positions.append([x,y, DIR])

def pop():
	if (positions):
		return positions.pop()
	else:
		return -1

def check_point(x, y):
	return not (x > max_width or x < min_width or y > max_height or y < min_height)

def move_to(x, y, direction):
	print '\n' +'\n'
	print("Direction: ", direction)
	print("move_to")
	print("x ", x)
	print("y ", y)
	print("height ", len(grid))
	print("width ", len(grid[0]))
	index_x = to_index_x(x)
	index_y = to_index_y(y)

	
	if not check_point(x,y):
		print("FAIL - OOB")
		return False
	
	if(grid[index_y][index_x]):
		print("FAIL - EXISTS")
		return False
	
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
	
	else:
		print("SUCCESS")
		return True

def empty():
	return len(positions) == 0

def discover(x,y):
	print("disc")
	make_block(x, y)
	#adjusting to index the array
	x = to_index_x(x)
	y = to_index_y(y)
	grid[y][x] = True

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
	s = True
	#creates maze by stacking all options at intersections
	current_x = min_width
	current_y = max_height
	#possible coordinate system
	cur_path = [] 
	push(current_x, current_y, "UP")
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: #quit if red X button pressed
				running = False
		
		while not empty():
				cur_path = pop()
				print(cur_path[0],"<current>", cur_path[1], "dir ", cur_path[2] )	
				if(move_to(cur_path[0], cur_path[1], cur_path[2])):
					
					discover(cur_path[0], cur_path[1])	

					temp_list = []
					count = 0
					
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
					
					while len(temp_list) != 0:
						rand_num = random.randint(0, len(temp_list)-1)
						push(temp_list[rand_num][0], temp_list[rand_num][1], temp_list[rand_num][2])
						temp_list.pop(rand_num)

					print("#################################################################################")

					pygame.display.flip()
	pygame.display.flip()
	time.sleep(10)
