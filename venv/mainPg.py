from tkinter import *
from tkinter import messagebox
import random
import time
from paddle import Paddle
from ball import Ball
from bricks import Bricks


def start_game():
    global tk
    tk = Tk()
    tk.title("Bounce !!")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=500, height=500, bg="Black", highlightthickness=0)
    canvas.pack()
    tk.update()

    paddle = Paddle(canvas, "Blue")
    bricks = Bricks(canvas, "Green")
    ball = Ball(canvas, paddle, bricks, "red")
    while True:
        if ball.hit_bottom == False and len(bricks.recs) > 0:
            ball.draw()
            paddle.draw()
        elif len(bricks.recs) == 0:
            flag = 1
            break
        elif ball.hit_bottom:
            flag = 2
            break
        tk.update_idletasks()
        tk.update()
        time.sleep(0.05)

    return flag


def boot():
    global tk
    final_val = start_game()
    if final_val == 1:
        resp = messagebox.askyesno("You Won !!!!", " Do you want to play again ???")
        if resp:
            print("true")
            tk.destroy()
            boot()
        else:
            print("False")
            tk.destroy()

    else:
        resp = messagebox.askyesno("You Lose !!!!", " Do you want to play again ???")
        if resp:
            print("true")
            tk.destroy()
            boot()
        else:
            print("False")
            tk.destroy()


boot()


