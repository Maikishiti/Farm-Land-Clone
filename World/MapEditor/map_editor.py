import pygame
from mouse import mouse
from tab import Tab, Button, DropMenu  # noqa

pygame.init()
screen_size = 600, 400
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Level Editor")
clock = pygame.time.Clock()

parent_tab = Tab((50, 50, 40, 40), pygame.Color("purple"),
                 shadow_on=True,
                 shadow_size=2,
                 shadow_color=(139, 58, 98, 200))

tab = DropMenu((55, 55, 10, 10),
               color=pygame.Color('red'),
               hover_color=(200, 0, 0),
               click_color=(255, 200, 200),

               parent=parent_tab,

               shadow_on=True,
               shadow_size=2,
               shadow_color=(139, 58, 98, 200))


running = True
while running:
    screen.fill(pygame.Color('bisque'))
    parent_tab.update()
    parent_tab.draw(screen)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        mouse.update(event)
    clock.tick(60)
pygame.quit()
