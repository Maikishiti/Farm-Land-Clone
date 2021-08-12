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

parent_tab = Tab((140, screen_size[1]), (190, 190, 200), "Label",
                 shadow_on=True, shadow_size=2, shadow_color=(39, 58, 98, 200))

tab = DropMenu((140, 10),

               text="b0",

               color=(210, 210, 210),
               hover_color=(200, 200, 200),
               click_color=(250, 250, 250),

               parent=parent_tab,

               shadow_on=True, shadow_size=2, shadow_color=(39, 58, 98, 200),
               shadow_sides={"Left": False, "Right": False,
                             "Top": False, "Bottom": True},

               children=[
    Button((40, 30), (220, 220, 220), "B1", (90, 90, 100), (200, 200, 255),
           shadow_on=True, shadow_size=2, shadow_color=(39, 58, 98, 200)),

    Button((40, 30), (230, 230, 230), "B2", (90, 90, 100), (200, 200, 255),
           shadow_on=True, shadow_size=2, shadow_color=(39, 58, 98, 200)),

    Button((40, 30), (240, 240, 240), "B3", (90, 90, 100), (200, 200, 255),
           shadow_on=True, shadow_size=2, shadow_color=(39, 58, 98, 200)),
])

parent_tab.fixed = True
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
