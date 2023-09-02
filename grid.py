import math
import math_util as util

class Raycaster:
    def __init__(self, grid):
        self.grid = grid

    def raycast(self, px, py, dir):
        """
        returns collision, distance, tile id
        """
        start = (px, py)
        hit = list(self.snap_to_grid(px, py, dir))
        dir_x = math.cos(dir)
        dir_y = math.sin(dir)

        ray_dist = math.sqrt(dir_x * dir_x + dir_y * dir_y)
        dist_to_x = abs(ray_dist / dir_x) if dir_x != 0 else math.inf
        dist_to_y = abs(ray_dist / dir_y) if dir_y != 0 else math.inf
        step_x = util.sign(dir_x)
        step_y = util.sign(dir_y)

        distance = 0
        ray_len_x, ray_len_y = 0, 0

        while True:
            if ray_len_x < ray_len_y:
                hit[0] += step_x
                distance = ray_len_x
                ray_len_x += dist_to_x
            else:
                hit[1] += step_y
                distance = ray_len_y
                ray_len_y += dist_to_y
            
            tile = self.grid[int(hit[1])][int(hit[0])]
            if tile > 0:
                collision = util.vec_add(start, (dir_x * distance, dir_y * distance))
                return collision, distance, tile



    def snap_to_grid(self, px, py, dir):
        xa = util.x_step(px, dir)
        ya = util.y_step(py, dir)

        snap_to_x = xa, util.complete_vec(dir, px=xa)
        snap_to_y = ya, util.complete_vec(dir, py=ya)
        
        if math.hypot(*snap_to_x) > math.hypot(*snap_to_y):
            return util.vec_add((px, py), snap_to_y)
        else:
            return util.vec_add((px, py), snap_to_x)
