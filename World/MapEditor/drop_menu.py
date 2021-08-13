from mouse import mouse
from button import Button
from statics import roboto_mono_medium


class DropMenu(Button):
    def __init__(self, rect, color=(0, 0, 0, 0),

                 text='',
                 text_pos=(0, 0),
                 text_size=10,
                 text_font=roboto_mono_medium,
                 text_color=(0, 0, 0),
                 text_antialias=True,
                 text_background=None,

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
        super().__init__(text_color=text_color, text_background=text_background,
                         click_color=click_color, move_bar_color=move_bar_color,
                         text=text, text_size=text_size,
                         hover_color=hover_color, text_antialias=text_antialias,
                         move_bar=move_bar, text_pos=text_pos,
                         color=color, parent=parent, children=children,
                         move_bar_fill=move_bar_fill, shadow_on=shadow_on,
                         shadow_size=shadow_size, rect=rect,
                         text_font=text_font, shadow_type=shadow_type,
                         shadow_color=shadow_color, shadow_sides=shadow_sides)
        i = 0
        for button in self.children.values():
            self.button_distance = button.rect.h
            button.rect.y += (self.button_distance * i)
            button.hidden = True
            button.shadow_sides["Top"] = False
            button.shadow_sides["Right"] = True
            button.shadow_sides["Left"] = True
            button.shadow_sides["Bottom"] = True
            i += 1
        self.active = False
        self.original_width = self.rect.w
        self.original_height = self.rect.h

    def update(self):
        super().update()
        self.clicked()
        i = 0
        for button in self.children.values():
            button.rect.x = self.rect.x
            self.button_distance = button.rect.h
            button.rect.y = self.original_height + self.rect.y \
                + self.button_distance*i
            i += 1

    def clicked(self):
        i = 0
        for button in self.children.values():
            if self.rect.collidepoint(mouse.last_clicked) \
                    or (button.rect.collidepoint(mouse.last_clicked)
                        and not button.hidden):
                button.hidden = False
                self.rect.h = button.rect.h * len(self.children) \
                    + self.original_height
                i += 1
            else:
                button.hidden = True
                self.rect.w = self.original_width
                self.rect.h = self.original_height
        self.active = i > 0
