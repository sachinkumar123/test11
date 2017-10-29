Read me file for bfs,dfs,ucs,bds

Give the numbers one by one seperated with comma... 

input:
4,1,2,7,5,3,8,6,b

output:
(prints the path in the tree)(reverse)
['1', '2', '3', '4', '5', '6', '7', '8', 'b']         ^
['1', '2', '3', '4', '5', 'b', '7', '8', '6']         |
['1', '2', 'b', '4', '5', '3', '7', '8', '6']         |
['1', 'b', '2', '4', '5', '3', '7', '8', '6']         ^
['b', '1', '2', '4', '5', '3', '7', '8', '6']         |
['4', '1', '2', 'b', '5', '3', '7', '8', '6']         |
['4', '1', '2', '7', '5', '3', 'b', '8', '6']         ^
['4', '1', '2', '7', '5', '3', '8', 'b', '6']         |
['4', '1', '2', '7', '5', '3', '8', '6', 'b'](input)  |

no of steps 164

Here,164 is total no of steps taken(while loop iterations)

Requirements:Python 2.7
