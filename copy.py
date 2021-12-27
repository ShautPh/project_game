# Welcome to my game
# Group 24 - Mengyi & Sauth
import tkinter as tk
import random
import time
from tkinter.constants import ANCHOR, SE 


# ----------------------------------------------
# TKINTER GRAPHICS
# ----------------------------------------------
window = tk.Tk()
#Adjust size of the window
window.geometry("1200x650")

#The title of the window
frame = tk.Frame()
window.title("Space Invader by (Sauth and MengYi)")
canvas = tk.Canvas(frame)

# BACKGROUND IN THE PROCESS=====================
bg = tk.PhotoImage(file="./img/start-game.png")
bg_game = tk.PhotoImage(file="./img/battle-game.png")

# PLAYER IMAGE........................
player = tk.PhotoImage(file="./img/player.png")
# PLAYER BULLET
bullet_player = tk.PhotoImage(file="./img/bullet_player.png")

# Background image
# label1 = tk.Label(window, image=bg)
# label1.place(x=0, y=0)

battle_image = canvas.create_image(1200, 650, anchor=SE, image=bg_game) 

# Enemies image.....................

black_ennemy_image = tk.PhotoImage(file="./img/black-animy.png")
blue_ennemy_image = tk.PhotoImage(file="./img/blue-animy.png")
red_ennemy_image = tk.PhotoImage(file="./img/red-animy.png")


# ----------------------------------------------
# CONSTANTS
# ----------------------------------------------
MOVE_PLAYER_INCREMENT = 16
ENNEMY_IMAGES = [black_ennemy_image,blue_ennemy_image,red_ennemy_image]


# ----------------------------------------------
# VARIABLES
# ----------------------------------------------
newEnnemyStartX = 1200
newEnnemyStartY = 30
playerStartX = 300
playerStartY = 400
BulletPlayerStartX = 380
BulletPlayerStartY = 400
posOfEachEnnemy = []
shooted = False
listOfEnemies = []
player_pos = canvas.create_image(playerStartX, playerStartY, image=player)
bullet_of_player = canvas.create_image(BulletPlayerStartX, BulletPlayerStartY, image=bullet_player, tags="player_bullet")


# THE POSITION OF THE PLAYER===================
def getPlayerPosition():
    return canvas.coords(player_pos)

# MOVE POSITION PLAYER BY USING KEY PRESS=====================================
def onWPressed(event) :
    goUp()
def onSPressed(event) :
    goDown()
def onAPressed(event) :
    goLeft()
def onDPressed(event) :
    goRight()

# MOVE POSITION BULLET BY USING KEY PRESS=====================================
def onSpacePressed(event):
    global shooted
    shooted = True
    move_bullet()


#MOVE PLAYER UP ==========================================================
def goUp():
    global shooted
    if getPlayerPosition()[1] > 50 :
        canvas.move(player_pos, 0, -MOVE_PLAYER_INCREMENT)
        if not shooted:
            canvas.move(bullet_of_player, 0, -MOVE_PLAYER_INCREMENT)
#MOVE PLAYER DOWN ======================================================
def goDown():
    global shooted
    if canvas.coords(player_pos)[1] < 600:
        canvas.move(player_pos,0,MOVE_PLAYER_INCREMENT)
        if not shooted:
            canvas.move(bullet_of_player, 0, MOVE_PLAYER_INCREMENT)

#MOVE PLAYER TO LEFT======================================================== 
def goLeft():
    global shooted
    if canvas.coords(player_pos)[0] > 20:
        canvas.move(player_pos,-MOVE_PLAYER_INCREMENT,0)
        if not shooted:
            canvas.move(bullet_of_player, -MOVE_PLAYER_INCREMENT, 0)

#MOVE PLAYER TO RIGHT======================================================
def goRight():
    global shooted
    if canvas.coords(player_pos)[0] < 1000:
        canvas.move(player_pos,MOVE_PLAYER_INCREMENT,0)
        if not shooted:
            canvas.move(bullet_of_player, MOVE_PLAYER_INCREMENT, 0)





# CREATE THE ENNEMIES TO DISPLAY ON SCREEN ===================
def create_enemy():
    global newEnnemyStartY
    if len(listOfEnemies) < 6  :
        newEnnemyStartY =random.randrange(40,500)
        ennemyImage = random.choice(ENNEMY_IMAGES)
        newEnemy = canvas.create_image(newEnnemyStartX,newEnnemyStartY,image=ennemyImage, tags="all_enemy")
        listOfEnemies.append(newEnemy)
    newEnnemyStartY = 30
    canvas.after(1000, create_enemy)

# MOVE POSITION OF THE ENNEMIES TO ANYWHERE===========================
def move_enemies():
    global listOfEnemies, posOfEachEnnemy
    ennemiesToBeDeleted = []
    for enemy in listOfEnemies:
        canvas.move(enemy, -10, 0)
        posOfEachEnnemy = canvas.coords(enemy)
        if posOfEachEnnemy[0] < 50:
            ennemiesToBeDeleted.append(enemy)
    for ennemy in ennemiesToBeDeleted:
        listOfEnemies.remove(ennemy)
        canvas.delete(ennemy)
    canvas.after(100,move_enemies)

# CREATE THE BULLET TO DISPLAY ON SCREEN ===================
def create_new_bullet():
    global bullet_of_player, shooted
    shooted = False
    pos = canvas.coords(player_pos)
    bullet_of_player = canvas.create_image(pos[0] + 80, pos[1], image=bullet_player, tags="player_bullet")


# MOVE BULLET OF PLAYER TO THE ENNEMIES ==============================
def move_bullet():
    canvas.move(bullet_of_player, 20, 0)
    pos = canvas.coords(bullet_of_player)
    if pos[0] < 900:
        canvas.after(20, move_bullet)
    else:
        canvas.delete("player_bullet")
        canvas.after(100, create_new_bullet)


#CALL THE FUNCTION TO PROGRESS=========================================
create_enemy()
move_enemies()


#KEYS THAT PLAYER HAS TO PRESS TO PLAY THE GAME=================================
window.bind("<w>", onWPressed)
window.bind("<s>",onSPressed)
window.bind("<d>",onDPressed)
window.bind("<a>",onAPressed)
window.bind("<space>",onSpacePressed)

#DISPLAY WINDOW====================================================
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
window.mainloop()




# def increment_player_score():
#     global SCORE,player_score
#     SCORE += 1
#     if SCORE <= 1: 
#         canvas.itemconfig(player_socre,text= "SCORE: "+ str(SCORE))
#     else:
#         canvas.itemconfig(player_socre,text= "SCORES: "+ str(SCORE))
#


# def appear_main_ennemy():
#     global main_ennemy
#     main_ennemy = canvas.create_image(1200, 650, anchor=SE, image= main_ennemy_image)
#     move_main_ennemy()

# def move_main_ennemy():
#     canvas.move(main_ennemy,-50,0)
#     canvas.after(3000,move_main_ennemy_go_right)
# def move_main_ennemy_go_right():
#     canvas.move(main_ennemy,50,0)
#     canvas.after(3000,move_main_ennemy_go_Down)
# def move_main_ennemy_go_Down():
#     canvas.move(main_ennemy,0,40)
#     canvas.after(3000,move_main_ennemy_go_up)
# def move_main_ennemy_go_up():
#     canvas.move(main_ennemy,0,-40)
#     canvas.after(3000,move_main_ennemy)
#     canvas.after(100,move_main_ennemy)