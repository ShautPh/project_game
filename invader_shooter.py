# Welcome to my game
# Group 24 - Mengyi & Sauth
import tkinter as tk
import random
import time
from tkinter import font
from tkinter.constants import ANCHOR, COMMAND, NW, SE
from tkinter.font import BOLD 
import winsound


# ----------------------------------------------
# TKINTER GRAPHICS
# ----------------------------------------------
window = tk.Tk()
#Adjust size of the window
window.geometry("1200x650")
window.resizable(False,False)

#The title of the window
frame = tk.Frame()
window.title("Space Invader by (Sauth and MengYi)")
canvas = tk.Canvas(frame)

# BACKGROUND IN THE PROCESS=====================
bg = tk.PhotoImage(file="./img/start-game.png")
bg_game = tk.PhotoImage(file="./img/battle-game.png")
loading_background =  tk.PhotoImage(file="./img/loading_bg.png")
# # PLAYER IMAGE........................
player = tk.PhotoImage(file="./img/player.png")
# PLAYER BULLET
bullet_player = tk.PhotoImage(file="./img/bullet_player.png")

# ENNEMY IMAGES.....................
black_ennemy_image = tk.PhotoImage(file="./img/black-animy.png")
blue_ennemy_image = tk.PhotoImage(file="./img/blue-animy.png")
red_ennemy_image = tk.PhotoImage(file="./img/red-animy.png")

display_game = False
def display_start_game():
    global display_game
    if not display_game: 
        canvas.create_image(0,0,anchor=NW, image = bg,tags="start")
        canvas.create_rectangle(378,290,534,350,fill="red",outline="",tags="start")
        canvas.create_text(454,320,text="START",font=("Purisa", 30, BOLD), fill="white",tags=("startTheGame","start"))
        canvas.create_rectangle(660,290,816,350,fill="red",outline="",tags="start")
        canvas.create_text(744,320,text="EXIT",font=("Purisa", 30, BOLD), fill="white",tags=("exitTheGame","start"))
    # winsound.PlaySound("sound/explosion.wav",winsound.SND_FILENAME | winsound.SND_ALIAS)
display_start_game()

#EXIT THE WINDOW TO STOP THE PROGRAME-----------------------------
def close_the_window(event):
    window.destroy()
#START GAME============
def start_process(event):
    global display_game
    canvas.delete("start")
    display_game = True
    if display_game: 
        canvas.after(100,loading_the_process)
#LOADING TIME BEFORE ALLOW PLAYER TO PLAY GAME===============================
def loading_the_process():
    canvas.create_image(0,0,image= loading_background, anchor = NW)
    canvas.create_text(600,300,text="Loading...", font= ("Purisa", 40,BOLD), fill="red")
    canvas.create_rectangle(450, 350,750,380, fill="#cccccc", outline= "")
    # loading_sign ()
    canvas.after(2,in_processing)
# d
# def loading_sign ():

#GAME IN PROCESSING-------------------------------------------
def in_processing():
    global player_pos,bullet_of_player
    battle_image = canvas.create_image(1200, 650, anchor=SE, image=bg_game)
    # CALL THE FUNCTION TO PROGRESS=========================================
    canvas.after(500,create_enemy)
    canvas.after(500,move_enemies)
    player_pos = canvas.create_image(300, 400, image=player)  
    bullet_of_player = canvas.create_image(BulletPlayerStartX, BulletPlayerStartY, image=bullet_player, tags="player_bullet")
  
# # ----------------------------------------------
# # CONSTANTS
# # ----------------------------------------------
MOVE_PLAYER_INCREMENT = 20
ENNEMY_IMAGES = [black_ennemy_image,blue_ennemy_image,red_ennemy_image]
# # ----------------------------------------------
# # VARIABLES
# # ----------------------------------------------
newEnnemyStartX = 1200
newEnnemyStartY = 30
playerStartX = 300
playerStartY = 400
BulletPlayerStartX = 380
BulletPlayerStartY = 400
posOfEachEnnemy = []
shooted = False
listOfEnemies = []

# # THE POSITION OF THE PLAYER================================================
def getPlayerPosition():
    return canvas.coords(player_pos)
# MOVE POSITION PLAYER BY USING KEY PRESS=====================================
def onWPressed(event):
    goUp()
def onSPressed(event):
    goDown()
def onAPressed(event):
    goLeft()
def onDPressed(event):
    goRight()

# MOVE POSITION BULLET BY USING KEY PRESS=====================================
def onSpacePressed(event):
    global shooted
    shooted = True
    move_bullet()
#==============================================================================
def goUp():
    global shooted
    if getPlayerPosition()[1] > 50 :
        canvas.move(player_pos, 0, -MOVE_PLAYER_INCREMENT)
        if not shooted:
            canvas.move(bullet_of_player, 0, -MOVE_PLAYER_INCREMENT)
#MOVE PLAYER DOWN ======================================================
def goDown():
    global shooted
    if getPlayerPosition()[1] < 600:
        canvas.move(player_pos,0,MOVE_PLAYER_INCREMENT)
        if not shooted:
            canvas.move(bullet_of_player, 0, MOVE_PLAYER_INCREMENT)
#MOVE PLAYER TO LEFT======================================================== 
def goLeft():
    global shooted
    if getPlayerPosition()[0] > 20:
        canvas.move(player_pos,-MOVE_PLAYER_INCREMENT,0)
        if not shooted:
            canvas.move(bullet_of_player, -MOVE_PLAYER_INCREMENT, 0)
#MOVE PLAYER TO RIGHT======================================================
def goRight():
    global shooted
    if getPlayerPosition()[0] < 1000:
        canvas.move(player_pos,MOVE_PLAYER_INCREMENT,0)
        if not shooted:
            canvas.move(bullet_of_player, MOVE_PLAYER_INCREMENT, 0)
# CREATE THE ENNEMIES TO DISPLAY ON SCREEN ===================
def create_enemy():
    global newEnnemyStartY
    if len(listOfEnemies) < 6 :
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
    global bullet_of_player, shooted, listOfBullet
    shooted = False
    pos = canvas.coords(player_pos)
    bullet_of_player = canvas.create_image(pos[0] + 80, pos[1], image=bullet_player, tags="player_bullet")
    # canvas.after(1000,create_new_bullet)

# MOVE BULLET OF PLAYER TO THE ENNEMIES ==============================
def move_bullet():
    print(listOfEnemies)
    canvas.move(bullet_of_player, 20, 0)
    pos = canvas.coords(bullet_of_player)
    if pos[0] > 1200:
        canvas.delete("player_bullet")
        canvas.after(100, create_new_bullet)
    else:
        canvas.after(20, move_bullet)
    
# KEYS THAT PLAYER HAS TO PRESS TO PLAY THE GAME=================================
window.bind("<w>", onWPressed)
window.bind("<s>",onSPressed)
window.bind("<d>",onDPressed)
window.bind("<a>",onAPressed)
window.bind("<space>",onSpacePressed)
#LEFT CLICK TO START OR EXIT THE GAME==================================
canvas.tag_bind("startTheGame","<Button-1>",start_process)
canvas.tag_bind("exitTheGame","<Button-1>",close_the_window)
#DISPLAY WINDOW====================================================
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
window.mainloop()
