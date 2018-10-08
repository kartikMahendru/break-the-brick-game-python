class Bricks:

    def __init__(self, canvas, color):
        self.recs = []
        self.canvas = canvas
        for i in range(1, 5):
            id = self.canvas.create_rectangle(0, 0, 50, 30, fill=color)
            self.canvas.move(id, 100*i+5, 200)
            self.recs.append(id)

    def draw(self):
        pass
