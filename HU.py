import random
from tkinter import W

field =  [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]

x = ...

def scanfornull(fts):
    for i in range(4):
        for j in range(4):
            if(fts[i][j] == 0): 
                return True
    return False

def spawnbase():
    x = random.randint(0, 15)
    if field[int(x/4)][x%4] == 0:
        field[int(x/4)][x%4] = 2
    else:
        spawnbase()

spawnbase()
print(field)

running = True

def move(diraxis):
    if diraxis.lower() == 'w':
        for i in range(4):
            for j in range(4):
                if i != 0 and field[i][j]!=0 :
                    if(field[i-1][j] == field [i][j]):
                        field [i-1][j] *= 2
                        field [i][j] = 0
                    elif(field[i-1][j] == 0):
                        field[i-1][j] = field[i][j]
                        field[i][j] = 0
                        print('done')
    elif diraxis.lower() == 's':
        None
    elif diraxis.lower() == 'a':
        None
    elif diraxis.lower() == 'd':
        None
    if scanfornull(field): spawnbase()

while running:
    move(input())
    print(field)


