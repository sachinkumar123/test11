import copy
import time
def check(l):                                 #check function that retuns 1 when destination is reached
    count=0
    for i in range(0,9):
        if str(l[i])==str(i+1):
            count=count+1
    #print count
    if count==8:
        return 1
    else:
        return 0

def dfs(v,flag,parent):                        # DFS Algorithm
    n=[]
    d=[]
    d=v[len(v)-1]
    ind=d.index('b')
    x=ind%3       # returns column of blank
    z=ind/3 # returns row of blank
    g=0                      
    if x+1<=2 and g==0:           # Moves blank to right
        n=copy.deepcopy(d)
        a=z*3+x+1
        temp=n[a]
        n[a]='b'
        n[ind]=temp
        if n not in flag:
                v.append(n)
                flag.append(n)
                g=1
		parent.update({str(n):str(d)})
    if z+1<=2 and g==0:             # Moves blank to down
        n=copy.deepcopy(d)
        a=(z+1)*3+x
        temp=n[a]
        n[a]='b'
        n[ind]=temp
        if n not in flag:
                v.append(n)
                flag.append(n)
                g=1
		parent.update({str(n):str(d)})
        #print n
    if z-1>=0 and g==0:              # Moves blank to up
        n=copy.deepcopy(d)
        a=(z-1)*3+x
        temp=n[a]
        n[a]='b'
        n[ind]=temp
        if n not in flag:
                v.append(n)
                flag.append(n)
                g=1
		parent.update({str(n):str(d)})
        #print n
    if x-1>=0 and g==0:           # moves blank to left
        n=copy.deepcopy(d)
        a=z*3+x-1
        temp=n[a]
        n[a]='b'
        n[ind]=temp
        if n not in flag:
                v.append(n)
                flag.append(n)
                g=1
		parent.update({str(n):str(d)})
        #print n
    
        #print n
    if g==0:                        # poping of stack
        v.pop()
    return v,flag,parent
        
        
    
l=[]
m=[]
flag=[]
n=0

inpu = raw_input()
start_time = time.time()
l=inpu.split(',')
parent={}
#for i in range(0,9):
 #   l.append(raw_input())
n=check(l)
m.append(l)
flag.append(l)
if n==1:
    print "solved"+str(l)

elif n==0:
    v=[]
    count=0
    while(len(m)!=0):
        v=m[len(m)-1]
        #print v
        n=check(v)
        if n==1:
            print "solved"                      # Prints if it is soved
            break
        m,flag,parent=copy.deepcopy(dfs(m,flag,parent))             # calling dfs function
	count=count+1
        #print m

o=str(['1','2','3','4','5','6','7','8','b'])

print o



while (True):                                 # printing the path between the origin and destination

    if parent[o]==str(l):

        break

    else:

        print parent[o]

        o=parent[o]

print l
k=time.time()-start_time                       # returns time of execution after taking the input 
print "no of steps "+str(count)
print "time: "+str(k)+" seconds"
