import sys
import bboxes

class mapset:

    def __init__(self):
        self.true_location = [0, 0]
        self.render = [0, 0]
        self.tile = [0, 0]
        self.no_go = bboxes.no_go_list
        self.noGo = bboxes.bboxList
        self.occlusion = bboxes.occlist
        self.occlusionList = []
        self.overlay = []
        self.bbox = bboxes.bboxList
        self.player_inbound = [32, 112, 80]
        self.shift = ""

    def update(self, player):
        if not player.outOfBounds_X:
            if self.shift == "west":
                self.render[0] += 1
                self.true_location[0] -= 1
                if self.true_location[0] <= 0:
                    self.true_location[0] = 0
                    self.render[0] = 0
                if self.render[0] > 0:
                    self.render[0] = -7
                    self.tile[0] -= 1
                    if self.tile[0] < 0:
                        self.tile[0] = 0
                self.shift = ""

            elif self.shift == "east":
                self.render[0] -= 1
                self.true_location[0] += 1
                if self.render[0] < -8:
                    self.render[0] = 0
                    self.tile[0] += 1
                self.shift = ""

        if not player.outOfBounds_Y:
            if self.shift == "north":
                self.render[1] += 1
                self.true_location[1] -= 1
                if self.true_location[1] <= 0:
                    self.true_location[1] = 0
                    self.render[1] = 0
                if self.render[1] > 0:
                    self.render[1] = -7
                    self.tile[1] -= 1
                    if self.tile[1] < 0:
                        self.tile[1] = 0
                self.shift = ""

            elif self.shift == "south":
                self.render[1] -= 1
                self.true_location[1] += 1
                if self.render[1] < -7:
                    self.render[1] = 0
                    self.tile[1] += 1
                self.shift = ""

        # check for occlusions
        for section in player.tileset:
            for key in self.occlusion:
                if key['tile'] == section:
                    centerX = section[0]
                    centerY = section[1]
                    drawX = (centerX * 8) - self.true_location[0]
                    drawY = (centerY * 8) - self.true_location[1]
                    colorValue = key['color']
                    self.occlusionList.append([drawX, drawY, centerX, centerY, colorValue])
        player.tileset = []




