import pygame
from pygame import transform
from mouse import mouse
import statics


def gradient(size, color):
    surface = pygame.Surface(size).convert_alpha()
    ratio = (255-color[3])/size[1]
    for y in range(size[1]):
        for x in range(size[0]):
            surface.set_at((x, y), (color[0], color[1], color[2], ratio*y))
    return surface


class Tab(pygame.Surface):
    def __init__(self, rect, color=(0, 0, 0, 0),

                 text='',
                 text_pos=(0, 0),
                 text_size=10,
                 text_font=statics.roboto_mono_medium,
                 text_color=(0, 0, 0),
                 text_antialias=True,
                 text_background=None,

                 parent=None,
                 children=[],

                 move_bar=None,  # Rect
                 move_bar_color=(0, 0, 0, 0),
                 move_bar_fill=0,

                 shadow_on=False,
                 shadow_size=5,
                 shadow_type="outline",
                 shadow_color=(0, 0, 0, 0),
                 shadow_sides={
                     "Left": True,
                     "Right": True,
                     "Top": True,
                     "Bottom": True
    }
    ):
        rect = (0, 0, rect[0], rect[1]) if len(rect) == 2 else rect
        self.rect = pygame.Rect(rect)
        super().__init__(self.rect.size)

        self.moving = False
        self.scaling = False
        self.hidden = False
        self.debug_boxes = False
        self.color = color
        self.fixed = False

        # <> Text Related
        self.text = text
        self.text_pos = text_pos
        self.text_size = text_size
        self.text_font = text_font
        self.text_color = text_color
        self.text_antialias = text_antialias
        self.text_background = text_background
        # </>

        # <> Inheritance Related
        self.parent = parent
        self.children = dict()
        for child in children:
            children[child].parent = self
            self.children[child] = children[child]

        if parent is not None:
            self.parent.children[f'tab{statics.num_of_tabs}'] = self
            self.parent_offset = list()
            self.parent_offset.append(self.rect.x)
            self.parent_offset.append(self.rect.y)
            self.rect.x = self.parent.rect.x + self.parent_offset[0]
            self.rect.y = self.parent.rect.y + self.parent_offset[1]
        # </>

        # <> MoveBar Related
        if move_bar is not None:
            self.move_bar = pygame.Rect(move_bar)
            self.move_bar_offset = self.move_bar.topleft
            self.move_bar.x += self.rect.x
            self.move_bar.y += self.rect.y
        else:
            self.move_bar = self.rect
            self.move_bar_offset = (0, 0)

        self.move_bar_color = move_bar_color
        self.move_bar_fill = move_bar_fill
        # </>

        # <> shadow Related
        self.shadow_on = shadow_on
        self.shadow_on = False if shadow_color[3] == 255 else self.shadow_on
        self.shadow_size = shadow_size
        self.shadow_type = shadow_type
        # Gradient Type can be:
        #     outline
        #     opaque_outline
        #     drop_shadow (not enabled)
        #     opaque_drop_shadow (not enabled)
        self.shadow_alpha = shadow_color[3]
        self.shadow_color = shadow_color
        self.shadow_sides = shadow_sides

        self.base_gradient = \
            gradient((1, 255-self.shadow_alpha), self.shadow_color)
        self.half_gradient = \
            gradient((1, 255-self.shadow_alpha), (
                self.shadow_color[0],
                self.shadow_color[1],
                self.shadow_color[2],
                self.shadow_color[3] + (255 - self.shadow_color[3])/2))
        self.horizontal_gradient = \
            transform.scale(self.base_gradient, (
                self.rect.w, self.shadow_size))
        self.vertical_gradient = \
            transform.scale(self.base_gradient, (
                self.rect.h, self.shadow_size))
        self.corner_gradient = \
            transform.scale(self.half_gradient, (
                int(self.shadow_size*.6), int(self.shadow_size*.6))) \
            if shadow_size > 3 \
            else transform.scale(self.half_gradient, (2, 2))
        if shadow_size == 2 or shadow_size == 1:
            self.corner_gradient = \
                transform.scale(self.half_gradient, (1, 1))

            # </>

        self.fill(color)
        statics.num_of_tabs += 1

    def draw_shadows(self, canvas):
        vertical = horizontal = corner = c_size = size = 0
        if self.shadow_type == "outline":
            vertical = self.vertical_gradient
            horizontal = self.horizontal_gradient
            corner = self.corner_gradient
            c_size = int(self.shadow_size * .6) \
                if int(self.shadow_size*.6) >= 2 \
                else 2
            c_size = 1 if self.shadow_size == 2 else c_size
            size = self.shadow_size

        elif self.shadow_type == "opaque_outline":
            vertical = \
                pygame.Surface((self.rect.h, self.shadow_size),
                               flags=pygame.SRCALPHA)
            horizontal = \
                pygame.Surface((self.rect.w, self.shadow_size),
                               flags=pygame.SRCALPHA)
            corner = \
                pygame.Surface((self.shadow_size, self.shadow_size),
                               flags=pygame.SRCALPHA)

            vertical.fill(self.shadow_color)
            horizontal.fill(self.shadow_color)
            corner.fill(self.shadow_color)
            size = c_size = self.shadow_size

        if self.shadow_sides["Top"]:
            canvas.blit(horizontal, (self.rect.x, self.rect.y-size))

            if self.shadow_sides["Left"]:
                canvas.blit(corner, (self.rect.x-c_size, self.rect.y-c_size))
                canvas.blit(transform.rotate(corner, 90), (
                            self.rect.x-c_size, self.rect.y-c_size))

            if self.shadow_sides["Right"]:
                canvas.blit(corner, (self.rect.right, self.rect.top-c_size))
                canvas.blit(transform.rotate(corner, 270), (
                            self.rect.right, self.rect.top-c_size))

        if self.shadow_sides["Bottom"]:
            canvas.blit(transform.rotate(horizontal, 180), (
                self.rect.left, self.rect.bottom))

            if self.shadow_sides["Right"]:
                canvas.blit(transform.rotate(corner, 180), (
                            self.rect.right, self.rect.bottom))
                canvas.blit(transform.rotate(corner, 270), (
                            self.rect.right, self.rect.bottom))

            if self.shadow_sides["Left"]:
                canvas.blit(transform.rotate(corner, 180), (
                            self.rect.left-c_size, self.rect.bottom))
                canvas.blit(transform.rotate(corner, 90), (
                            self.rect.left-c_size, self.rect.bottom))

        if self.shadow_sides["Right"]:
            canvas.blit(transform.rotate(vertical, 270), (
                self.rect.right, self.rect.top))

        if self.shadow_sides["Left"]:
            canvas.blit(transform.rotate(vertical, 90), (
                        self.rect.x-size, self.rect.top))

    def update(self):
        if self.children is not []:
            for child in self.children.values():
                child.update()
                if not self.moving:
                    if not child.hidden:
                        if not child.fixed:
                            child.move()
        if not self.hidden:
            for child in self.children.values():
                for sub_child in child.children.values():
                    if not (sub_child.rect.collidepoint(mouse.last_clicked)
                            or child.rect.collidepoint(mouse.last_clicked)):
                        if not self.fixed:
                            self.move()

    def draw(self, canvas, pos=None):
        self.rect.topleft = pos if pos is not None else self.rect.topleft
        if not self.hidden:
            self.fill(self.color)
            if self.shadow_on:
                self.draw_shadows(canvas)
            canvas.blit(self, self.rect.topleft)

            # Text Bliting
            canvas.blit(tmp_surface := self.text_font.render(
                self.text,       self.text_antialias,
                self.text_color, self.text_background),
                (self.rect.center[0] + self.text_pos[0]
                 - tmp_surface.get_width()/2,
                 self.rect.center[1] + self.text_pos[1]
                 - tmp_surface.get_height()/2))

            if self.move_bar_fill == 0:
                tmp_surface = pygame.Surface(self.move_bar.size)
                tmp_surface.fill(self.move_bar_color)
                if 3 < len(self.move_bar_color):
                    tmp_surface.set_alpha(self.move_bar_color[3])
                canvas.blit(tmp_surface, self.move_bar)
            else:
                pygame.draw.rect(canvas, self.move_bar_color,
                                 self.move_bar, self.move_bar_fill)
            for child in reversed(self.children.values()):
                child.draw(canvas)

    def move(self):
        # TODO: offset mouse click moving tab

        if self.move_bar.collidepoint(mouse.last_clicked) and mouse.left:
            self.moving = True

        elif self.moving and not mouse.left:
            self.moving = False

        if self.children is not {}:
            for child in self.children.values():
                try:
                    if child.active:
                        self.moving = False
                        print("active")
                except Exception as e:
                    print("not an DropMenu")
                    raise e
                if (child.move_bar.collidepoint(mouse.last_clicked)
                        and mouse.left) or child.moving:
                    self.moving = False
                    child.moving = True

        if self.parent is not None:
            if self.parent.moving and mouse.left:
                self.moving = False

        if self.moving:
            self.rect.x = mouse.pos.x-self.move_bar.w/2-self.move_bar_offset[0]
            self.rect.y = mouse.pos.y-self.move_bar.h/2-self.move_bar_offset[1]
            self.move_bar.x = self.rect.x + self.move_bar_offset[0]
            self.move_bar.y = self.rect.y + self.move_bar_offset[1]
            if self.children is not {}:
                for child in self.children.values():
                    child.rect.x = self.rect.x + child.parent_offset[0]
                    child.rect.y = self.rect.y + child.parent_offset[1]
            if self.parent is not None:
                self.parent_offset[0] = self.rect.x - self.parent.rect.x
                self.parent_offset[1] = self.rect.y - self.parent.rect.y


# <>
# def movable(self):
#     if mouse.pos[0] < self.size + 10 and mouse.pos[0] > self.size - 10:
#         return True
#
# def move(self):
#     if (mouse.left and (mouse.last_clicked[0] < self.size + 10
#                         and mouse.last_clicked[0] > self.size - 10)):
#         self.moving = True
#     elif self.moving and not mouse.left:
#         self.moving = False
#
#     if self.moving:
#         self.size = mouse.pos[0]
# </>
