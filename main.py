import pygame
pygame.init()

width, height = 800, 600
fps = 60
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Raycaster")

def draw():
    pass

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