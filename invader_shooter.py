# Welcome to my game
# Group 24 - Mengyi & Sauth
import tkinter as tk
import random
import time
from tkinter.constants import ANCHOR 

window = tk.Tk()
#Adjust size of the window
window.geometry("1400x700")

#The title of the window
frame = tk.Frame()
window.title("Space Invader by (Sauth and MengYi)")
canvas = tk.Canvas(frame)


# Add Image
player = tk.PhotoImage(file="./img/player.png")
player_pos = canvas.create_image(300, 400, image=player)


#Move Up 
def goUp(event):

    while True: 
        canvas.update()
        canvas.move(player_pos,0,-1)
        time.sleep(0.01)
#Move down 
def goDown(event):
    while True: 
        canvas.update()
        canvas.move(player_pos,0,1)
        time.sleep(0.001)
#Move left 
def goLeft(event):
    canvas.move(player_pos, -20, 0)
#Move right
def goRight(event):
    canvas.move(player_pos, 20, 0)

#Button to controll the player
<<<<<<< HEAD
window.bind("<w>",goUp)
window.bind("<s>",goDown)
=======
# canvas.pack("<w>",goUp)
window.bind("<d>",goRight)
window.bind("<a>",goLeft)
>>>>>>> b96da25ca8f104450fa946922b8a95b8d82e28f7
#display window
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
window.mainloop()
