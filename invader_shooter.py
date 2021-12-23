# Welcome to my game
# Group 24 - Mengyi & Sauth
import tkinter as tk
import random
import time
from tkinter.constants import ANCHOR, SE 

window = tk.Tk()
#Adjust size of the window
window.geometry("1200x650")

#The title of the window
frame = tk.Frame()
window.title("Space Invader by (Sauth and MengYi)")
canvas = tk.Canvas(frame)


# Add Image
# Background 
bg = tk.PhotoImage(file="./img/start-game.png")
bg_game = tk.PhotoImage(file="./img/battle-game.png")

# Player image........................
player = tk.PhotoImage(file="./img/player.png")


# # Background image
# label1 = tk.Label(window, image=bg)
# label1.place(x=0, y=0)



# Enemies image.....................

enemy_1 = tk.PhotoImage(file="./img/black-animy.png")
enemy_2 = tk.PhotoImage(file="./img/blue-animy.png")
enemy_3 = tk.PhotoImage(file="./img/red-animy.png")
# list_of_enemies = [enemy_1,enemy_2,enemy_3]


# Variable=================================
amountOfEnemies = 0
listOfEnemies = []

battle_image = canvas.create_image(1200, 650, anchor=SE, image=bg_game) 
player_pos = canvas.create_image(300, 400, image=player)

# black_enemy = canvas.create_image(1200, 300, image=enemy_1) 
# blue_enemy = canvas.create_image(1200, 350, image=enemy_2) 
# red_enemy = canvas.create_image(1200, 400, image=enemy_3) 


#Move Up(player) ==========================================================
def goUp(event):
    while True: 
        canvas.update()
        if canvas.coords(player_pos)[1] > 50 :
            canvas.move(player_pos,0,-4)
        time.sleep(0.01)

#Move down(player) ======================================================
def goDown(event):
    while True: 
        canvas.update()
        if canvas.coords(player_pos)[1] < 600:
            canvas.move(player_pos,0,4)
        time.sleep(0.01)
#Move left(player)======================================================== 
def goLeft(event):
    if canvas.coords(player_pos)[0] > 20:
        canvas.move(player_pos,-2,0)
    while True: 
        canvas.update()
        if canvas.coords(player_pos)[0] > 20:
            canvas.move(player_pos,-2,0)
        time.sleep(0.01)
#Move right(player)======================================================
def goRight(event):
    if canvas.coords(player_pos)[0] < 500:
        canvas.move(player_pos,2,0)
    while True: 
        canvas.update()
        if canvas.coords(player_pos)[0] < 500:
            canvas.move(player_pos,2,0)
        time.sleep(0.01)

# create enemy to display on screen ===================
positionY = 30
def create_enemy():
    global amountOfEnemies,positionY
    positionY += 100
    type_of_enemy = [enemy_1,enemy_2,enemy_3]
    if amountOfEnemies < 5  :
        amountOfEnemies += 1
        enemy = canvas.create_image(1200,positionY,image=random.choice(type_of_enemy), tags="all_enemy")
        listOfEnemies.append(enemy)

def move_enemies():
    global amountOfEnemies,positionY,listOfEnemies
    remove_enemy = []
    for index in range(len(listOfEnemies)):
        enemy = listOfEnemies[index]
        position_of_enemy = canvas.coords(enemy)[0]
        canvas.move(enemy, -10, 0)
        if position_of_enemy < -20: 
            canvas.delete("all_enemy")
        # else:
        #     for i in range(len(remove_enemy)):
    canvas.after(1000,create_enemy)
    canvas.after(100,move_enemies)
    

create_enemy()
move_enemies()

#Keys that player press to play game
window.bind("<w>",goUp)
window.bind("<s>",goDown)
window.bind("<d>",goRight)
window.bind("<a>",goLeft)




#display window
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
window.mainloop()
