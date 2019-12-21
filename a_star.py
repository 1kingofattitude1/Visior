import time as t

graph=[[0,1,2,0,0,0,0,0],
			[0,0,0,7,4,0,0,0],
			[0,0,0,0,0,7,1,0],
			[0,0,0,0,0,0,0,3],
			[0,0,0,0,0,0,0,2],
			[0,0,0,0,0,0,0,5],
			[0,0,0,0,0,0,0,12],
			[0,0,0,0,0,0,0,0]]

h_value={'A':5,'B':6,'Y':8,'X':5,'C':4,'D':15,'E':0}
mapper={'S':0,'A':1,'B':2,'Y':3,'X':4,'C':5,'D':6,'E':7}
revmapper={0:'S',1:'A',2:'B',3:'Y',4:'X',5:'C',6:'D',7:'E'}

distance={}

print("starting point is ->  S")
print("Ending point is ->  E")
print("Node	 H_values")
for i,j in h_value.items():
	print("%s  	 %d"%(i,j))
print("------------------------------------")

def  get_value(keystring):
	sum=0
	for i in range(0,len(keystring)-1):
		sum+=graph[mapper[keystring[i]]][mapper[keystring[i+1]]]
	sum+=h_value[keystring[len(keystring)-1]]
	return sum

def generate_distance(keystring):
	#print("keystring",keystring)
	value=get_value(keystring)
	distance[keystring]=value

def check_row(label):
	rowlabel=label[len(label)-1]
	for i in range(0,8):
		if (graph[mapper[rowlabel]][i]!=0):
			#print("%s -> %s = %d"%(rowlabel,revmapper[i],graph[mapper[rowlabel]][i]))
			generate_distance(label+revmapper[i])
	#print(distance)


start_time = t.time()
check_row('S')
print(distance)
keystr=min(distance,key=lambda k:distance[k])
print("min-> %s = %d"%(keystr,distance[keystr]))
distance.pop(keystr)

while("E" not in keystr):
	check_row(keystr)
	print(distance)
	keystr=min(distance,key=lambda k:distance[k])
	print("min-> %s = %d"%(keystr,distance[keystr]))
	distance.pop(keystr)

print("A * min cost path is -> ",keystr)
print("Time taken in ->%f sec"%(t.time()-start_time))
