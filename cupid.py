import pyxel
import arrow

class cupid:
    def __init__(self):
        self.tile_location = [0, 0]
        self.tile = [3, 4]
        self.tileset = []
        self.true_location = [24, 32]
        self.render = [24, 32]
        self.walkCounter = 0
        self.walking = False
        self.walkAnim = False
        self.outOfBounds_X = True
        self.outOfBounds_Y = True
        self.direction = "S"
        self.sprite = [0, 0]
        self.arrows = []

    def update(self, maps):
        if pyxel.btnp(pyxel.KEY_S, 1, 1):
            self.render[1] += 1
            self.true_location[1] += 1
            got_bumped = False

            for rect in maps.no_go:
                if self.true_location[1] + 16 == rect[1]:
                    if (self.true_location[0] <= rect[2]) and (self.true_location[0] + 16 >=  rect[0]):
                        got_bumped = True
                        self.render[1] -= 1
                        self.true_location[1] -= 1
                        break

            if (self.render[1] > maps.player_inbound[2]) and not got_bumped:
                self.render[1] -= 1
                maps.shift = "south"

            self.walking = True
            self.direction = "S"
            if self.walkCounter < 5:
                self.sprite = [0, 0]
                self.walkAnim = False
            elif self.walkCounter < 10:
                self.sprite = [2, 0]
                self.walkAnim = True

        elif pyxel.btnp(pyxel.KEY_W, 1, 1):
            self.render[1] -= 1
            self.true_location[1] -= 1
            got_bumped = False


            for rect in maps.no_go:
                if self.true_location[1] == rect[3]:
                    if (self.true_location[0] <= rect[2]) and (self.true_location[0] + 16 >= rect[0]):
                        self.render[1] += 1
                        self.true_location[1] += 1
                        got_bumped = True
                        break

            if self.render[1] < maps.player_inbound[1] and not got_bumped:
                self.render[1] += 1
                maps.shift = "north"

            self.walking = True
            self.direction = "N"
            if self.walkCounter < 5:
                self.sprite = [0, 2]
                self.walkAnim = False
            elif self.walkCounter < 10:
                self.sprite = [2, 2]
                self.walkAnim = True

        elif pyxel.btnp(pyxel.KEY_A, 1, 1):
            self.render[0] -= 1
            self.true_location[0] -= 1
            got_bumped = False

            for rect in maps.no_go:
                if self.true_location[0] == rect[2]:
                    if (self.true_location[1] <= rect[3]) and (self.true_location[1] + 16 >= rect[1]):
                        self.render[0] += 1
                        self.true_location[0] += 1
                        got_bumped = True
                        break

            if self.render[0] < maps.player_inbound[0] and not got_bumped:
                 self.render[0] += 1
                 maps.shift = "west"

            self.walking = True
            self.direction = "W"
            if self.walkCounter < 5:
                self.sprite = [0, 4]
                self.walkAnim = False
            elif self.walkCounter < 10:
                self.sprite = [2, 4]
                self.walkAnim = True

        elif pyxel.btnp(pyxel.KEY_D, 1, 1):
            self.render[0] += 1
            self.true_location[0] += 1
            got_bumped = False

            for rect in maps.no_go:
                if self.render[0] + 16 == rect[0]:
                    if (self.true_location[1] <= rect[3]) and (self.true_location[1] + 16 >= rect[1]):
                        self.render[0] -= 1
                        self.true_location[0] -= 1
                        got_bumped = True
                        break

            if self.render[0] > maps.player_inbound[1] and not got_bumped:
                self.render[0] -= 1
                maps.shift = "east"

            self.walking = True
            self.direction = "E"
            if self.walkCounter < 5:
                self.sprite = [0, 6]
                self.walkAnim = False
            elif self.walkCounter < 10:
                self.sprite = [2, 6]
                self.walkAnim = True

        else:
            self.walking = False
            self.walkCounter = 0
            self.walkAnim = False

        if self.walking:
            if self.walkCounter < 10:
                self.walkCounter += 1
            else:
                self.walkCounter = 0

        for i in range(-1, 3, 1):
            for j in range(-1, 3, 1):
                self.tileset.append([(self.tile[0] + i), (self.tile[1] + j)])

        # TODO: Update the OOB code to allow player into OOB area
        if self.outOfBounds_X or self.outOfBounds_Y:
            if self.render[0] > 32 and self.outOfBounds_X:
                self.outOfBounds_X = False
            if self.render[1] > 32 and self.outOfBounds_Y:
                self.outOfBounds_Y = False


        if pyxel.btnp(pyxel.KEY_LEFT_BUTTON):
            self.arrows.append(arrow.arrow(self))

        for bolts in self.arrows:
            bolts.update()



