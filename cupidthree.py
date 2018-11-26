import pyxel
import arrow


class CupidThree:
    def __init__(self):
        self.tile_location = [0, 0]
        self.tile = [1, 1]
        self.true_locationtl = [8, 8]
        self.true_locationbr = [23, 23]
        self.tileset = []
        self.render = [8, 8]
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
            self.true_locationtl[1] += 1
            self.true_locationbr[1] += 1
            self.tile_location[1] += 1
            if 0 > self.tile_location[1] < 2:
                got_bumped = False
                for location in self.testnogo:
                    if (self.true_location[1] + 16) == location[1]:
                        if (self.true_location[0] + 16 - self.tile_location[0]) <= location[0]:
                            got_bumped = True
                if self.tile_location[0] > 0:
                    possible_bump.append([self.tile[0] + 2, self.tile[1] + 2])
                for tile in possible_bump:
                    if tile in maps.noGo:
                        got_bumped = True
                if got_bumped:
                    self.render[1] -= 1
                    self.tile_location[1] -= 1
                else:
                    self.tile[1] += 1
                    self.tile_location[1] = 0
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
            self.tile_location[1] -= 1
            if self.tile_location[1] < 0:
                got_bumped = False
                possible_bump = [[self.tile[0], self.tile[1] - 1], [self.tile[0] + 1, self.tile[1] - 1]]
                if self.tile_location[0] > 0:
                    possible_bump.append([self.tile[0] - 1, self.tile[1] - 1])
                for tile in possible_bump:
                    if tile in maps.noGo:
                        got_bumped = True
                if got_bumped:
                    self.render[1] += 1
                    self.tile_location[1] += 1
                else:
                    self.tile[1] -= 1
                    self.tile_location[1] = 7
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
            self.tile_location[0] -= 1
            if self.tile_location[0] < 0:
                self.tile[0] -= 1
                if self.tile in maps.noGo:
                    self.tile[0] += 1
                    self.render[0] += 1
                    self.tile_location[0] += 1
                else:
                    self.tile_location[0] = 7
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
            self.tile_location[0] += 1
            if self.tile_location[0] > 7:
                self.tile[0] += 1
                if self.tile in maps.noGo:
                    self.tile[0] -= 1
                    self.render[0] -= 1
                    self.tile_location[0] -= 1
                else:
                    self.tile_location[0] = 0
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