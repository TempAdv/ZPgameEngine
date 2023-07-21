
from pickle import TRUE
import pygame


#function to count how many other cells of some color cell have in nearest 8 one
def count8(cells,x,y,cell):
	#yeah this part is monstrosity
	neighbours = 0
	try:
		if cells[y-1][x-1] == cell:
			neighbours += 1 
	except:
		pass

	try:
		if cells[y][x-1] == cell:
			neighbours += 1 
	except:
		pass

	try:
		if cells[y+1][x-1] == cell:
			neighbours += 1 
	except:
		pass

	try:
		if cells[y-1][x] == cell:
			neighbours += 1 
	except:
		pass

	try:
		if cells[y+1][x] == cell:
			neighbours += 1 
	except:
		pass

	try:
		if cells[y-1][x+1] == cell:
			neighbours += 1 
	except:
		pass

	try:
		if cells[y][x+1] == cell:
			neighbours += 1 
	except:
		pass

	try:
		if cells[y+1][x+1] == cell:
			neighbours += 1 
	except:
		pass
	
	return neighbours



def main(colors,updateFunctions):

	#colors - dictionary of numbers and colors wich represents them
	#updateFunctions - dictionary of numbers and functions wich will be called when updater checks a cell with this color


	# size of cells grid
	SandboxXSize = 50
	SandboxYSize = 50
	
	# size of window
	WindowXSize = 451
	WindowYSize = 487
	
	# UTC - updateTimerCount. It grows until equals to UTCmax then UTC equals to 1 again. This 2 vars needed to call cells 
	# functions not in every frame
	UTC = 1
	UTCmax = 10
	
	activeColor = 1
	paused = False

	
	cells = []
	cellsBuffer = []

	#creating grid of cells and buffer of its

	for i in range(SandboxYSize):
		cells.append([])
		cellsBuffer.append([])
		row = cells[i]
		row2 = cellsBuffer[i]
		for j in range(SandboxXSize):
			row.append(1)
			row2.append(1)

	pygame.init()
	win = pygame.display.set_mode((WindowXSize, WindowYSize))
	pygame.display.set_caption("ZP")

	clock = pygame.time.Clock()
	run = True

	#updater calls function for every cell in cells but this functions change Buffer. When updater done with all cells
	#it will put result from buffer to 'cells'

	while(run):

		UTC += 1

		y = 0
		for i in cells:

			x = 0
			for cell in i:
				if not paused and UTC == UTCmax:

					function = updateFunctions[cell]
					function(cells, cellsBuffer, x,y)
				pygame.draw.rect(win, colors[cell], pygame.Rect(9*x+1, 9*y+37, 8, 8))

				x += 1
			y += 1
		
		#panel things

		#pause indicator
		pygame.draw.rect(win, '#000000', pygame.Rect(3, 3, 30, 30))
		if paused:
			
			pygame.draw.rect(win, '#FFFFFF', pygame.Rect(5, 4, 10, 28))
			pygame.draw.rect(win, '#FFFFFF', pygame.Rect(19, 4, 10, 28))
		else:
			pygame.draw.polygon(win, '#FFFFFF', ((9, 4),(23, 18),(9, 32)))
			pass

		#active color indicator
		pygame.draw.rect(win, colors[activeColor], pygame.Rect(40, 4, 28, 28))
		
		if UTC >= UTCmax:
			UTC = 0

		for i in range(SandboxYSize):
			row = cells[i]
			row2 = cellsBuffer[i]
			for j in range(SandboxXSize):
				row[j] = row2[j]

		for event in pygame.event.get():

			if pygame.mouse.get_pressed()[0] and activeColor!= -1:
				mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
				if mouse_pos_x > 0 and mouse_pos_x < WindowXSize and mouse_pos_y> 36 and mouse_pos_y < WindowYSize:
					mouse_cell_x = (mouse_pos_x - 1) // 9
					mouse_cell_y = (mouse_pos_y - 37) // 9
					cellsBuffer[mouse_cell_y][mouse_cell_x] = activeColor

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_p:
					if paused == False: paused = True
					else: paused = False

				if event.key == pygame.K_MINUS and UTCmax > 1:
					UTCmax -= 1

				if event.key == pygame.K_EQUALS:
					UTCmax += 1
					
				# lil monstrosity

				if event.key == pygame.K_1:
					activeColor = 1

				if event.key == pygame.K_2:
					activeColor = 2

				if event.key == pygame.K_3:
					activeColor = 3

				if event.key == pygame.K_4:
					activeColor = 4

				if event.key == pygame.K_5:
					activeColor = 5

				if event.key == pygame.K_6:
					activeColor = 6

				if event.key == pygame.K_7:
					activeColor = 7

				if event.key == pygame.K_8:
					activeColor = 8

				if event.key == pygame.K_9:
					activeColor = 9

				if event.key == pygame.K_0:
					activeColor = 0
					
			if event.type == pygame.QUIT:
				run = False

		clock.tick(60)

		pygame.display.flip()

	pygame.quit()

#if __name__ == "__main__":
#    main()