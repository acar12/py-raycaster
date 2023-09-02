import math
import pygame
import grid
pygame.init()

width, height = 1300, 900
fps = 60
fov = math.radians(60)
wall_height = 0.5
dist_to_projection = (width / 2) / math.tan(fov / 2)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Raycaster")

# game set-up
grid = grid.Raycaster([
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
])

def draw():
    for i in range(0, width, 5):
        angle = i / width * fov
        col, dist, tile = grid.raycast(2, 2, angle)
        if tile > 0:
            if dist != 0:
                dist *= math.cos(angle)
                draw_height = wall_height / dist * dist_to_projection
                print(draw_height)
                top = (height - draw_height) // 2
                pygame.draw.rect(screen, (255, 255, 255), (i, top, 5, draw_height))



timer = pygame.time.Clock()
running = True
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # rendering
    draw()
    pygame.display.update()
    # end
    timer.tick(fps)