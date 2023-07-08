
import pygame
import random

def main():
	colors = {0:'#202000',
		   1:'#A0A000'

	}

	def passFun(x,y):
		pass

	def disappear(x,y):
		pass
		#row = cells[y]
		#row[x] = random.randint(0,1)




	updateFunctions = {
		0:passFun,
		1:disappear
		}


	SandboxXSize = 50
	SandboxYSize = 50
	

	WindowXSize = 451
	WindowYSize = 451
	
	cells = []

	for i in range(SandboxYSize):
		cells.append([])
		row = cells[i]
		for j in range(SandboxXSize):
			row.append(0)

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
				function(x,y)
				pygame.draw.rect(win, colors[cell], pygame.Rect(9*x+1, 9*y+1, 8, 8))

				x += 1
			y += 1

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				mouse_pos = pygame.mouse.get_pos()
				mouse_pos_x, mouse_pos_y = mouse_pos

				if mouse_pos_x> 0 and mouse_pos_x < WindowXSize and mouse_pos_y> 0 and mouse_pos_y < WindowYSize:
					mouse_cell_x = (mouse_pos_x - 1) // 9
					mouse_cell_y = (mouse_pos_y - 1) // 9
					row = cells[mouse_cell_y]
					
					if event.key == pygame.K_1:
						row[mouse_cell_x] = 1

					if event.key == pygame.K_0:
						row[mouse_cell_x] = 0
					
			if event.type == pygame.QUIT:
				run = False

		clock.tick(20)

		pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
    main()