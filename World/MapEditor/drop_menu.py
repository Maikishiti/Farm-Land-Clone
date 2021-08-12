from mouse import mouse
from button import Button


class DropMenu(Button):
    def __init__(self, rect,

                 color=(0, 0, 0, 0),
                 text='',
                 hover_color=(0, 0, 0, 0),
                 click_color=(0, 0, 0, 0),

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
        super().__init__(rect=rect, color=color, hover_color=hover_color,
                         click_color=click_color, text=text, parent=parent,
                         children=children, move_bar=move_bar,
                         move_bar_color=move_bar_color,
                         move_bar_fill=move_bar_fill, shadow_on=shadow_on,
                         shadow_size=shadow_size, shadow_type=shadow_type,
                         shadow_color=shadow_color, shadow_sides=shadow_sides)
        i = 0
        for button in self.children:
            self.button_distance = button.rect.h
            button.rect.y += self.button_distance * i
            button.hidden = True
            i += 1
        self.active = False
        self.original_width = self.rect.w
        self.original_height = self.rect.h

    def update(self):
        super().update()
        self.clicked()
        i = 0
        for button in self.children:
            button.rect.x = self.rect.x
            self.button_distance = button.rect.h
            button.rect.y = self.rect.y + self.button_distance*i
            i += 1

    def clicked(self):
        i = 0
        for button in self.children:
            if self.rect.collidepoint(mouse.last_clicked) \
                    or (button.rect.collidepoint(mouse.last_clicked)
                        and not button.hidden):
                button.hidden = False
                self.rect.w = button.rect.w
                self.rect.h = button.rect.h * len(self.children)
                i += 1
            else:
                button.hidden = True
                self.rect.w = self.original_width
                self.rect.h = self.original_height
        self.active = i > 0
