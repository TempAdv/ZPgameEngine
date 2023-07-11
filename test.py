from ZP import *

colors = {1:'#202000',
          2:'#A0A000',
		  3:'#101010',
		  4:'#A01010'}



def passFun(cells, cellsBuffer, x,y):
	neighbours = count8(cells,x,y,4)
	if neighbours == 3:
		cellsBuffer[y][x] = 4

def builder(cells, cellsBuffer, x,y):
	if y > 0 and y < 49:
		row = cells[y-1]
		row2 = cells[y+1]
		if row[x] == 2 and row2[x] == 1:
			row3 = cellsBuffer[y+1]
			row3[x] = 2
		if row2[x] == 2 and row[x] == 1:
			row3 = cellsBuffer[y-1]
			row3[x] = 2

	if x > 0 and x < 49:
		row = cells[y]
		row2 = cellsBuffer[y]
		if row[x-1] == 2 and row[x+1] == 1:
			row2[x+1] = 2
		if row[x+1] == 2 and row[x-1] == 1:
			row2[x-1] = 2

def block(cells, cellsBuffer, x,y):
	pass

def duplicat(cells, cellsBuffer, x,y):

	neighbours = count8(cells,x,y,4)
	if neighbours != 3 and neighbours != 2:
		cellsBuffer[y][x] = 1

updateFunctions = {
	1:passFun,
	2:builder,
	3:block,
	4:duplicat
	}

main(colors,updateFunctions)
