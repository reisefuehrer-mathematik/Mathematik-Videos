from librfm.colors import *

from manim import *

config.background_color = PRIMARY_PALETTE.get_background()

class Example(Scene):
    def construct(self):
        self.function_color = SECOND_COLOR
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-2, 10, 1],
            x_length=10,
            axis_config={"color": MAIN_COLOR},
            x_axis_config={
                "numbers_to_include": np.arange(-4, 4.01, 2),
                "numbers_with_elongated_ticks": np.arange(-4, 4.01, 2),
            },
            tips=False,
        )
        f = axes.plot(lambda x: x**2, color=SECOND_COLOR, x_range=[-np.sqrt(10), np.sqrt(10)])
        g = f.copy().shift(RIGHT*2).set_color(TERTIARY_COLOR)

        f_label = axes.get_graph_label(f, "f(x)=x^2", direction=UP/2, x_val=-np.sqrt(10))
        g_text = MathTex("g(x)=", "f(", "?", ")")
        g_label = axes.get_graph_label(g, g_text, direction=UP/2).shift(RIGHT*2)
        
        self.play(Write(axes))
        self.add(f_label)
        self.play(Create(f))
        self.wait(duration=2)
        self.play(TransformFromCopy(f, g))
        self.play(FadeIn(g_label))
        #self.play(Transform(g_text, MathTex("g(x)=", "f(", "x-2", ")")))

        line = Line(f.get_point_from_function(1), g.get_point_from_function(1)+RIGHT*2).set_color(YELLOW)
        number = DecimalNumber(0, num_decimal_places=1).set_color(YELLOW)
        f_always(number.set_value, line.get_length)
        always(number.next_to, line, UP)

        self.add(number)
        self.play(Create(line))
        self.wait(1)

        line.move_to(axes.i2gp(-5, f))
        self.play(MoveAlongPath(line, f.copy().shift(RIGHT), rum_time=100))
        g_text = MathTex("g(x)=", "f(", "x-", "2", ")", tex_to_color_map={"2": YELLOW})
        tmp = axes.get_graph_label(g, g_text, direction=UP/2).shift(RIGHT*2)
        # Throws an error now:
        # self.play(Transform(number, g_text[2]), TransformMatchingShapes(g_label, tmp))

        return VGroup(axes, f, g, f_label, g_label)
