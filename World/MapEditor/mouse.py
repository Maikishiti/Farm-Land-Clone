import pygame


class Mouse:
    def __init__(self):
        self.pos = pygame.math.Vector2()
        self.left = False
        self.right = False
        self.middle = False
        self.scroll_up = False
        self.scroll_down = False
        self.last_clicked = pygame.math.Vector2()

    def update(self, event=None):
        self.pos = pygame.math.Vector2(pygame.mouse.get_pos())
        self.rel = pygame.math.Vector2(pygame.mouse.get_rel())

        if event is not None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.left = True
                    self.last_clicked = pygame.math.Vector2(
                        pygame.mouse.get_pos())

                if event.button == 2:
                    self.middle = True

                if event.button == 3:
                    self.right = True

                if event.button == 4:
                    self.scroll_up = True

                if event.button == 5:
                    self.scroll_down = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.left = False

                if event.button == 2:
                    self.middle = False

                if event.button == 3:
                    self.right = False

                if event.button == 4:
                    self.scroll_up = False

                if event.button == 5:
                    self.scroll_down = False


mouse = Mouse()
