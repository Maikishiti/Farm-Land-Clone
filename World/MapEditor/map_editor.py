import pygame
from mouse import mouse
from tab import Tab
from button import Button
from drop_menu import DropMenu

pygame.init()
screen_size = 600, 400
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Level Editor")
clock = pygame.time.Clock()

tab = DropMenu((140, 10),

               text="b0",

               color=(210, 210, 210),
               hover_color=(200, 200, 200),
               click_color=(250, 250, 250),

               parent=Tab((140, screen_size[1]), (190, 190, 200), "Label",
                          shadow_on=False, shadow_size=2,
                          shadow_color=(39, 58, 98, 200)),

               shadow_on=False, shadow_size=2, shadow_color=(39, 58, 98, 200),
               shadow_sides={"Left": False, "Right": False,
                             "Top": False, "Bottom": True},

               children={
    'B1': Button((40, 30), (220, 220, 220), "Botão1",
                 hover_color=(90, 90, 100),
                 click_color=(250, 250, 255),
                 shadow_on=False, shadow_size=2,
                 shadow_color=(39, 58, 98, 200)),

    'B2': Button((40, 30), (230, 230, 230), "Botão2",
                 hover_color=(90, 90, 100),
                 click_color=(250, 250, 255),
                 shadow_on=False, shadow_size=2,
                 shadow_color=(39, 58, 98, 200)),

    'B3': Button((40, 30), (240, 240, 240), "Botão3",
                 hover_color=(90, 90, 100),
                 click_color=(250, 250, 255),
                 shadow_on=False, shadow_size=2,
                 shadow_color=(39, 58, 98, 200)),
})

tab.parent.fixed = True
running = True
while running:
    screen.fill(pygame.Color('bisque'))
    tab.parent.update()
    tab.parent.draw(screen)
    print(tab.children['B1'].clicked())

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        mouse.update(event)
    clock.tick(60)
pygame.quit()
