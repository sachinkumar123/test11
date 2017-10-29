import copy
import time
g=[]
def check1(l):                   # check function for immediate input
    count=0
    for i in range(0,9):
        if str(l[i])==str(i+1):
            count=count+1
    #print count
    if count==8:
        return 1
    else:
        return 0

def check(closed1,closed2):          # check function for finding common list between two closed queues
    for i in closed1:
	if i in closed2:
		global g
		g=copy.deepcopy(i)
		#print g
		return 1
    
def bfs(v,flag,parent,k1,k2):               # Function that runs bfs to processes the node and adds neighbour nodes into queue 
    n=[]
    d=[]
    d=v.pop(0)
    k1.pop(0)
    k2.append(d)
    ind=d.index('b')
#    print "index"
 
   # print d
    x=ind%3             # returns columun of blank
   # print x
    z=ind/3            # returns row of blank
       # below code is pushing neighbour or child nodes into queue
    if x+1<=2:                      #Moves blank to right
        n=copy.deepcopy(d)                           
#	print x+1
        p=z*3+x+1
	#print n
        temp=n[p]
        n[p]='b'
        n[ind]=temp
        if n not in flag:
		k1.append(n)
                v.append(n)
                flag.append(n)
                parent.update({str(n):str(d)})
        #print n
    if z+1<=2:             # moves blank to down
        n=copy.deepcopy(d) 
        a=(z+1)*3+x
        temp=n[a]
        n[a]='b'
        n[ind]=temp
        if n not in flag:
		k1.append(n)
                v.append(n)
                flag.append(n)
                parent.update({str(n):str(d)})
        #print n

    if x-1>=0:             # moves blank to left
        n=copy.deepcopy(d)
        a=z*3+x-1
        temp=n[a]
        n[a]='b'
        n[ind]=temp
        if n not in flag:
		k1.append(n)
                v.append(n)
                flag.append(n)
                parent.update({str(n):str(d)})
        #print n
    
    if z-1>=0:             # moves blank to up
        n=copy.deepcopy(d)
        a=(z-1)*3+x
        temp=n[a]
        n[a]='b'
        n[ind]=temp
        if n not in flag:
		k1.append(n)
                v.append(n)
                flag.append(n)
                parent.update({str(n):str(d)})
        #print n
    
    
    return k1,k2,v,flag,parent                     # returns parent list , open and closed lists ,
l=[]
m=[]
flag=[]           # 
flag2=[]          # 
parent2={}
m2=[]
closed1=[]        # closed lists for making it as flag for processed list
closed2=[]        # 
op1=[]
op2=[]
n=0
parent={}
inpu = raw_input()                          # input as string
start_time = time.time()
l=inpu.split(',')                   # appending input as list
#for i in range(0,9):
 #   l.append(raw_input())
n=check1(l)
m.append(l)
op1.append(l)
o=['1','2','3','4','5','6','7','8','b']
op2.append(o)
m2.append(o)
flag.append(l)
if n==1:
    print "solved"+str(l)

elif n==0:
    v=[]
    v2=[]
    count=0
    while len(m)!=0 and len(m2)!=0:        
        op1,closed1,m,flag,parent=copy.deepcopy(bfs(m,flag,parent,op1,closed1))  #     Processing BFS from first node(input node) 
	op2,closed2,m2,flag2,parent2=copy.deepcopy(bfs(m2,flag2,parent2,op2,closed2)) # Processing BFS from target node to front
	n=check(closed1,closed2)
        if n==1:
            print "solved"
            break
        count=count+1

f=copy.deepcopy(str(g))
jk=copy.deepcopy(str(g))
kkr=[]
o1=str(['1','2','3','4','5','6','7','8','b'])
print o1
while True:                                    # Printing the path between input and destination
	if parent2[f]==str(o1):
		break
	else:
		kkr.append(parent2[f])
		f=parent2[f]
	
while len(kkr)>0:
	ph=[]
	ph=kkr.pop()
	print ph


print g
while True:
	if parent[jk]==str(l):
		break
	else:
		print parent[jk]
		jk=parent[jk]
print l	 
k=time.time()-start_time             # returns execution time after taking input
print "no of steps :"+str(count)
print "time: "+str(k)+" seconds"	
