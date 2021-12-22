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
canvas = tk.Canvas(frame)


# Add Image
# Player image........................
player = tk.PhotoImage(file="./img/player.png")
player_pos = canvas.create_image(300, 400, image=player)

# Enemies image.....................
enemy_1 = tk.PhotoImage(file="./img/black-animy.png")
enemy_2 = tk.PhotoImage(file="./img/blue-animy.png")
enemy_3 = tk.PhotoImage(file="./img/red-animy.png")
enemies = [enemy_1,enemy_2,enemy_3]
black_enemy = canvas.create_image(1100, 300, image=random.choice(enemies)) 

# Variable
amountOfEnemies = 2



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

def enemy1_coming():
    global black_enemy, amountOfEnemies
    position = random.randrange(25, 600)
    pos = canvas.coords(black_enemy)
    positionOfenemy = random.randrange(500, 800)
    if amountOfEnemies <= 10:
        if pos[0] > positionOfenemy and pos[1] < 600:
            canvas.move(black_enemy, -10.15,0)
        else:
            black_enemy = canvas.create_image(1100, position, image=random.choice(enemies)) 
            amountOfEnemies += 1
    canvas.after(100, enemy1_coming)

    # canvas.after(100,enemy1_coming)

canvas.after(100,enemy1_coming)
# canvas.after(900,enemy2_coming)
# canvas.after(800,enemy3_coming)
#Button to controll the player
window.bind("<w>",goUp)
window.bind("<s>",goDown)
window.bind("<d>",goRight)
window.bind("<a>",goLeft)
#display window
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
window.mainloop()
