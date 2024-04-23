from manim import *

class TrapeziumArea(Scene):
	def construct(self):
		trapezium = Polygon([-5, -1, 0], [-3,1,0] , [-1,1,0] , [0, -1, 0],color=TEAL_E,stroke_width=5)
		self.play(Create(trapezium), run_time=0.5)
		self.play(trapezium.animate.set_fill(TEAL_B, opacity=1), run_time=0.4)
		
		l1 = DashedLine([-3,2,0], [-3,-2,0],color=GRAY)
		l2 = DashedLine([-1,2,0],[-1,-2,0],color=GRAY)
		self.play(Create(l1), Create(l2), run_time=0.4)

		brace1 = BraceBetweenPoints([-3,1,0] , [-1,1,0], direction=UP)
		brace1Text = MarkupText("<i>b<sub>2</sub></i>").next_to(brace1, UP)
		brace2 = BraceBetweenPoints([-3,-1,0] , [-1,-1,0], direction=DOWN)
		brace2Text = MarkupText("<i>b<sub>2</sub></i>").next_to(brace2, DOWN)
		brace3 = BraceBetweenPoints([-5,-1,0] , [-3,-1,0], direction=DOWN)
		brace3Text = MarkupText("<i>b<sub>1</sub></i>").next_to(brace3, DOWN)
		brace4 = BraceBetweenPoints([-1,-1,0] , [0,-1,0], direction=DOWN)
		brace4Text = MarkupText("<i>b<sub>3</sub></i>").next_to(brace4, DOWN)
		self.play(
			FadeIn(brace1),FadeIn(brace1Text),
			FadeIn(brace2),FadeIn(brace2Text),
			FadeIn(brace3),FadeIn(brace3Text),
			FadeIn(brace4),FadeIn(brace4Text),
			run_time = 0.4
		)
		
		brace6 = BraceBetweenPoints([0,1,0] , [0,-1,0], direction=RIGHT)
		brace6Text = MarkupText("<i>h</i>").next_to(brace6, RIGHT)
		self.play(FadeIn(brace6),FadeIn(brace6Text), run_time = 0.4)
		self.wait(1)

		equation1 = MathTex(r"Area = ")
		equation1.move_to([1.5, 2.5, 0])
		equation5 = MathTex(r"\frac{b_1h}{2}")
		equation5.next_to(equation1)
		equation6 = MathTex(r"+ \ b_2h")
		equation6.next_to(equation5)
		equation7 = MathTex(r"+ \frac{b_3h}{2}")
		equation7.next_to(equation6)
		self.play(FadeIn(equation1),FadeIn(equation5),FadeIn(equation6),FadeIn(equation7), run_time = 0.4)
		self.wait(1)

		equation2 = MathTex(r"\frac{h(b_1+b_3)}{2}")
		equation2.next_to(equation1)
		self.play(
			ReplacementTransform(equation5, equation2),
			ReplacementTransform(equation7, equation2),
			equation6.animate.next_to(equation2)
		)
		self.wait(1.5)

		equation3 = MathTex(r"+ \frac{2b_2h}{2}")
		equation3.next_to(equation2)
		self.play(ReplacementTransform(equation6, equation3))
		self.wait(1.5)

		equation4 = MathTex(r"\frac{h(b_1+b_3+2b_2)}{2}")
		equation4.next_to(equation1)
		self.play(ReplacementTransform(equation3, equation4),ReplacementTransform(equation2, equation4))
		self.remove(equation3)
		self.remove(equation2)
		self.wait(1.5)

		equation8 = MathTex(r"\frac{h(b_1+b_3+b_2+b_2)}{2}")
		equation8.next_to(equation1)
		self.play(ReplacementTransform(equation4, equation8))
		self.remove(equation4)
		self.wait(1.5)

		brace5 = BraceBetweenPoints([-5,-1,0] , [0,-1,0], direction=DOWN)
		brace5Text = MarkupText("<i>b<sub>4</sub></i>").next_to(brace5, DOWN)
		self.play(
			ReplacementTransform(brace2, brace5),
			ReplacementTransform(brace3, brace5),
			ReplacementTransform(brace4, brace5),
			ReplacementTransform(brace2Text, brace5Text),
			ReplacementTransform(brace3Text, brace5Text),
			ReplacementTransform(brace4Text, brace5Text)
		)
		self.wait(1.5)

		equation9 = MathTex(r"\frac{h(b_4+b_2)}{2}")
		equation9.next_to(equation1)
		self.play(ReplacementTransform(equation8, equation9))
		self.wait(2)

		self.play(
			FadeOut(equation1),
			FadeOut(equation9),
			FadeOut(l1),
			FadeOut(l2),
			FadeOut(brace1),
			FadeOut(brace1Text),
			FadeOut(brace5),
			FadeOut(brace5Text),
			FadeOut(brace6),
			FadeOut(brace6Text),
		)
		self.wait(1)

		trapezium2 = Polygon([-5, -1, 0], [-3,1,0] , [-1,1,0] , [0, -1, 0],color=TEAL_E,stroke_width=5,fill_color=TEAL_B,fill_opacity=1)
		trapezium2.generate_target()
		trapezium2.target.shift(2*UP)
		trapezium.generate_target()
		trapezium.target.shift(DOWN)
		self.play(MoveToTarget(trapezium2),MoveToTarget(trapezium))

		self.play(Rotate(trapezium2),angle=PI, axis= IN)

		trapezium2.generate_target()
		trapezium2.target.shift(4*RIGHT, 3*DOWN)
		self.play(MoveToTarget(trapezium2))
		self.wait(1)

		equation10 = MathTex(r"Area \ of \ this \ parallelogram = (b_2+b_4)*h").shift(UP)
		self.play(FadeIn(equation10), run_time = 0.4)
		self.wait(1.5)

		equation11 = MathTex(r"Area \ of \ this \ trapezium = \frac{(b_2+b_4)*h}{2}").shift(UP)
		self.play(ReplacementTransform(equation10, equation11), trapezium2.animate.set_opacity(0.2))
		self.wait(5)

