#game of life

grid = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

newgrid = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

listofcoord = []

def showGrid(): #shows the grid
    for i in range(0,21):
        print(grid[i])
    print('')
    #return True

def placeCell(): #places the cell based on the txt
    fh = open("cross.txt", "r") #load the appopriate text file here
    content = fh.read().splitlines()
    for i in range(len(content)):
        coord = (content[i]).split()
        listofcoord.append(coord)
        #print(coord)
    #print(listofcoord)
    for elementno in range(1,int(listofcoord[0][0]) + 1):
        row = int(listofcoord[elementno][0])
        column = int(listofcoord[elementno][1])
        grid[row][column] = 1
        #print(row,column)
    #showGrid()
    #print(content)

    fh.close()

'''
def neighborCounter():  #Neighbor Counter for debugging 
    neighbor = 0
    for a in range(0,21): #without corners its 1,20
        for b in range (0,21):
            #print(a, b)
            if (a > 0 and b > 0) and (a < 20 and b < 20): #all in the middle
                if grid[a-1][b-1] == 1:
                    neighbor += 1
                if grid[a-1][b] == 1:
                    neighbor += 1
                if grid[a-1][b+1] == 1:
                    neighbor += 1
                if grid[a][b-1] == 1:
                    neighbor += 1
                if grid[a][b+1] == 1:
                    neighbor += 1
                if grid[a+1][b-1] == 1:
                    neighbor += 1
                if grid[a+1][b] == 1:
                    neighbor += 1
                if grid[a+1][b+1] == 1:
                    neighbor += 1
                print(a,b,"has", neighbor, "neighbors")
                neighbor = 0
            if a == 0 and b == 0: #up left
                if grid[a][b+1] == 1:
                    neighbor += 1
                if grid[a+1][b] == 1:
                    neighbor += 1
                if grid[a+1][b+1] == 1:
                    neighbor += 1
                print(a, b, "has", neighbor, "neighbors")
                neighbor = 0
            if a == 0 and b == 20: #up right
                if grid[a][b-1] == 1:
                    neighbor += 1
                if grid[a+1][b] == 1:
                    neighbor += 1
                if grid[a+1][b-1] == 1:
                    neighbor += 1
                print(a, b, "has", neighbor, "neighbors")
                neighbor = 0
            if a == 20 and b == 0: #down left
                if grid[a-1][b+1] == 1:
                    neighbor += 1
                if grid[a-1][b] == 1:
                    neighbor += 1
                if grid[a][b+1] == 1:
                    neighbor += 1
                print(a, b, "has", neighbor, "neighbors")
                neighbor = 0
            if a == 20 and b == 20: #down right
                if grid[a][b-1] == 1:
                    neighbor += 1
                if grid[a-1][b] == 1:
                    neighbor += 1
                if grid[a-1][b-1] == 1:
                    neighbor += 1
                print(a, b, "has", neighbor, "neighbors")
                neighbor = 0
            if a == 0 and 1 <= b <= 19: #up
                if grid[a][b-1] == 1:
                    neighbor += 1
                if grid[a][b+1] == 1:
                    neighbor += 1
                if grid[a+1][b-1] == 1:
                    neighbor += 1
                if grid[a+1][b] == 1:
                    neighbor += 1
                if grid[a+1][b+1] == 1:
                    neighbor += 1
                print(a, b, "has", neighbor, "neighbors")
                neighbor = 0
            if a == 20 and 1 <= b <= 19: #down
                if grid[a][b - 1] == 1:
                    neighbor += 1
                if grid[a][b + 1] == 1:
                    neighbor += 1
                if grid[a-1][b - 1] == 1:
                    neighbor += 1
                if grid[a-1][b] == 1:
                    neighbor += 1
                if grid[a-1][b + 1] == 1:
                    neighbor += 1
                print(a, b, "has", neighbor, "neighbors")
                neighbor = 0
            if b == 20 and 1 <= a <= 19: #right
                if grid[a+1][b-1] == 1:
                    neighbor += 1
                if grid[a-1][b-1] == 1:
                    neighbor += 1
                if grid[a-1][b-1] == 1:
                    neighbor += 1
                if grid[a][b-1] == 1:
                    neighbor += 1
                if grid[a+1][b-1] == 1:
                    neighbor += 1
                print(a, b, "has", neighbor, "neighbors")
                neighbor = 0
            if b == 0 and 1 <= a <= 19: #left
                if grid[a+1][b] == 1:
                    neighbor += 1
                if grid[a-1][b] == 1:
                    neighbor += 1
                if grid[a+1][b+1] == 1:
                    neighbor += 1
                if grid[a][b+1] == 1:
                    neighbor += 1
                if grid[a-1][b+1] == 1:
                    neighbor += 1
                print(a, b, "has", neighbor, "neighbors")
                neighbor = 0
'''

