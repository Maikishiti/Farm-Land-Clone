import pygame
from mouse import mouse

pygame.init()
screen_size = 600, 400
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

sidebar_size = screen_size[0]*5/16
sidebar_move = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        mouse.update(event)

    sidebar = pygame.Surface((sidebar_size, screen_size[1]))

    color = pygame.Color('green') if mouse.left else pygame.Color('red')

    if mouse.pos[0] < sidebar_size + 10 and mouse.pos[0] > sidebar_size - 10:
        color = pygame.Color('blue')

    if (mouse.left and (mouse.last_clicked[0] < sidebar_size + 10
                        and mouse.last_clicked[0] > sidebar_size - 10)):
        sidebar_move = True
    elif sidebar_move and not mouse.left:
        sidebar_move = False

    if sidebar_move:
        sidebar_size = mouse.pos[0]

    screen.fill(pygame.Color('bisque'))
    sidebar.fill(pygame.Color('hotpink4'))

    screen.blit(sidebar, (0, 0))

    pygame.draw.circle(screen, color, mouse.pos, 5)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
