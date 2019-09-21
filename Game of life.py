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

listofcoord = []

def showGrid():
    for i in range(22):
        print(grid[i])
    print('')
    #return True

def placeCell():
    fh = open("cross.txt", "r")
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
    showGrid()
    #print(content)

    fh.close()

'''''
def neighborCounter():
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
'''
def GameOfLife():
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
                #print(a,b,"has", neighbor, "neighbors")
    if neighbor >= 1: #killer
        grid[a][b] = 0
    if neighbor <= 4:
        grid[a][b] = 0
    if (neighbor == 2 or neighbor == 3) and grid[a][b] == 1:
        grid[a][b] = 1
    if grid[a][b] == 0 and neighbor == 3: #populator
        grid[a][b] == 1
    neighbor = 0
            if a == 0 and b == 0: #up left
                if grid[a][b+1] == 1:
                    neighbor += 1
                if grid[a+1][b] == 1:
                    neighbor += 1
                if grid[a+1][b+1] == 1:
                    neighbor += 1
                #print(a, b, "has", neighbor, "neighbors")
    if neighbor >= 1:
        grid[a][b] = 0
    if neighbor <= 4:
        grid[a][b] = 0
    if (neighbor == 2 or neighbor == 3) and grid[a][b] == 1:
        grid[a][b] = 1
    if grid[a][b] == 0 and neighbor == 3: #populator
        grid[a][b] == 1
    neighbor = 0
            if a == 0 and b == 20: #up right
                if grid[a][b-1] == 1:
                    neighbor += 1
                if grid[a+1][b] == 1:
                    neighbor += 1
                if grid[a+1][b-1] == 1:
                    neighbor += 1
                #print(a, b, "has", neighbor, "neighbors")
    if neighbor >= 1:
        grid[a][b] = 0
    if neighbor <= 4:
        grid[a][b] = 0
    if (neighbor == 2 or neighbor == 3) and grid[a][b] == 1:
        grid[a][b] = 1
    if grid[a][b] == 0 and neighbor == 3: #populator
        grid[a][b] == 1
    neighbor = 0
            if a == 20 and b == 0: #down left
                if grid[a-1][b+1] == 1:
                    neighbor += 1
                if grid[a-1][b] == 1:
                    neighbor += 1
                if grid[a][b+1] == 1:
                    neighbor += 1
                #print(a, b, "has", neighbor, "neighbors")
    if neighbor >= 1:
        grid[a][b] = 0
    if neighbor <= 4:
        grid[a][b] = 0
    if (neighbor == 2 or neighbor == 3) and grid[a][b] == 1:
        grid[a][b] = 1
    if grid[a][b] == 0 and neighbor == 3: #populator
        grid[a][b] == 1
    neighbor = 0
            if a == 20 and b == 20: #down right
                if grid[a][b-1] == 1:
                    neighbor += 1
                if grid[a-1][b] == 1:
                    neighbor += 1
                if grid[a-1][b-1] == 1:
                    neighbor += 1
                #print(a, b, "has", neighbor, "neighbors")
    if neighbor >= 1:
        grid[a][b] = 0
    if neighbor <= 4:
        grid[a][b] = 0
    if (neighbor == 2 or neighbor == 3) and grid[a][b] == 1:
        grid[a][b] = 1
    if grid[a][b] == 0 and neighbor == 3: #populator
        grid[a][b] == 1
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
                #print(a, b, "has", neighbor, "neighbors")
    if neighbor >= 1:
        grid[a][b] = 0
    if neighbor <= 4:
        grid[a][b] = 0
    if (neighbor == 2 or neighbor == 3) and grid[a][b] == 1:
        grid[a][b] = 1
    if grid[a][b] == 0 and neighbor == 3: #populator
        grid[a][b] == 1
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
                #print(a, b, "has", neighbor, "neighbors")
    if neighbor >= 1:
        grid[a][b] = 0
    if neighbor <= 4:
        grid[a][b] = 0
    if (neighbor == 2 or neighbor == 3) and grid[a][b] == 1:
        grid[a][b] = 1
    if grid[a][b] == 0 and neighbor == 3: #populator
        grid[a][b] == 1
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
                #print(a, b, "has", neighbor, "neighbors")
    if neighbor >= 1:
        grid[a][b] = 0
    if neighbor <= 4:
        grid[a][b] = 0
    if (neighbor == 2 or neighbor == 3) and grid[a][b] == 1:
        grid[a][b] = 1
    if grid[a][b] == 0 and neighbor == 3: #populator
        grid[a][b] == 1
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
                #print(a, b, "has", neighbor, "neighbors")
    if neighbor >= 1:
        grid[a][b] = 0
    if neighbor <= 4:
        grid[a][b] = 0
    if (neighbor == 2 or neighbor == 3) and grid[a][b] == 1:
        grid[a][b] = 1
    if grid[a][b] == 0 and neighbor == 3: #populator
        grid[a][b] == 1
    neighbor = 0