def GameOfLife(a,b): #Game of life mechanics with integrated neighbor counter
    neighbor = 0
    if (a > 0 and b > 0) and (a < 20 and b < 20): #all in the middle
        if grid[a-1][b-1] == 1:
            neighbor += 1
        if grid[a-1][b] == 1:
            neighbor += 1
        if grid[a-1][b+1] == 1:
            neighbor += 1
        if grid[a][b-1] == 1:
            neighbor += 1
        if grid[a][b+1] == 1:
            neighbor += 1
        if grid[a+1][b-1] == 1:
            neighbor += 1
        if grid[a+1][b] == 1:
            neighbor += 1
        if grid[a+1][b+1] == 1:
            neighbor += 1
        #print(a, b, "has", neighbor, "neighbors")
        #killer(a, b, neighbor)
        #return (a, b, neighbor)
    if a == 0 and b == 0:  # up left
        if grid[a][b + 1] == 1:
            neighbor += 1
        if grid[a+1][b] == 1:
            neighbor += 1
        if grid[a+1][b+1] == 1:
            neighbor += 1
        #print(a, b, "has", neighbor, "neighbors")
        #killer(a, b, neighbor)
        #return (a, b, neighbor)
    if a == 0 and b == 20: #up right
        if grid[a][b-1] == 1:
            neighbor += 1
        if grid[a+1][b] == 1:
            neighbor += 1
        if grid[a+1][b-1] == 1:
            neighbor += 1
        #print(a, b, "has", neighbor, "neighbors")
        #killer(a, b, neighbor)
        #return (a, b, neighbor)
    if a == 20 and b == 0: #down left
        if grid[a-1][b+1] == 1:
            neighbor += 1
        if grid[a-1][b] == 1:
            neighbor += 1
        if grid[a][b+1] == 1:
            neighbor += 1
        #print(a, b, "has", neighbor, "neighbors")
        #killer(a, b, neighbor)
        #return (a, b, neighbor)
    if a == 20 and b == 20: #down right
        if grid[a][b-1] == 1:
            neighbor += 1
        if grid[a-1][b] == 1:
            neighbor += 1
        if grid[a-1][b-1] == 1:
            neighbor += 1
        #print(a, b, "has", neighbor, "neighbors")
        #killer(a, b, neighbor)
        #return (a, b, neighbor)
    if a == 0 and 1 <= b <= 19: #up
        if grid[a][b-1] == 1:
            neighbor += 1
        if grid[a][b+1] == 1:
            neighbor += 1
        if grid[a+1][b-1] == 1:
            neighbor += 1
        if grid[a+1][b] == 1:
            neighbor += 1
        if grid[a+1][b+1] == 1:
            neighbor += 1
        #print(a, b, "has", neighbor, "neighbors")
        #killer(a,b,neighbor)
        #return (a, b, neighbor)
    if a == 20 and 1 <= b <= 19: #down
        if grid[a][b - 1] == 1:
            neighbor += 1
        if grid[a][b + 1] == 1:
            neighbor += 1
        if grid[a-1][b - 1] == 1:
            neighbor += 1
        if grid[a-1][b] == 1:
            neighbor += 1
        if grid[a-1][b + 1] == 1:
            neighbor += 1
        #print(a, b, "has", neighbor, "neighbors")
        #killer(a, b, neighbor)
        #return (a, b, neighbor)
    if b == 20 and 1 <= a <= 19: #right
        if grid[a+1][b-1] == 1:
            neighbor += 1
        if grid[a-1][b-1] == 1:
            neighbor += 1
        if grid[a-1][b-1] == 1:
            neighbor += 1
        if grid[a][b-1] == 1:
            neighbor += 1
        if grid[a+1][b-1] == 1:
            neighbor += 1
        #print(a, b, "has", neighbor, "neighbors")
        #killer(a, b, neighbor)
        #return (a, b, neighbor)
    if b == 0 and 1 <= a <= 19: #left
        if grid[a+1][b] == 1:
            neighbor += 1
        if grid[a-1][b] == 1:
            neighbor += 1
        if grid[a+1][b+1] == 1:
            neighbor += 1
        if grid[a][b+1] == 1:
            neighbor += 1
        if grid[a-1][b+1] == 1:
            neighbor += 1
        #print(a, b, "has", neighbor, "neighbors")
        #killer(a, b, neighbor)
        #return(a,b,neighbor)
    #print(a, b, "has", neighbor, "neighbors")
    killer(a, b, neighbor)
    #print(a,b)

