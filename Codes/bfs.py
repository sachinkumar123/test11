import copy
import time
def check(l):                                 #check function to tell whether node(configuration ) reached desired destination
    count=0
    for i in range(0,9):
        if str(l[i])==str(i+1):
            count=count+1
    #print count
    if count==8:
        return 1
    else:
        return 0

def bfs(v,flag,parent):                           # BFS Algorithm
    n=[]
    d=[]
    d=v.pop(0)
    ind=d.index('b')
    x=ind%3            # retuns column of blank pos
    z=ind/3           # returns row of blank pos
  
    if x+1<=2:                                                                    # appending neighbours of parent i.e child nodes into queue
        n=copy.deepcopy(d)                              
        a=z*3+x+1                          # moves blank to right
        temp=n[a]
        n[a]='b'
        n[ind]=temp
        if n not in flag:
                v.append(n)
                flag.append(n)
                parent.update({str(n):str(d)})             #updating parent
        #print n
    if z+1<=2:
        n=copy.deepcopy(d)              # moves blank to down
        a=(z+1)*3+x
        temp=n[a]
        n[a]='b'
        n[ind]=temp
        if n not in flag:
                v.append(n)
                flag.append(n)
                parent.update({str(n):str(d)})
        #print n
    if x-1>=0:                       # moves blank to left
        n=copy.deepcopy(d)
        a=z*3+x-1
        temp=n[a]
        n[a]='b'
        n[ind]=temp
        if n not in flag:
                v.append(n)
                flag.append(n)
                parent.update({str(n):str(d)})
    
	    #print n
    if z-1>=0:                         #moves blank to up
        n=copy.deepcopy(d)
        a=(z-1)*3+x
        temp=n[a]
        n[a]='b'
        n[ind]=temp
        if n not in flag:
                v.append(n)
                flag.append(n)
                parent.update({str(n):str(d)})
        #print n
    
    
    return v,flag,parent
        
    
l=[]
m=[]
flag=[]
n=0
parent={}
inpu = raw_input()          # taking input as string
l=inpu.split(',')
#for i in range(0,9):
 #   l.append(raw_input())
start_time = time.time()
n=check(l)
m.append(l)
flag.append(l)
if n==1:
    print "solved"+str(l)

elif n==0:
    v=[]
    count=0
    while(len(m)!=0):
        v=m[0]
        #print v
        n=check(v)
        if n==1:
            print "solved"              # breaking when problem is solved
            break
	count=count+1
        m,flag,parent=copy.deepcopy(bfs(m,flag,parent))   # Calling BFS function
        #print m
o=str(['1','2','3','4','5','6','7','8','b'])
print o

while (True):                     # printing path between given node to destination
    if parent[o]==str(l):
        break
    else:
        print parent[o]
        o=parent[o]
k=time.time()-start_time                       # returns time of execution after taking the input
print l
print "time: "+str(k)
print "no of steps "+str(count)+" seconds"
