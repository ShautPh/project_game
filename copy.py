# Welcome to my game
# Group 24 - Mengyi & Sauth
import tkinter as tk
import random
<<<<<<< HEAD
import time
from tkinter import font
=======
>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee
from tkinter.constants import ANCHOR, COMMAND, NW, SE, TRUE, W
from tkinter.font import BOLD 
import winsound
import os



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
game_over =  tk.PhotoImage(file="./img/game-over.png")
<<<<<<< HEAD
pause_button = tk.PhotoImage(file="./img/pause-icon.png")
=======
game_win =  tk.PhotoImage(file="./img/win-game.png")
>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee
# # PLAYER IMAGE........................
player = tk.PhotoImage(file="./img/player.png")  #SIZE OF PLAYER (174x122)

# WINDOW SHOW WHEN PLAYER.................................
player_win = tk.PhotoImage(file="./img/win-game.png")
# PLAYER BULLET..........................
bullet_player = tk.PhotoImage(file="./img/bullet_player.png") #SIZE OF PLAYER BULLET ()
# PLAYER BULLET.......................
bullet_ennemy = tk.PhotoImage(file="./img/bullet_ennemy.png") #SIZE OF PLAYER BULLET (45x45)
# FIRE
fire_ennemy = tk.PhotoImage(file="./img/fire.png")
fire_player = tk.PhotoImage(file="./img/fire_player.png")
# ENNEMY IMAGES.....................
black_ennemy_image = tk.PhotoImage(file="./img/black-animy.png") #SIZE OF ENNEMY (95x95)
blue_ennemy_image = tk.PhotoImage(file="./img/blue-animy.png")
red_ennemy_image = tk.PhotoImage(file="./img/red-animy.png")
main_ennemy_image = tk.PhotoImage(file="./img/main-animy.png")

display_game = False
def display_start_game():
<<<<<<< HEAD
    global display_game,SCORE
=======
    global display_game
>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee
    if not display_game: 
        canvas.create_image(0,0,anchor=NW, image = bg,tags="start")
        canvas.create_rectangle(378,290,534,350,fill="red",outline="",tags="start")
        canvas.create_text(454,320,text="START",font=("Purisa", 30, BOLD), fill="white",tags=("startTheGame","start"))
        canvas.create_rectangle(660,290,816,350,fill="red",outline="",tags="start")
        canvas.create_text(744,320,text="EXIT",font=("Purisa", 30, BOLD), fill="white",tags=("exitTheGame","start"))
<<<<<<< HEAD
    # elif display_game and SCORE == 2: 
    #     canvas.create_image(1000,650,image=player_win ,anchor=SE)
    #     # window.destroy()
    # winsound.PlaySound("sound/explosion.wav",winsound.SND_FILENAME | winsound.SND_ALIAS)
=======
>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee
display_start_game()

#EXIT THE WINDOW TO STOP THE PROGRAME-----------------------------
def close_the_window(event):
    window.destroy()
#START GAME============
def start_process(event):
    global display_game
    canvas.delete("start")
    display_game = True
    if display_game : 
        loading_the_process()

#LOADING TIME BEFORE ALLOW PLAYER TO PLAY GAME===============================
def loading_the_process():
    canvas.create_image(0,0,image= loading_background, anchor = NW)
    canvas.create_text(600,300,text="Loading...", font= ("Purisa", 40,BOLD), fill="red")
    canvas.create_rectangle(450, 350,750,380, fill="#cccccc", outline= "")
    canvas.after(10,in_processing)


#GAME IN PROCESSING-------------------------------------------
def in_processing():
<<<<<<< HEAD
    global player_pos,bullet_of_player,player_socre,battle_image, minusPlayerLives, SCORE
    minusPlayerLives = 0
    SCORE = 0 
    battle_image = canvas.create_image(1200, 650, anchor=SE, image=bg_game)
=======
    global player_pos,bullet_of_player,player_socre,battle_image, minusPlayerLives, listOfEnemies
    minusPlayerLives = 0
    listOfEnemies = []
    battle_image = canvas.create_image(1200, 650, anchor=SE, image=bg_game)
    positionXOfPlayer = random.randrange(100,400)
    positionYOfPlayer = random.randrange(100,400)
