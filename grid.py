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
        hit = [px, py]
        dir_x = math.cos(dir)
        dir_y = math.sin(dir)

        ray_dist = math.sqrt(dir_x * dir_x + dir_y * dir_y)
        dist_to_x = abs(ray_dist / dir_x) if dir_x != 0 else math.inf
        dist_to_y = abs(ray_dist / dir_y) if dir_y != 0 else math.inf
        step_x = util.sign(dir_x)
        step_y = util.sign(dir_y)

        distance = 0
        ray_len_x, ray_len_y = 0, 0

        if step_x > 0:
            ray_len_x = (int(px) + 1 - px) * dist_to_x
        else:
            ray_len_x = (px - int(px)) * dist_to_x
        if step_y > 0:
            ray_len_y = (int(py) + 1 - py) * dist_to_y
        else:
            ray_len_y = (py - int(py)) * dist_to_y

        vertical = False
        while True:
            if hit[0] < 0 or hit[1] < 0 \
                    or math.floor(hit[0]) > len(self.grid[0]) - 1 or math.floor(hit[1]) > len(self.grid) - 1:
                return
            
            tile = self.grid[math.floor(hit[1])][math.floor(hit[0])]
            if tile > 0:
                collision = util.vec_add(start, util.vec_scl(dir_x, dir_y, distance))
                return collision, distance, tile, vertical

            if ray_len_x < ray_len_y:
                vertical = True
                hit[0] += step_x
                distance = ray_len_x
                ray_len_x += dist_to_x
            else:
                vertical = False
                hit[1] += step_y
                distance = ray_len_y
                ray_len_y += dist_to_y
