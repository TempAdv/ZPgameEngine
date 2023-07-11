from ZP import *

colors = {1:'#202000',
          2:'#A0A000',
		  3:'#101010'}



def passFun(cells, cellsBuffer, x,y):
	pass

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

def rightBuild(cells, cellsBuffer, x,y):
	pass
	#row = cells[y]
	#row[x] = random.randint(0,1)

updateFunctions = {
	1:passFun,
	2:builder,
	3:block,
	4:rightBuild
	}

main(colors,updateFunctions)
