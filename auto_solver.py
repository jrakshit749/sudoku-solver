import pyautogui as pg #For automation
import numpy as np
import time

grid = []
#The while loop is to accept inputs from the user Row by Row and store is aas an Integer as well as a String in 2 different lists
while True:
    row = list(input('Row: '))
    ints = []
    for n in row:
        ints.append(int(n))
    grid.append(ints)     #Integer List

    if(len(grid))==9:
        break
    print('Row ' + str(len(grid)) + ' Complete') 

time.sleep(5)

def Print(matrix):
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])
    for lists in final:
        for num in lists:
            str_fin.append(str(num)) #String List

    counter =[]
#The automation part where we tell the program what to do with the grid of sudoku
    for num in str_fin:
        pg.press(num) #Enters a possible number
        pg.hotkey('right') #moves to the next right space
        counter.append(num)
        if len(counter)%9 == 0:
            pg.hotkey('down') #moves to the next bottom space
            for i in range(9):
                pg.hotkey('left') #moves to the previous left space


#take input as column, row and a number to check if the number is possible in that specified space
def possible(y, x, n):
    global grid
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3) * 3
    y0 = (y//3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

# possible(4,4,5) --Just a checker for the default sudoku grid

#This function actually solves the sudoku
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    Print(grid)

solve()