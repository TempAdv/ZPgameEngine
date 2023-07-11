
import pygame
import random

def main(colors,updateFunctions):


	SandboxXSize = 50
	SandboxYSize = 50
	

	WindowXSize = 451
	WindowYSize = 451
	
	cells = []
	cellsBuffer = []

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
	while(run):

		y = 0
		for i in cells:

			x = 0
			for cell in i:
				function = updateFunctions[cell]
				function(cells, cellsBuffer, x,y)
				pygame.draw.rect(win, colors[cell], pygame.Rect(9*x+1, 9*y+1, 8, 8))

				x += 1
			y += 1

		for i in range(SandboxYSize):
			row = cells[i]
			row2 = cellsBuffer[i]
			for j in range(SandboxXSize):
				row[j] = row2[j]

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				mouse_pos = pygame.mouse.get_pos()
				mouse_pos_x, mouse_pos_y = mouse_pos

				if mouse_pos_x> 0 and mouse_pos_x < WindowXSize and mouse_pos_y> 0 and mouse_pos_y < WindowYSize:
					mouse_cell_x = (mouse_pos_x - 1) // 9
					mouse_cell_y = (mouse_pos_y - 1) // 9
					row = cellsBuffer[mouse_cell_y]
					
					if event.key == pygame.K_1:
						row[mouse_cell_x] = 1

					if event.key == pygame.K_2:
						row[mouse_cell_x] = 2

					if event.key == pygame.K_3:
						row[mouse_cell_x] = 3

					if event.key == pygame.K_4:
						row[mouse_cell_x] = 4

					if event.key == pygame.K_5:
						row[mouse_cell_x] = 5

					if event.key == pygame.K_6:
						row[mouse_cell_x] = 6

					if event.key == pygame.K_7:
						row[mouse_cell_x] = 7

					if event.key == pygame.K_8:
						row[mouse_cell_x] = 8

					if event.key == pygame.K_9:
						row[mouse_cell_x] = 9

					if event.key == pygame.K_0:
						row[mouse_cell_x] = 0
					
			if event.type == pygame.QUIT:
				run = False

		clock.tick(10)

		pygame.display.flip()

	pygame.quit()

#if __name__ == "__main__":
#    main()