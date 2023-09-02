import math
import math_util as util
import pygame

class Player:
    def __init__(self, px, py, rot, speed, rot_speed, grid):
        self.pos = (px, py)
        self.rot = rot
        self.speed = speed
        self.rot_speed = rot_speed
        self.grid = grid
    
    def process_key_input(self, keys):
        if keys [pygame.K_w]:
            self.move_forward(self.speed)
        elif keys[pygame.K_s]:
            self.move_forward(-self.speed)
        elif keys[pygame.K_a]:
            self.move_right(-self.speed)
        elif keys[pygame.K_d]:
            self.move_right(self.speed)

    def move_forward(self, dist):
        move = (dist * math.cos(self.rot), dist * math.sin(self.rot))
        pos = util.vec_add(self.pos, move)
        self.set_pos_if_empty(pos)

    def move_right(self, dist):
        ang = self.rot + math.pi / 2
        move = (dist * math.cos(ang), dist * math.sin(ang))
        pos = util.vec_add(self.pos, move)
        self.set_pos_if_empty(pos)

    def set_pos_if_empty(self, pos):
        if self.check_if_empty(pos):
            self.pos = pos

    def check_if_empty(self, coord):
        return self.grid.grid[int(coord[1])][int(coord[0])] == 0