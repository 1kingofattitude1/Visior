from astar_python.astar import Astar
from random import randrange
import time as t

mat=[[0,1,2,0,0,0,0,0],
			[0,0,0,7,4,0,0,0],
			[0,0,0,0,0,7,1,0],
			[0,0,0,0,0,0,0,3],
			[0,0,0,0,0,0,0,2],
			[0,0,0,0,0,0,0,5],
			[0,0,0,0,0,0,0,12],
			[0,0,0,0,0,0,0,0]]

#generating matrix
row = []
col = []
for i in range(100):
	for j in range(100):
		row.append(randrange(0,100))
	col.append(row.copy())
	row.clear()


start_time = t.time()
astar = Astar(col)
result = astar.run([50,50],[75,75])

print(result)

print("Time taken in ->%f sec"%(t.time()-start_time))