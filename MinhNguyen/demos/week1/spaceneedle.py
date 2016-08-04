def topDome():
	for k in range(0, 4):
		row = ''
		for i in range(0, 9-k*3):
			row += " "
		row += "__/"
		for i in range(0, 3*k):
			row += ":"
		row += "||"
		for i in range(0, 3*k):
			row += ":"
		print row + "\\__"
	row = "|"
	for i in range(0,24):
		row +=  "\""
	print row + "|"
def needle():
	for k in range(0, 3):
		row = ''
		for i in range(0, 12):
			row += " "
		print row + "||"
needle()
topDome()
for i in range(0, 4):
	row = ''
	for k in range(0, i*2):
		row += " "
	row += "\\_"
	for k in range(0, 11-(2*i)):
		row += "/\\"
	print row + "_/"
needle()
for i in range(0, 16):
	row = ''
	for k in range(0, 9):
		row +=" "
	print row + "|%%||%%|"
topDome()