'''
'''
def GameOfLife():
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
            elif a == 0 and b == 0:  # up left
                if grid[a][b + 1] == 1:
                    neighbor += 1
                if grid[a + 1][b] == 1:
                    neighbor += 1
                if grid[a + 1][b + 1] == 1:
                    neighbor += 1
            elif a == 0 and b == 20: #up right
                if grid[a][b-1] == 1:
                    neighbor += 1
                if grid[a+1][b] == 1:
                    neighbor += 1
                if grid[a+1][b-1] == 1:
                    neighbor += 1
            elif a == 20 and b == 0: #down left
                if grid[a-1][b+1] == 1:
                    neighbor += 1
                if grid[a-1][b] == 1:
                    neighbor += 1
                if grid[a][b+1] == 1:
                    neighbor += 1
            elif a == 20 and b == 20: #down right
                if grid[a][b-1] == 1:
                    neighbor += 1
                if grid[a-1][b] == 1:
                    neighbor += 1
                if grid[a-1][b-1] == 1:
                    neighbor += 1
            elif a == 0 and 1 <= b <= 19: #up
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
            elif a == 20 and 1 <= b <= 19: #down
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
            elif b == 20 and 1 <= a <= 19: #right
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
            elif b == 0 and 1 <= a <= 19: #left
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

'''

def GameOfLife(a,b,neighbor):
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
        print(a, b, "has", neighbor, "neighbors")
        #killer(a, b, neighbor)
        #return (a, b, neighbor)
    if a == 0 and b == 0:  # up left
        if grid[a][b + 1] == 1:
            neighbor += 1
        if grid[a + 1][b] == 1:
            neighbor += 1
        if grid[a + 1][b + 1] == 1:
            neighbor += 1
        print(a, b, "has", neighbor, "neighbors")
        #killer(a, b, neighbor)
        #return (a, b, neighbor)
    if a == 0 and b == 20: #up right
        if grid[a][b-1] == 1:
            neighbor += 1
        if grid[a+1][b] == 1:
            neighbor += 1
        if grid[a+1][b-1] == 1:
            neighbor += 1
        print(a, b, "has", neighbor, "neighbors")
        #killer(a, b, neighbor)
        #return (a, b, neighbor)
    if a == 20 and b == 0: #down left
        if grid[a-1][b+1] == 1:
            neighbor += 1
        if grid[a-1][b] == 1:
            neighbor += 1
        if grid[a][b+1] == 1:
            neighbor += 1
        print(a, b, "has", neighbor, "neighbors")
        #killer(a, b, neighbor)
        #return (a, b, neighbor)
    if a == 20 and b == 20: #down right
        if grid[a][b-1] == 1:
            neighbor += 1
        if grid[a-1][b] == 1:
            neighbor += 1
        if grid[a-1][b-1] == 1:
            neighbor += 1
        print(a, b, "has", neighbor, "neighbors")
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
        print(a, b, "has", neighbor, "neighbors")
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
        print(a, b, "has", neighbor, "neighbors")
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
        print(a, b, "has", neighbor, "neighbors")
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
        print(a, b, "has", neighbor, "neighbors")
        #killer(a, b, neighbor)
        #return(a,b,neighbor)
    #print(a, b, "has", neighbor, "neighbors")
    #print(a,b)

def killer(a,b,neighbor):
    if grid[a][b] == 1 and neighbor >= 1:
        grid[a][b] = 0
    if grid[a][b] == 1 and neighbor <= 4:
        grid[a][b] = 0
    if grid[a][b] == 1 and (neighbor == 2 or neighbor == 3):
        grid[a][b] = 1
    if grid[a][b] == 0 and neighbor == 3:  # populator
        grid[a][b] = 1
    else:
        grid[a][b] = grid[a][b]

    #print(a,b,neighbor)

'''
            if grid[a][b] == 1 and neighbor >= 1:
                grid[a][b] = 0
            elif grid[a][b] == 1 and neighbor <= 4:
                grid[a][b] = 0
            elif grid[a][b] == 1 and (neighbor == 2 or neighbor == 3):
                grid[a][b] = 1
            elif grid[a][b] == 0 and neighbor == 3:  # populator
                grid[a][b] == 1
                neighbor = 0
            #time.sleep(3)
            print(grid[0])
            print(grid[1])
            print(grid[2])
            print(grid[3])
            print(grid[4])
            print(grid[5])
            print(grid[6])
            print(grid[7])
            print(grid[8])
            print(grid[9])
            print(grid[10])
            print(grid[11])
            print(grid[12])
            print(grid[13])
            print(grid[14])
            print(grid[15])
            print(grid[16])
            print(grid[17])
            print(grid[18])
            print(grid[19])
            print(grid[20])
            print('')
'''



showGrid() #shows empty grid
placeCell() #loads cell location depending on .txt
for i in range(21): #first check aka GENERATION 0
    for o in range(21):
        GameOfLife(i,o,0)
        #print(i,o,neighbor)