>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee
    # CALL THE FUNCTION TO PROGRESS=========================================
    x = 86
    for i in range(5):
        live = canvas.create_rectangle(x,22,x+40,50,fill="red",outline="",tags="blood")
        x += 46
        listOfPlayerLives.append(live)
    player_socre = canvas.create_text(160,100,text="SCORE: 0",font=("Purisa", 16, BOLD), fill="white",tags=("startTheGame","start"))
    player_pos = canvas.create_image(positionXOfPlayer, positionYOfPlayer, image=player)  
    # if minusPlayerLives < -4:
    #     displayLost()
    canvas.after(500,create_enemy)
    canvas.after(500,move_enemies)
    canvas.after(500, create_player_bullet)
    canvas.after(500, move_player_bullet)
    canvas.after(500, move_ennemy_bullet)

def displayLost():
    canvas.create_image(1200, 650, anchor=SE, image=game_over)
    canvas.create_text(452,467,text="AGAIN",font=("Purisa", 30, BOLD), fill="white",tags=("startTheGame","start"))
    canvas.create_text(744,467,text="EXIT",font=("Purisa", 30, BOLD), fill="white",tags=("exitTheGame","start"))
<<<<<<< HEAD
def restart():
    global newEnnemyStartX, newEnnemyStartY, playerStartX, playerStartY, BulletPlayerStartX, BulletPlayerStartY, posOfEachEnnemy, 
=======

# def displayWin():
#     canvas.create_image(1200, 650, anchor=SE, image=game_win)
#     canvas.create_text(452,467,text="AGAIN",font=("Purisa", 30, BOLD), fill="white",tags=("startTheGame","start"))
#     canvas.create_text(744,467,text="EXIT",font=("Purisa", 30, BOLD), fill="white",tags=("exitTheGame","start"))

>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee
# # ----------------------------------------------
# # CONSTANTS
# # ----------------------------------------------
MOVE_PLAYER_INCREMENT = 20
ENNEMY_IMAGES = [black_ennemy_image,blue_ennemy_image,red_ennemy_image]
SCORE = 0 
BULLET_SIZE = 59
ENNEMY_SIZE = 95
<<<<<<< HEAD
=======
PLAYER_WIDTH = PLAYER_HEIGHT = 45
>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee
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
game_lost = False
listOfEnemies = []
listOfPlayerBullet = []
listOfEnnemyBullet = []
listOfPlayerLives = []
minusPlayerLives = 0

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
#==============================================================================
def goUp():
    global shooted
    if getPlayerPosition()[1] > 50 :
        canvas.move(player_pos, 0, -MOVE_PLAYER_INCREMENT)
#MOVE PLAYER DOWN ======================================================
def goDown():
    global shooted
    if getPlayerPosition()[1] < 600:
        canvas.move(player_pos,0,MOVE_PLAYER_INCREMENT)
#MOVE PLAYER TO LEFT======================================================== 
def goLeft():
    global shooted
    if getPlayerPosition()[0] > 20:
        canvas.move(player_pos,-MOVE_PLAYER_INCREMENT,0)    
#MOVE PLAYER TO RIGHT======================================================
def goRight():
    global shooted
    if getPlayerPosition()[0] < 1000:
        canvas.move(player_pos,MOVE_PLAYER_INCREMENT,0)

# CREATE THE ENNEMIES AND THEIR BULLET TO DISPLAY ON SCREEN ===================
def create_enemy():
<<<<<<< HEAD
    global newEnnemyStartY,minusPlayerLives
    numberEnnemyOnce = random.randrange(6,12)
    if len(listOfEnemies) < numberEnnemyOnce and minusPlayerLives > -5:
=======
    global newEnnemyStartY
    numberEnnemyOnce = random.randrange(6,12)
    if len(listOfEnemies) < numberEnnemyOnce and minusPlayerLives < 5:
