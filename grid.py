import math
import math_util as util

class Raycaster:
    def __init__(self, grid):
        self.grid = grid

    def raycast(px, py, dir):
        pass

    def snap_to_grid(px, py, dir):
        xa = util.x_step(px, dir)
        ya = util.y_step(py, dir)

        snap_to_x = xa, util.complete_vec(dir, px=xa)
        snap_to_y = ya, util.complete_vec(dir, py=ya)
        
        if math.hypot(snap_to_x) > math.hypot(snap_to_y):
            return util.vec_add((px, py), snap_to_y)
        else:
            return util.vec_add((px, py), snap_to_x)
