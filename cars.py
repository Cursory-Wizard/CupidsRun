import pyxel


class Cars:

    def __init__(self,x, y, choice):
        self.render = [x, y]
        self.animation_frame_west = [[0, 10], [0, 12], [0, 14], [0, 16], [0, 18], [0, 20]]
        self.animation_frame_east = [[4, 10], [4, 12], [4, 14]]
        self.animation = self.animation_frame_west[0 + choice]
        self.timer = 0
        self.car_choice = choice

    def update_west(self, maps):
        self.render[1]
        self.render[0] -= 1
        self.timer += 1
        if self.timer == 12:
            self.animation = self.animation_frame_west[1 + self.car_choice]
        elif self.timer == 24:
            self.animation = self.animation_frame_west[2 + self.car_choice]
        elif self.timer > 35:
            self.timer = 0
            self.animation = self.animation_frame_west[0 + self.car_choice]

    def update_east(self, maps):
        self.render[0] += 1
        self.timer += 1
        if self.timer == 12:
            self.animation = self.animation_frame_east[1]
        elif self.timer == 24:
            self.animation = self.animation_frame_east[2]
        elif self.timer > 35:
            self.timer = 0
            self.animation = self.animation_frame_east[0]
