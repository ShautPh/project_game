# Welcome to my game
# Group 24 - Mengyi & Sauth
import tkinter as tk
import random
import time
from tkinter.constants import ANCHOR 

window = tk.Tk()
#Adjust size of the window
window.geometry("1200x650")

#The title of the window
frame = tk.Frame()
window.title("Space Invader by (Sauth and MengYi)")
canvas = tk.Canvas()


# Add Image
# Background 
bg = tk.PhotoImage(file="./img/start-game.png")
# Player image........................
player = tk.PhotoImage(file="./img/player.png")
player_pos = canvas.create_image(300, 400, image=player)

# # Background image
# label1 = tk.Label(window, image=bg)
# label1.place(x=0, y=0)

# Enemies image.....................
enemy_1 = tk.PhotoImage(file="./img/black-animy.png")
enemy_2 = tk.PhotoImage(file="./img/blue-animy.png")
enemy_3 = tk.PhotoImage(file="./img/red-animy.png")
# list_of_enemies = [enemy_1,enemy_2,enemy_3]


# Variable
amountOfEnemies = 2

black_enemy = canvas.create_image(1200, 300, image=enemy_1) 
blue_enemy = canvas.create_image(1200, 350, image=enemy_2) 
red_enemy = canvas.create_image(1200, 400, image=enemy_3) 


#Move Up(player) 
def goUp(event):
    while True: 
        canvas.update()
        if canvas.coords(player_pos)[1] > 50 :
            canvas.move(player_pos,0,-2)
        time.sleep(0.01)
#Move down(player) 
def goDown(event):
    while True: 
        canvas.update()
        if canvas.coords(player_pos)[1] < 600:
            canvas.move(player_pos,0,2)
        time.sleep(0.01)
#Move left(player) 
def goLeft(event):
    while True: 
        canvas.update()
        if canvas.coords(player_pos)[0] > 20:
            canvas.move(player_pos,-2,0)
        time.sleep(0.01)
#Move right(player)
def goRight(event):
    while True: 
        canvas.update()
        if canvas.coords(player_pos)[0] < 500:
            canvas.move(player_pos,2,0)
        time.sleep(0.01)


def appear_enemies():
    global black_enemy,blue_enemy,red_enemy, amountOfEnemies
    pos_enemy = canvas.coords(black_enemy)
    position = random.randrange(25, 500)
    positionOfenemy = random.randrange(500, 800)
    canvas.move(black_enemy, -10.50,0)
    canvas.move(blue_enemy, -12.50,0)
    canvas.move(red_enemy, -11.50,0)
    # if amountOfEnemies <= 10:
    if pos_enemy[0] > positionOfenemy:
        canvas.move(black_enemy, 0,2)
        canvas.move(blue_enemy, 0,-2)
        canvas.move(red_enemy, 0,3)
    canvas.after(100, appear_enemies)


# canvas.after(100, appear_enemies)
canvas.after(100,appear_enemies)



#Keys that player press to play game
window.bind("<w>",goUp)
window.bind("<s>",goDown)
window.bind("<d>",goRight)
window.bind("<a>",goLeft)




#display window
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
window.mainloop()
