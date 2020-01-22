from time import time
from random import randrange

class TractionTest():

	max_range = 1400
	matrix = []
	def __init__(self):
		s = time()
		row = []
		for i in range(self.max_range):
			for j in range(self.max_range):
				row.append(float(randrange(0,10000)*3.141982))
			self.matrix.append(row.copy())
			row.clear()
		print(f"Test Case Created in -> {time()-s}s")


	def getTestCase(self):
		#print(self.matrix)
		return self.matrix,self.max_range







if __name__ == "__main__": # Do Not Copy this

# First Import this code in ur code as package as "from TractionTest import *+"

# COPY These two lines AND paste in ur code without Tabs
	t = TractionTest()
	t.getTestCase()