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
#Move down 
#Move left 
def goLeft(event):
    canvas.move(player_pos, -20, 0)
#Move right
def goRight(event):
    canvas.move(player_pos, 20, 0)

#Button to controll the player
# canvas.pack("<w>",goUp)
window.bind("<d>",goRight)
window.bind("<a>",goLeft)
#display window
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
window.mainloop()
