class Block:
    x = 0
    y = 0
    n = 0
    def __init__(self, x, y,n):
        self.x = x
        self.y = y
        self.type = n
        self.color = n
        self.rotation = 0
    def image(self):
        return shapes[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(shapes[self.type])