from mouse import mouse
from tab import Tab
from statics import roboto_mono_medium


class Button(Tab):
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

        super().__init__(rect, color, text, text_pos, text_size, text_font,
                         text_color, text_antialias, text_background, parent,
                         children,  move_bar, move_bar_color, move_bar_fill,
                         shadow_on, shadow_size, shadow_type, shadow_color,
                         shadow_sides)
        self.backup_color = color
        self.hover_color = hover_color
        self.click_color = click_color

    def update(self):
        self.moving = False
        if self.children is not {}:
            for child in self.children.values():
                child.update()

        if not self.hidden:
            self.hover()
            if self.clicked():
                self.color = self.click_color

    def move(self): pass

    def hover(self):
        self.color = self.hover_color \
            if self.rect.collidepoint(mouse.pos) \
            else self.backup_color

    def clicked(self):
        return (self.rect.collidepoint(mouse.pos) and mouse.left)
