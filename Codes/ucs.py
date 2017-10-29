import time
import copy
class Node:
	def __init__(self):                       # structured node that has two datatypes
		self.li =[]
		self.cost = 0
def check(l):                         
    count=0                                      #check function that will return 1 when we reach desired configuration 
    for i in range(0,9):
        if str(l[i])==str(i+1):
            count=count+1
    #print count
    if count==8:
        return 1
    else:
        return 0

def bfs(v,flag,parent):                          # BFS algorithm
    temp1=[]
    n=[]
    d=[]
    d=v.pop(0)
    ind=d.index('b')                                   
    x=ind%3          # to find column of blank position 
    z=ind/3 # to fin row of blank position
    if x+1<=2:                               # code below is appending neighbours of the taken node . and neighbours are identified w.r.t postion
        n=copy.deepcopy(d)
        a=z*3+x+1
        temp=n[a]
        n[a]='b'                         # Moving blank to right
        n[ind]=temp
	e=Node()
	h=0
	if temp<='3':
                h=1
        elif temp<='6':
                h=2
        else:
                h=3
        e.cost=h
	e.li=copy.deepcopy(n)
	
		
        if n not in flag:
                #v.append(n)
		temp1.append(e)
                flag.append(n)
                parent.update({str(n):str(d)})
        #print n
    if z+1<=2:                                  # moving blank to down
        n=copy.deepcopy(d)
        a=(z+1)*3+x
        temp=n[a]
        n[a]='b'
	h=0
        n[ind]=temp
	e=Node()
	if temp<='3':
                h=1
        elif temp<='6':
                h=2
        else:
                h=3
        e.cost=h
	e.li=copy.deepcopy(n)
	
		
        if n not in flag:
		temp1.append(e)
              #  v.append(n)
                flag.append(n)
                parent.update({str(n):str(d)})
        #print n
    if x-1>=0:                       # moving blank left
	n=copy.deepcopy(d)
        a=z*3+x-1
        temp=n[a]
        n[a]='b'
        n[ind]=temp
	e=Node()
	h=0
	if temp<='3':
		h=1
	elif temp<='6':
		h=2
	else:
		h=3
	e.cost=h	
	e.li=copy.deepcopy(n)
	
		
        if n not in flag:
                #v.append(n)
		temp1.append(e)
                flag.append(n)
                parent.update({str(n):str(d)})
        #print n
    if z-1>=0:                                         #moving blank to up
        n=copy.deepcopy(d)
        a=(z-1)*3+x
        temp=n[a]
	h=0
        n[a]='b'
        n[ind]=temp
	e=Node()
        if temp<='3':
                h=1
        elif temp<='6':
                h=2
        else:
                h=3
        e.cost=h
		
	e.li=copy.deepcopy(n)
	
		
        if n not in flag:
               # v.append(n)
		temp1.append(e)
                flag.append(n)
                parent.update({str(n):str(d)})
        #print n
   
    temp1.sort(key=lambda e:e.cost)          # Sorting the child nodes of the parent node w.r.t cost of moving element
    lu=len(temp1)
    p=Node()
    p1=[]
    while(lu > 0):
	p=temp1.pop(0)
	p1=copy.deepcopy(p.li)
	v.append(p1)
	lu=len(temp1)
		
		
	
		
    
    return v,flag,parent
        
        
    
l=[]
m=[]
flag=[]
n=0
parent={}
inpu = raw_input()
start_time = time.time()  # time stamp
l=inpu.split(',')
#for i in range(0,9):
#    l.append(raw_input())
n=check(l)
m.append(l)
flag.append(l)
if n==1:
    print "solved"+str(l)

elif n==0:
    v=[]
    count =0
    while(len(m)!=0):
        v=m[0]
        #print v
        n=check(v)
        if n==1:
            print "solved"
            break
        m,flag,parent=copy.deepcopy(bfs(m,flag,parent))      # calling bfs algorithm
        count=count+1
        #print m
o=str(['1','2','3','4','5','6','7','8','b'])
#print o in parent
#print g
while (True):                       # printing path between the given node and desired node.
    if parent[o]==str(l):
        break
    else:

        	print parent[o]
        	o=parent[o]
print l
k=time.time()-start_time                          # Time stamp that return execution time after input is given
print "no of steps :"+str(count)
print "time: "+str(k)+" seconds"
