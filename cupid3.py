import pyxel
import arrow


class CupidThree:
    def __init__(self):

        self.tile_location = [0, 0]
        self.tile = [3, 4]
        self.tileset = []
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

        # Move South
        if pyxel.btnp(pyxel.KEY_S, 1, 1):
            got_bumped = False
            self.render[1] += 1
            self.tile_location[1] += 1
            if self.tile_location[1] > 7:
                self.tile[1] += 1
                self.tile_location[1] = 0
            if self.tile_location[1] == 1:
                possible_bump = [[self.tile[0], self.tile[1] + 1], [self.tile[0] + 1, self.tile[1] + 1]]
                for tile in possible_bump:
                    if tile in maps.noGo:
                        got_bumped = True
                        self.tile_location[1] -= 1
                        break
            if (self.render[1] > maps.player_inbound[2]) and not got_bumped:
                maps.shift = "south"
            if (self.render[1] > maps.player_inbound[2]) or got_bumped:
                self.render[1] -= 1

            self.walking = True
            self.direction = "S"
            if self.walkCounter < 5:
                self.sprite = [0, 0]
                self.walkAnim = False
            elif self.walkCounter < 10:
                self.sprite = [2, 0]
                self.walkAnim = True

        elif pyxel.btnp(pyxel.KEY_W, 1, 1):
            got_bumped = False
            self.render[1] -= 1
            self.tile_location[1] -= 1
            if self.tile_location[1] < 0:
                possible_bump = [[self.tile[0], self.tile[1] - 1], [self.tile[0] + 1, self.tile[1] - 1]]
                for tile in possible_bump:
                    if tile in maps.noGo:
                        got_bumped = True
                        self.tile_location[1] += 1
                        break
                if not got_bumped:
                    self.tile[1] -= 1
                    self.tile_location[1] = 7
            if (self.render[1] < maps.player_inbound[0]) and not got_bumped:
                maps.shift = "north"
            if (self.render[1] < maps.player_inbound[0]) or got_bumped:
                self.render[1] += 1

            self.walking = True
            self.direction = "N"
            if self.walkCounter < 5:
                self.sprite = [0, 2]
                self.walkAnim = False
            elif self.walkCounter < 10:
                self.sprite = [2, 2]
                self.walkAnim = True

        elif pyxel.btnp(pyxel.KEY_A, 1, 1):
            got_bumped = False
            self.render[0] -= 1
            self.tile_location[0] -= 1
            if self.tile_location[0] < 0:
                possible_bump = [[self.tile[0] - 1, self.tile[0]], [self.tile[0] - 1, self.tile[1] + 1]]
                for tile in possible_bump:
                    if tile in maps.noGo:
                        got_bumped = True
                        self.tile_location[0] += 1
                        break
                if not got_bumped:
                    self.tile[0] -= 1
                    self.tile_location[0] = 7
            if (self.render[0] < maps.player_inbound[0]) and not got_bumped:
                maps.shift = "west"
            if (self.render[0] < maps.player_inbound[0]) or got_bumped:
                self.render[0] += 1

            self.walking = True
            self.direction = "W"
            if self.walkCounter < 5:
                self.sprite = [0, 4]
                self.walkAnim = False
            elif self.walkCounter < 10:
                self.sprite = [2, 4]
                self.walkAnim = True

        elif pyxel.btnp(pyxel.KEY_D, 1, 1):
            got_bumped = False
            self.render[0] += 1
            self.tile_location[0] += 1
            if self.tile_location[0] > 7:
                self.tile[0] += 1
                self.tile_location[0] = 0
            if self.tile_location[0] == 1:
                possible_bump = [[self.tile[0] + 1, self.tile[1]], [self.tile[0] + 1, self.tile[1] + 1]]
                for tile in possible_bump:
                    if tile in maps.noGo:
                        got_bumped = True
                        self.tile_location[0] -= 1
                        break

            if (self.render[0] > maps.player_inbound[1]) and not got_bumped:
                maps.shift = "east"
            if (self.render[0] > maps.player_inbound[1]) or got_bumped:
                self.render[0] -= 1

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

        self.tileset.append([self.tile[0], self.tile[1]])
        self.tileset.append([self.tile[0], self.tile[1] + 1])
        self.tileset.append([self.tile[0] + 1, self.tile[1]])
        self.tileset.append([self.tile[0] + 1, self.tile[1] + 1])

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