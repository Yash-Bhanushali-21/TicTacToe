import pygame
import os
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

os.environ['SDL_VIDEO_WINDOW_POS'] = '400,100'
pygame.init()
display_width = 600
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
caption = pygame.display.set_caption("This is my first try!")
clock = pygame.time.Clock()  # fps
val = False
killed = False
turn=0
declare=''
inputted = []
user_input=''
winner = ' '  # declaration of variables and constants
grid = [[None, None, None], \
        [None, None, None], \
        [None, None, None]]

white = (255, 255, 255)
green = (50, 205, 50)
blue = (0, 0, 255)
red = (255, 0, 0)
bright_green = (127, 255, 0)
yellow = (255, 255, 0)
silver = (192, 192, 192)
purple = (128, 0, 128)
black = (0, 0, 0)
color = [black, green, blue, red, bright_green, yellow, silver, purple, white]

x = 200
y = 200

listdim = [(0, 0, x, y), (x, 0, x, y), (x + y, 0, x, y), (0, y, x, y), (x, y, x, y), (x + y, y, x, y),
           (0, x + y, x, y), (x, x + y, x, y), (x + y, x + y, x, y)]
listdim2=[(0, 0), (x, 0), (x + y,0),(0, y), (x, y), (x + y, y),
           (0, x + y), (x, x + y), (x + y, x + y)]
listdimloop=[(0, x + y, x+2, y/2),(x + y, x + y, x, y/2)]


def indexofrect(r,c):
    if r==0:
        return c
    if r==1:
        return (c+3)
    if r==2:
        return (c+6)

def decisionmaker():
    global winner
    chance = False
    val = True
    up = ''
    if user_input == 'X':
        up == 'O'
    else:
        up = 'X'
    while val is True:
        for i in range(0, 9):  # checking if player may win in next move
            a, b = listdim2[i]
            r, c = check(a, b)
            if grid[r][c] == 'X' or grid[r][c] == 'O':
                continue
            grid[r][c] = up
            predict = gameWon(grid)
            if predict == up:
                print('the player may win at' + str(r) + '' + str(c))
                chance = True
                winner = ''
                grid[r][c] = None
                break
            else:
                grid[r][c] = None
        if chance == True:
            random_num = indexofrect(r, c)
            print(random_num)
            row, col = r, c
        else:
            random_num = random.randint(0, 8)
            (p, q) = listdim2[random_num]
            (row, col) = check(p, q)

        if grid[row][col] == 'X' or grid[row][col] == 'O':
            val = True
        else:
            print(random_num)
            val = False
            button_func(random_num)




rect = []
j = int


def buttondisplay():
    count = 0
    for i in listdim:
        app = pygame.draw.rect(gameDisplay,color[count],i)
        rect.append(app)
        count += 1

def message_display(text,x,y,width,height,col,size):
    smallText = pygame.font.Font("freesansbold.ttf", size)
    TextSurf, TextRect = text_objects(text, smallText,col)  # function for printing X
    TextRect.center = ((x + (width / 2)), (y + (height / 2)))
    update = gameDisplay.blit(TextSurf, TextRect)

def text_objects(text,font,color):
    textSurface = font.render(text,True,color)
    return textSurface, textSurface.get_rect()  # text objects for text font


def O(x, y, width, height):
    smallText = pygame.font.Font("freesansbold.ttf", 60)
    TextSurf, TextRect = text_objects("O", smallText,white)
    TextRect.center = ((x + (width / 2)), (y + (height / 2)))  # function for printing O
    update = gameDisplay.blit(TextSurf, TextRect)


def X(x, y, width, height):
    smallText = pygame.font.Font("freesansbold.ttf", 60)
    TextSurf, TextRect = text_objects("X", smallText,white)  # function for printing X
    TextRect.center = ((x + (width / 2)), (y + (height / 2)))
    update = gameDisplay.blit(TextSurf, TextRect)