def killer(a, b, neighbor):
    if grid[a][b] == 1 and neighbor <= 1:
        newgrid[a][b] = 0
    elif grid[a][b] == 1 and neighbor >= 4:
        newgrid[a][b] = 0
    elif grid[a][b] == 1 and (neighbor == 2 or neighbor == 3):
        newgrid[a][b] = 1
    elif grid[a][b] == 0 and neighbor == 3:  # populator
        newgrid[a][b] = 1
    elif grid[a][b] == 0 and neighbor <= 2:
        newgrid[a][b] = 0
    elif grid[a][b] == 0 and neighbor >= 4:
        newgrid[a][b] = 0
    else:
        newgrid[a][b] = 0
    #print(a,b,neighbor)
    #neighbor = 0
    #return neighbor

def gridUpdate(): #updates the base grid
    for i in range(0,21):
        for o in range(0,21):
            grid[i][o] = newgrid[i][o]

showGrid() #shows empty grid
placeCell() #loads cell location depending on .txt
showGrid()
for z in range(10): #shows how many generation to be made
    for i in range(21):
        for o in range(21):
            GameOfLife(i,o)
    gridUpdate()
    showGrid()
    print('nxtgrid')

'''

FOR DEBUGGING PURPOSES (CODE BELOW)

'''

'''
#showGrid() #shows empty grid
placeCell() #loads cell location depending on .txt
showGrid()
#for z in range(11):
for i in range(21): #first check aka GENERATION 1
    for o in range(21):
        GameOfLife(i,o)
        #if i == 20 and o == 20:
         #   continue
    #print(i,o,neighbor)
    #neighbor = 0
#del grid[:]
gridUpdate()
showGrid()
print('nxtgrid')


for i in range(21): #first check aka GENERATION 2
    for o in range(21):
        GameOfLife(i,o)
#        if i == 20 and o == 20:
 #           continue
    #print(i,o,neighbor)
    #neighbor = 0
#del grid[:]
gridUpdate()
showGrid()
print('nxtgrid')


for i in range(21): #first check aka GENERATION 3
    for o in range(21):
        GameOfLife(i,o)
 #       if i == 20 and o == 20:
  #          continue
    #print(i,o,neighbor)
    #neighbor = 0
#del grid[:]
gridUpdate()
showGrid()
print('nxtgrid')


for i in range(21): #first check aka GENERATION 4
    for o in range(21):
        GameOfLife(i,o)
 #       if i == 20 and o == 20:
  #          continue
    #print(i,o,neighbor)
    #neighbor = 0
#del grid[:]
gridUpdate()
showGrid()
print('nxtgrid')
'''
