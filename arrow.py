import pyxel

class arrow:

    def __init__(self, player):
        self.x = player.render[0]
        self.y = player.render[1]
        self.direction = player.direction
        if self.direction == "S":
            self.sprite = [4, 2]
        if self.direction == "N":
            self.sprite = [4, 0]
        if self.direction == "E":
            self.sprite = [2, 2]
        if self.direction == "W":
            self.sprite = [2, 4]

    def update(self):
        if self.direction == "S":
            self.y += 3
        if self.direction == "N":
            self.y -= 3
        if self.direction == "E":
            self.x += 3
        if self.direction == "W":
            self.x -= 3