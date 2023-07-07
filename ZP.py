
import pygame


def main():
	colors = {0:'#A0A000'

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

				pygame.draw.rect(win, colors[cell], pygame.Rect(9*x+1, 9*y+1, 8, 8))

				x+= 1
			y += 1

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		clock.tick(50)

		pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
    main()