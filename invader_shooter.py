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
# black_enemy = canvas.create_image(1100, 20, image=enemy_1) 
# blue_enemy = canvas.create_image(1100, 20, image=enemy_2) 
# red_enemy = canvas.create_image(1100, 20, image=enemy_3) 

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
    black_enemy = canvas.create_image(1100, 0, image=enemy_1) 
    while not False: 
        canvas.update()
        canvas.move(black_enemy,-1,1)
        time.sleep(0.01)
def enemy2_coming():
    blue_enemy = canvas.create_image(1100, 0, image=enemy_2) 
    while not False: 
        canvas.update()
        canvas.move(blue_enemy,-1,1)
        time.sleep(0.01)
def enemy3_coming():
    red_enemy = canvas.create_image(1100, 0, image=enemy_3) 
    while not False: 
        canvas.update()
        canvas.move(red_enemy,-1,1)
        time.sleep(0.01)
random

canvas.after(1000,enemy1_coming)
canvas.after(900,enemy2_coming)
canvas.after(800,enemy3_coming)
#Button to controll the player
window.bind("<w>",goUp)
window.bind("<s>",goDown)
window.bind("<d>",goRight)
window.bind("<a>",goLeft)
#display window
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
window.mainloop()