>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee
        newEnnemyStartY =random.randrange(20,500)
        ennemyImage = random.choice(ENNEMY_IMAGES)
        newEnemy = canvas.create_image(newEnnemyStartX,newEnnemyStartY,image=ennemyImage)
        listOfEnemies.append(newEnemy)
        bullet_of_ennemy = canvas.create_image(newEnnemyStartX, newEnnemyStartY, image=bullet_ennemy)
        listOfEnnemyBullet.append(bullet_of_ennemy)
    newEnnemyStartY = 30
    canvas.after(1000, create_enemy)

# MOVE POSITION OF THE ENNEMIES TO ANYWHERE===========================
def move_enemies():
    ennemiesToBeDeleted = []
<<<<<<< HEAD
    for enemy in listOfEnemies:
        canvas.move(enemy, -10, 2)
        posOfEachEnnemy = canvas.coords(enemy)
        if posOfEachEnnemy[0] < 50 or posOfEachEnnemy[1] > 650:
            ennemiesToBeDeleted.append(enemy)
    for ennemy in ennemiesToBeDeleted:
        listOfEnemies.remove(ennemy)
        canvas.delete(ennemy)
    ennemyMeetPlayer(listOfEnemies)
    canvas.after(100,move_enemies)

# CREATE THE BULLET OF THE PLAYER TO DISPLAY ON SCREEN ===================
def create_player_bullet():
    if minusPlayerLives > -5:
=======
    if minusPlayerLives < 5:
        for enemy in listOfEnemies:
            canvas.move(enemy, -10, 2)
            posOfEachEnnemy = canvas.coords(enemy)
            if posOfEachEnnemy[0] < 50 or posOfEachEnnemy[1] > 650:
                ennemiesToBeDeleted.append(enemy)
        for ennemy in ennemiesToBeDeleted:
            listOfEnemies.remove(ennemy)
            canvas.delete(ennemy)
        ennemyMeetPlayer(listOfEnemies)
        canvas.after(100,move_enemies)

# CREATE THE BULLET OF THE PLAYER TO DISPLAY ON SCREEN ===================
def create_player_bullet():
    if minusPlayerLives < 5:
>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee
        bullet_of_player = canvas.create_image(getPlayerPosition()[0] + 80, getPlayerPosition()[1], image=bullet_player, tags="player_bullet")
        listOfPlayerBullet.append(bullet_of_player)
        canvas.after(500, create_player_bullet)

# MOVE BULLET OF ENNEMIES TO THE PLAYER   ==============================
def move_ennemy_bullet():
    bulletEnnemyToRemove = []
<<<<<<< HEAD
    for bullet_ennemy in listOfEnnemyBullet:
        canvas.move(bullet_ennemy, -30, 0)
        pos_bullet = canvas.coords(bullet_ennemy)
        if pos_bullet[0] < 100:
            bulletEnnemyToRemove.append(bullet_ennemy)
    
    for bullet_ennemy in bulletEnnemyToRemove:
        listOfEnnemyBullet.remove(bullet_ennemy)
        canvas.delete(bullet_ennemy)
    ennemyBulletMeetPlayer(listOfEnnemyBullet)
    canvas.after(100,move_ennemy_bullet)
=======
    if minusPlayerLives < 5:
        for bullet_ennemy in listOfEnnemyBullet:
            canvas.move(bullet_ennemy, -30, 0)
            pos_bullet = canvas.coords(bullet_ennemy)
            if pos_bullet[0] < 100:
                bulletEnnemyToRemove.append(bullet_ennemy)
        for bullet_ennemy in bulletEnnemyToRemove:
            listOfEnnemyBullet.remove(bullet_ennemy)
            canvas.delete(bullet_ennemy)
        ennemyBulletMeetPlayer(listOfEnnemyBullet)
        canvas.after(100,move_ennemy_bullet)
>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee

# MOVE BULLET OF PLAYER TO THE ENNEMIES ==============================
def move_player_bullet():
    bulletToRemove = []
