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
black_enemy = canvas.create_image(1100, 20, image=enemy_1) 

type_of_anemy = [enemy_1,enemy_2,enemy_3]

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
    anemy_appear = random.choice(type_of_anemy)
    position = random.randrange(25, 600)
    pos = canvas.coords(anemy_appear)
    canvas.create_image(1100, position, image=anemy_appear) 
    if pos[1] > 25 :

        canvas.move(anemy_appear, -10.15,0)
    # if pos[0] > 550 and pos[1] < 600:
    #     canvas.move(anemy_appear, -10.15,0)
    # else:
    #     canvas.create_image(1100, position, image=anemy_appear) 
    # canvas.after(150, enemy1_coming)

canvas.after(100,enemy1_coming)










#Button to controll the player
window.bind("<w>",goUp)
window.bind("<s>",goDown)
window.bind("<d>",goRight)
window.bind("<a>",goLeft)




#display window
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
window.mainloop()
