# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:11:23 2019

@author: Steven Kyle Y Esguerra SN: 2019#####
"""

import time as stib #stib.sleeps needed
import sys

'''
Main grid
'''
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

'''
Temporary grid (for updating)
'''
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

'''
Function to print the grid
'''
def showGrid(): #shows the grid
    for i in range(0,21):
        #print(grid[i])
        a = ''.join(map(str, grid[i]))
        print(a)
    #return True

'''
Function to place the coordinates based on the TXT file. File handling included.
Currently has:
Tumbler, Exploder, Ten Cell Row, Cross, Small Exploder, and Corners
Also has Glider (custom)
'''
def placeCell(): #places the cell based on the txt
    print("Preset files")
    print("---------------")
    print("[1] Corners")
    print("[2] Cross")
    print("[3] Exploder")
    print("[4] Glider")
    print("[5] Small Exploder")
    print("[6] Ten Cell Row")
    print("[7] Tumbler")
    print("[8] Exit App")
    print("---------------")
    while True:
        try:
            preset = int(input("Which file to load?: "))
            print("--------------")
            break
        except ValueError:
	        print("Please enter valid input")
    if preset == 1:
	    file_name="corners.txt"
    if preset == 2:
	    file_name="cross.txt"
    if preset == 3:
	    file_name="exploder.txt"
    if preset == 4:
	    file_name="glider.txt"
    if preset == 5:
	    file_name="small_exploder.txt"
    if preset == 6:
	    file_name="ten_cell_row.txt"
    if preset == 7:
	    file_name="tumbler.txt"
    if preset == 8:
	    sys.exit
	
    fh = open(file_name, "r") #load the appopriate text file here
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
Function whose sole purpose is to count the number of neighbor of an specific cell. Just used in debugging
'''
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

'''
Function the implemented the rules of game of life, neighbor counter is also implemented
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

'''
Function for killing/populating an specific cell
'''
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
	
'''
Updates the main grid 
'''
def gridUpdate(): #updates the base grid
    for i in range(0,21):
        for o in range(0,21):
            grid[i][o] = newgrid[i][o]


'''
Whole sequence, change z range to how many iteration to be done
11 = 10 generation
'''
print('---------------')
#showGrid() #shows empty grid
print("WELCOME TO JOHN CONWAY'S GAME OF LIFE")
print("written by st0bb3n on python 3")
print('---------------')
stib.sleep(1)
placeCell()
showGrid()
while True:
    try:
        print("---------------")
        ii = int(input("How many generations do you want? 0 for infinite: "))
        print('---------------')
        break
    except ValueError:
	    print("Please enter a valid integer")
stib.sleep(1)
print('---------------')

if ii > 0:
    for z in range(ii): #shows how many generation to be made
        for i in range(21):
            for o in range(21):
                GameOfLife(i,o)
        gridUpdate()
        showGrid()
        print('---------------')
        stib.sleep(1)
    print("Simulation Done!")
if ii == 0:
    while True: #shows how many generation to be made
        for i in range(21):
            for o in range(21):
                GameOfLife(i,o)
        gridUpdate()
        showGrid()
        print('---------------')
        print('Ctrl + C to terminate')
        print('---------------')
        stib.sleep(1)



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