<<<<<<< HEAD
    for bullet in listOfPlayerBullet:
        canvas.move(bullet, 30, 0)
        winsound.PlaySound("sound/shoot.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
        pos_bullet = canvas.coords(bullet)
        if pos_bullet[0] > 1100:
            bulletToRemove.append(bullet)
    for bullet in bulletToRemove:
        listOfPlayerBullet.remove(bullet)
        canvas.delete(bullet)
    bulletMeetEnnemy()
    canvas.after(100,move_player_bullet)
=======
    if minusPlayerLives < 5:
        for bullet in listOfPlayerBullet:
            canvas.move(bullet, 20, 0)
            # winsound.PlaySound("sound/shoot.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
            pos_bullet = canvas.coords(bullet)
            if pos_bullet[0] > 1100:
                bulletToRemove.append(bullet)
        for bullet in bulletToRemove:
            listOfPlayerBullet.remove(bullet)
            canvas.delete(bullet)
        bulletMeetEnnemy()
        canvas.after(100,move_player_bullet)
>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee

# DISPLAY FIRE WHEN BULLET OF PLAYER TOUCH ENNEMY ================================
def displayFire():
    positionOfEn = canvas.coords(enemy)
    winsound.PlaySound("sound/explosion.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.create_image(positionOfEn[0],positionOfEn[1],image=fire_ennemy,tags="deleteFire")
    canvas.after(300,disappearFire)

# DISPLAY FIRE WHEN PLAYER TOUCH ENNEMY ================================
def displayFirePlayer():
    # winsound.PlaySound("sound/explosion.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    canvas.create_image(getPlayerPosition()[0]+80,getPlayerPosition()[1],image=fire_player,tags="deleteFire")
    canvas.after(300,disappearFire)
def disappearFire():
    canvas.delete("deleteFire")
# TO CHECK IF PLAYER BULLET MEET ENNEMY========================================
def playerBulletMeetEnnemy(listOfPlayerBullets, listOfEnemies):
    global enemy
    toBeDeleted = []
    for playerBullet in listOfPlayerBullets:
        positionOfBulletPlayer = canvas.coords(playerBullet)
        for enemy in listOfEnemies:
            positionOfEn = canvas.coords(enemy)
<<<<<<< HEAD
            if (positionOfBulletPlayer[1]+59 >= positionOfEn[1]) and (positionOfBulletPlayer[1]+59 <= positionOfEn[1]+95) and (positionOfBulletPlayer[0]+59 >= positionOfEn[0]) and (positionOfBulletPlayer[0]+59 <= positionOfEn[0]+95):
=======
            if (positionOfBulletPlayer[1]+BULLET_SIZE >= positionOfEn[1]) and (positionOfBulletPlayer[1]+BULLET_SIZE <= positionOfEn[1]+ENNEMY_SIZE ) and (positionOfBulletPlayer[0]+BULLET_SIZE >= positionOfEn[0]) and (positionOfBulletPlayer[0]+BULLET_SIZE <= positionOfEn[0]+ENNEMY_SIZE):
>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee
                toBeDeleted.append(playerBullet)
                toBeDeleted.append(enemy)
                displayFire()
    return toBeDeleted

# TO CHECK IF ENNEMY BULLET MEET PLAYER========================================
def ennemyBulletMeetPlayer(listOfEnnemyBullet):
<<<<<<< HEAD
    global ennemyBullet
=======
>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee
    toBeDeleted = []
    for ennemyBullet in listOfEnnemyBullet:
        positionOfBulletEnnemy = canvas.coords(ennemyBullet)
        if (getPlayerPosition()[1]+45 >=positionOfBulletEnnemy[1]) and (getPlayerPosition()[1]+45 <= positionOfBulletEnnemy[1]+85) and (getPlayerPosition()[0]+45 >= positionOfBulletEnnemy[0]) and (getPlayerPosition()[0]+45 <= positionOfBulletEnnemy[0]+85):
            toBeDeleted.append(ennemyBullet)
            bulletMeetPlayer()
<<<<<<< HEAD
            deleteEnnemyBullet()
            
                # winsound.PlaySound("sound/explosion.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
=======
            displayFirePlayer()
            deleteEnnemyBullet(ennemyBullet)
>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee
    return toBeDeleted

# CHECK WHEN THE PLAYER MEET WITH ENNEMY ==========================================
def ennemyMeetPlayer(listOfEnemies):
    global ennemy
    toBeDeleted = []
    for ennemy in listOfEnemies:
        positionOfEnnemy = canvas.coords(ennemy)
        if (getPlayerPosition()[1]+45 >=positionOfEnnemy[1]) and (getPlayerPosition()[1]+45 <= positionOfEnnemy[1]+85) and (getPlayerPosition()[0]+45 >= positionOfEnnemy[0]) and (getPlayerPosition()[0]+45 <= positionOfEnnemy[0]+85):
            toBeDeleted.append(ennemy)
            displayFirePlayer()
            bulletMeetPlayer()
<<<<<<< HEAD
            deleteEnnemy()
            
                # winsound.PlaySound("sound/explosion.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    return toBeDeleted

=======
            deleteEnnemy(ennemy)
    return toBeDeleted

# DELETE ENNEMY FROM THE LIST OF THE ENNEMY ===================================
>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee
def bulletMeetEnnemy():
    meetEnemy = playerBulletMeetEnnemy(listOfPlayerBullet, listOfEnemies)
    if len(meetEnemy) > 0:
        listOfPlayerBullet.remove(meetEnemy[0])
        listOfEnemies.remove(meetEnemy[1])
        canvas.delete(meetEnemy[0])
        canvas.delete(meetEnemy[1])
        scoreIncrement()

<<<<<<< HEAD
def bulletMeetPlayer():
    global minusPlayerLives, game_lost 
    if minusPlayerLives != -5:
        minusPlayerLives -= 1
        canvas.itemconfig(listOfPlayerLives[minusPlayerLives], fill="")
    else:
        displayLost()



def deleteEnnemyBullet():
    listOfEnnemyBullet.remove(ennemyBullet)
    canvas.delete(ennemyBullet)

def deleteEnnemy():
    listOfEnemies.remove(ennemy)
    canvas.delete(ennemy)
=======
# TO MINUS LIVE OF THE PLAYER WHENEVER TOUCHED ENNEMY OR BULLET OF THE ENNEMY====
def bulletMeetPlayer():
    global minusPlayerLives, SCORE
    minusPlayerLives += 1
    canvas.itemconfig(listOfPlayerLives[-minusPlayerLives], fill="")
    if minusPlayerLives == 5:
        displayLost()
    # elif minusPlayerLives > -5 and SCORE == 10 : 
    #     displayWin()


# TO DELETE=============================================
def deleteEnnemyBullet(ennemyBullet):
    listOfEnnemyBullet.remove(ennemyBullet)
    canvas.delete(ennemyBullet)
def deleteEnnemy(ennemy):
    listOfEnemies.remove(ennemy)
    canvas.delete(ennemy)
# .............................................

# INCREMENT SOCRE FOR PLAYER WHEN ITS BULLET TOUCH ENNEMY=========================
>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee
def scoreIncrement():
    global SCORE
    SCORE += 1
    if SCORE <= 1: 
        canvas.itemconfig(player_socre,text= "SCORE: "+ str(SCORE))
    else:
<<<<<<< HEAD
        canvas.itemconfig(player_socre,text= "SCORES: "+ str(SCORE))
=======
        title = "SCORES: "
    canvas.itemconfig(player_socre,text= title + str(SCORE))
>>>>>>> fa93052a656af8eea8f12a1ac8d678a1f1b15aee
#     if SCORE == 20:
#         appear_main_ennemy()

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


# KEYS THAT PLAYER HAS TO PRESS TO PLAY THE GAME=================================
window.bind("<w>", onWPressed)
window.bind("<s>",onSPressed)
window.bind("<d>",onDPressed)
window.bind("<a>",onAPressed)
#LEFT CLICK TO START OR EXIT THE GAME==================================
canvas.tag_bind("startTheGame","<Button-1>",start_process)
canvas.tag_bind("exitTheGame","<Button-1>",close_the_window)
#DISPLAY WINDOW====================================================
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
window.mainloop()