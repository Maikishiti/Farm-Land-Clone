import pygame
from mouse import mouse
from tab import Tab
from button import Button
from drop_menu import DropMenu  # noqa

pygame.init()
screen_size = 600, 400
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Level Editor")
clock = pygame.time.Clock()

parent_tab = Tab((50, 50, 40, 40), pygame.Color("purple"), "Label",
                 shadow_on=True, shadow_size=2, shadow_color=(139, 58, 98, 200))

tab = DropMenu((10, 10),

               text="b0",

               color=pygame.Color('red'),
               hover_color=(200, 0, 0),
               click_color=(255, 200, 200),

               parent=parent_tab,

               shadow_on=True, shadow_size=2, shadow_color=(139, 58, 98, 200),

               children=[
    Button((30, 20), pygame.Color("blue3"), "B1", (0, 0, 100), (200, 200, 255)),  # noqa
    Button((30, 20), pygame.Color("blue"), "B2", (0, 0, 100), (200, 200, 255)),  # noqa
    Button((30, 20), pygame.Color("skyblue3"), "B3", (0, 0, 100), (200, 200, 255))  # noqa
])

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
