import math
import math_util as util
import pygame

class Player:
    def __init__(self, px, py, rot, speed, rot_speed, grid):
        self.pos = (px, py)
        self.rot = math.radians(rot)
        self.speed = speed
        self.rot_speed = math.radians(rot_speed)
        self.grid = grid
    
    def process_key_input(self, keys):
        if keys [pygame.K_w]:
            self.move_forward(self.speed)
        if keys[pygame.K_s]:
            self.move_forward(-self.speed)
        if keys[pygame.K_a]:
            self.move_right(-self.speed)
        if keys[pygame.K_d]:
            self.move_right(self.speed)
        if keys[pygame.K_LEFT]:
            self.rotate(-10)
        if keys[pygame.K_RIGHT]:
            self.rotate(10)

    def rotate(self, x):
        self.rot += x * self.rot_speed 
        self.rot %= math.pi * 2
        

    def move_forward(self, dist):
        move = util.vec_scl(math.cos(self.rot), math.sin(self.rot), dist)
        pos = util.vec_add(self.pos, move)
        self.set_pos_if_empty(pos)

    def move_right(self, dist):
        ang = self.rot + math.pi / 2
        move = util.vec_scl(math.cos(ang), math.sin(ang), dist)
        pos = util.vec_add(self.pos, move)
        self.set_pos_if_empty(pos)

    def set_pos_if_empty(self, pos):
        if self.check_if_empty(pos):
            self.pos = pos

    def check_if_empty(self, coord):
        return self.grid.grid[int(coord[1])][int(coord[0])] == 0