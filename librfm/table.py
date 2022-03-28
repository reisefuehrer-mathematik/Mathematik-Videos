from manim import *

class Table(VGroup):
    def __init__(self, width, height, num_cols, num_rows, line_color, **kwargs) -> None:
        VGroup.__init__(self, **kwargs)
        self.col_width = width/num_cols
        self.row_height = height/num_rows
        width_half = .5*width
        hline = Line(ORIGIN-width_half*RIGHT, ORIGIN+width_half*RIGHT).set_color(line_color)
        self.add(*hline)
        for col in range(1, num_cols):
            x_pos = ORIGIN+(-width_half+col*self.col_width)*RIGHT
            vline = Line(x_pos+UP, x_pos+DOWN*height).set_color(line_color)
            self.add(*vline)
        
    def get_entry(self, row, column, label: Mobject) -> Mobject:
        pos = self.get_y()*UP + self.get_x()*RIGHT
        label.next_to(pos, direction=row*self.row_height*UP+column*self.col_width*RIGHT)
        return label