def lastpage(declare):
    end=False
    while not end:
        if declare=='X' or declare=='O':
            message_display('the winner is ' + str(declare), 200, 200, 200, 100, bright_green, 30)
        else:
            message_display('This is a tie condition' , 200, 200, 200, 100, bright_green, 30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        pygame.display.update()
    clock.tick(60)


def check(x1, y1):
    if x1 == 0:
        col = 0
    elif x1 == 200:
        col = 1
    else:
        col = 2
    if y1 == 0:
        row = 0
    elif y1 == 200:
        row = 1
    else:
        row = 2
    return (row, col)


def button_func(num):
    global user_input
    (a,b)= listdim2[num]
    (row, col) = check(a, b)
    grid[row][col] = user_input
    print(grid[row][col])
    if user_input == 'X':
        X(listdim[num][0], listdim[num][1], listdim[num][2], listdim[num][3])
        user_input='O'
    else:
        O(listdim[num][0], listdim[num][1], listdim[num][2], listdim[num][3])
        user_input='X'
    pygame.time.wait(500)


def gameWon(grid):
    global winner,tiecall
    count=0

    # check for winning rows
    for row in range(0, 3):
        if ((grid[row][0] == grid[row][1] == grid[row][2]) and \
                (grid[row][0] is not None)):
            # this row won
            winner = grid[row][0]
            break
    # check for winning columns
    for col in range(0, 3):
        if (grid[0][col] == grid[1][col] == grid[2][col]) and \
                (grid[0][col] is not None):
            # this column won
            winner = grid[0][col]
            break

    # check for diagonal winners
    if (grid[0][0] == grid[1][1] == grid[2][2]) and \
            (grid[0][0] is not None):
        # game won diagonally left to right
        winner = grid[0][0]

    if (grid[0][2] == grid[1][1] == grid[2][0]) and \
            (grid[0][2] is not None):
        # game won diagonally right to left
        winner = grid[0][2]
    for row in range(0, 3):
        if (grid[row][0] is not None and grid[row][1] is not None and grid[row][2] is not None):
            count += 1
    if count==3 and winner=='':
        return 'tie'
    else:
        return winner


firstlooprect=[]

def mainloop():
    buttondisplay()
    global turn
    crashed=False
    while not crashed:  # main loop for only 9 moves
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                root = tk.Tk()
                root.withdraw()
                MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application?',
                                                   icon='warning')
                if MsgBox == 'yes':
                    crashed = True
                break
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (turn==1):
            decisionmaker()
            turn=0

        else:
            for n in range(0,9):
                if rect[n].collidepoint(mouse) and click[0]:
                    button_func(n)
                    turn=1
                    break

        declare=gameWon(grid)
        if declare=='X' or declare=='O':
            print('the winner is',declare)
            gameDisplay.fill(white)
            lastpage(declare)
            break
        if declare=='tie':
            print('This is a Tie')
            gameDisplay.fill(white)
            lastpage('This is a Tie')
            break



        pygame.display.update()
        clock.tick(60)

nextmove=0

def get_input():
     global user_input,nextmove
     application_window = tk.Tk()
     application_window.geometry('200x140+600+250')
     application_window.title('Tic-Tac-Toe')
     input1 = Entry(application_window, bg='white', font=('sanserif', 10), width=25)
     input1.place(x=3, y=60)
     def fetch():
         global user_input,nextmove
         user_input = input1.get()
         if len(input1.get()) == 0:
             messagebox.showinfo("Input Error", "Please Enter X or O")
             nextmove=0

         else:
             application_window.destroy()
             nextmove=1

     label1=Label(application_window,text='Enter X or O',font=('sanserif', 13,'bold'),width=20)
     label1.place(x=0,y=20)
     button1=Button(application_window,bg='blue',font=('sanserif',10),fg='white',width=10,height=2,text='GO',command=fetch)
     button1.place(x=50, y=85)

     def on_closing():
         if messagebox.askokcancel("Quit", "Do you want to quit?"):
             application_window.destroy()

     application_window.protocol("WM_DELETE_WINDOW", on_closing)
     application_window.mainloop()

get_input()
if nextmove==1:
    gameDisplay.fill(white)
    mainloop()
else:
    pygame.quit()

pygame.quit() # 60fps