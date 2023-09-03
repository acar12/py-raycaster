import math
import pygame
import grid
from player import Player
import math_util as util
pygame.init()

# constants
width, height = 1024, 768
fps = 40
fov = math.radians(60)
wall_height = 0.8
dist_to_projection = (width / 2) / math.tan(fov / 2)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Raycaster")

#  textures
textures = [pygame.image.load("textures/wall.png"), pygame.image.load("textures/wall2.png")]
# game set-up
grid = grid.Raycaster([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 2, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 2, 0, 0, 2, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])
max_dist = math.sqrt(len(grid.grid) ** 2 + len(grid.grid[0]) ** 2)
player = Player(
    2, 2, 0,
    0.1, 0.1, 
    grid
)

def draw():
    buff = []
    slice_width = 1
    for i in range(0, width, slice_width):
        rel_ang = (i / width - 0.5) * fov
        angle = rel_ang + player.rot
        raycast = grid.raycast(*player.pos, angle)
        if raycast:
            col, dist, tile, vertical = raycast
            if tile > 0:
                if dist != 0:
                    dist *= math.cos(rel_ang)
                    dist = abs(dist)
                
                    draw_height = wall_height / dist * dist_to_projection
                    top = (height - draw_height) // 2
                    c = 0.2 + 0.8 * ((max_dist - dist) / max_dist)

                    wall_txr = textures[tile - 1]
                    tx = (col[1] if vertical else col[0]) % 1 * wall_txr.get_size()[0]
                    slice = pygame.transform.scale(wall_txr, (wall_txr.get_size()[0], draw_height))
                    screen.blit(slice, (i, top), (tx, 0, slice_width, draw_height))
            buff.append(col)

    # mini-map
    num_rows = len(grid.grid)
    num_cols = len(grid.grid[0])
    cell_size = 15
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, num_rows * cell_size, num_cols * cell_size))
    for i in range(len(grid.grid)):
        for j in range(len(grid.grid[0])):
            if grid.grid[j][i] > 0:
                pygame.draw.rect(screen, (255, 0, 0), 
                    (i * cell_size, j * cell_size, cell_size, cell_size))
                
    pygame.draw.circle(screen, (0, 0, 255), (player.pos[0] * cell_size, player.pos[1] * cell_size), 5)
    for c in buff:
        pygame.draw.line(screen, (0, 255, 0), 
            (player.pos[0] * cell_size, player.pos[1] * cell_size),
            (c[0] * cell_size, c[1] * cell_size))



timer = pygame.time.Clock()
running = True
locked = True
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            locked = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            locked = True
    # custom input processing
    # pygame.event.set_grab(locked)
    player.process_key_input(pygame.key.get_pressed())
    # player.process_mouse_input(*pygame.mouse.get_rel())
    # rendering
    screen.fill((0, 0, 0))
    draw()
    pygame.display.update()
    
    # end
    timer.tick(fps)