from tkinter import *
import random
import time

class Ball:
    speed = 2
    i=1
    j=1

    def __init__(self, canvas, paddle, bricks, color):
        self.canvas = canvas
        self.paddle = paddle
        self.bricks = bricks
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = Ball.speed
        self.y = Ball.speed
        self.hit_bottom = False
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        print(self.canvas_width)
        print(self.canvas_height)

    def hit(self, pos):
        pos_paddle = self.canvas.coords(self.paddle.id)
        if pos[2] >= pos_paddle[0] and pos[0] <= pos_paddle[2]:
            if pos[3] <= pos_paddle[1] <= pos_paddle[3]:
                return True
        return False

    def collision_with_bricks(self, pos):
        for id in self.bricks.recs:
            pos_bricks = self.canvas.coords(id)
            #case 1: hit from bottom
            if pos_bricks[0] < pos[0] < pos_bricks[2] and pos_bricks[1] < pos[1] < pos_bricks[3]:
                if pos_bricks[0] < pos[2] < pos_bricks[2]:
                    return 1, id

            #case 2 : hit from top
            if pos_bricks[0] < pos[2] < pos_bricks[2] and pos_bricks[1] < pos[3] < pos_bricks[3]:
                if pos_bricks[0] < pos[0] < pos_bricks[2]:
                    return 1, id

            #case 3: hit from left
            if pos_bricks[0] < pos[2] < pos_bricks[2] and pos_bricks[1] < pos[3] < pos_bricks[3]:
                if pos_bricks[1] < pos[1] < pos_bricks[3]:
                    return 2, id

            #case 4 : hit from right
            if pos_bricks[0] < pos[0] < pos_bricks[2] and pos_bricks[1] < pos[1] < pos_bricks[3]:
                if pos_bricks[1] < pos[3] < pos_bricks[3]:
                    return 2, id

        return 0, 0

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = Ball.speed
        if pos[1] <= 0:
            self.y = Ball.speed
        if pos[2] >= self.canvas_width:
            self.x = -Ball.speed
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True

        if self.hit(pos):
            print(Ball.i)
            Ball.i=Ball.i+1
            self.y = -Ball.speed

        if len(self.bricks.recs) > 0:
            val, brick_id = self.collision_with_bricks(pos)
            if val == 1:
                print(Ball.j)
                Ball.j=Ball.j+1
               # self.y = -self.y
                self.canvas.delete(brick_id)
                self.bricks.recs.remove(brick_id)

            elif val == 2:
                self.x = -self.x
                self.canvas.delete(brick_id)
                self.bricks.recs.remove(brick_id)



