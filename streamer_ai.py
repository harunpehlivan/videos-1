from manim import *
from network import NeuralNetworkMobject


class Intro(Scene):
    def construct(self):
        title = TextMobject("Super Mario NEAT")
        title.scale(1.5)
        title.to_edge(UP)
        rect = ScreenRectangle(height=6)
        rect.next_to(title, DOWN)
        self.play(
            FadeInFromDown(title),
            ShowCreation(rect)
        )
        self.wait(2)


class InputANN(Scene):
    def construct(self):
        mario = SVGMobject("files/mario.svg")
        a = Arrow(LEFT, RIGHT, color=RED)

        nn = SVGMobject("files/nn.svg")
        nn.move_to(2.5 * RIGHT)

        head = TextMobject("Artificial Neural Network", color=BLUE)
        head.move_to(2 * UP)
        head.scale(1.5)

        foot = TextMobject("Recommender System", color=RED)
        foot.move_to(2 * DOWN)
        foot.scale(1.5)

        self.play(ShowCreation(mario))
        self.play(ApplyMethod(mario.shift, 2.5 * LEFT), ShowCreation(a))
        self.play(ShowCreation(nn))
        self.wait(2)

        self.play(ShowCreation(head))
        self.wait(2)

        self.play(ShowCreation(foot))
        self.wait(2)


class NeuralNetwork(Scene):
    def construct(self):
        network = NeuralNetworkMobject([3, 4, 3], 0.15)
        network.scale(2.5)

        neuron_arrow = Arrow(ORIGIN, 1 * UP)
        neuron_arrow.next_to(network, 1 * UP)

        neuron_text = TextMobject("Neurons")
        neuron_text.next_to(neuron_arrow, 1 * UP)

        input_arrow = Arrow(1 * LEFT, ORIGIN, color=BLUE)
        input_arrow.next_to(network, 2 * LEFT)

        input_text = TextMobject("Inputs", color=BLUE)
        input_text.next_to(input_arrow, 1 * UP)

        output_arrow = Arrow(ORIGIN, 1 * RIGHT, color=RED)
        output_arrow.next_to(network, 2 * RIGHT)

        output_text = TextMobject("Outputs", color=RED)
        output_text.next_to(output_arrow, 1 * UP)

        weight_arrow = Arrow(2 * LEFT, 2 * LEFT + 2 * DOWN)

        weight_text = TextMobject("Weights")
        weight_text.next_to(weight_arrow, 1 * DOWN)

        brace = Brace(VGroup(network), DOWN)
        text = brace.get_text("Bias")

        self.play(ShowCreation(network))
        self.wait(2)

        self.play(ShowCreation(neuron_arrow), ShowCreation(neuron_text))
        self.wait(2)

        self.play(ShowCreation(input_arrow), ShowCreation(input_text))
        self.wait(2)

        self.play(ShowCreation(output_arrow), ShowCreation(output_text))
        self.wait(2)

        self.play(ShowCreation(weight_arrow), ShowCreation(weight_text))
        self.wait(2)

        self.play(ShowCreation(brace), ShowCreation(text))
        self.wait(2)


class Sigmoid(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": 0,
        "y_max": 1,
        "graph_origin": 3 * DOWN,
        "function_color": RED,
        "axes_color": WHITE,
        "x_labeled_nums": range(-5, 6, 2)
    }

    def construct(self):
        text = TextMobject("Sigmoid")
        text.scale(2)
        text.move_to(3 * UP)

        self.setup_axes(animate=True)

        self.play(ApplyMethod(self.axes.scale, 0.75))

        func_graph = self.get_graph(self.sigmoid, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label=r"\sigma (x) = max(x, \alpha x)", color=WHITE)
        graph_lab.scale(0.75)

        brace = Brace(VGroup(func_graph), LEFT)
        b_text = brace.get_tex(r"0 < \sigma (x) < 1")

        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(graph_lab))
        self.play(ShowCreation(text))

        self.play(ShowCreation(brace), ShowCreation(b_text))
        self.wait(2)

    def sigmoid(self, x):
        return 1 / (1 + math.e ** (-x))


class Relu(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "function_color": GREEN,
        "axes_color": WHITE,
        "x_labeled_nums": range(-5, 6, 2)
    }

    def construct(self):
        text = TextMobject("ReLU")
        text.scale(2)
        text.move_to(3 * UP)

        self.setup_axes(animate=True)

        self.play(ApplyMethod(self.axes.scale, 0.75))

        func_graph = self.get_graph(self.relu, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label=r"y = max(x, \alpha x)")

        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(graph_lab))
        self.play(ShowCreation(text))
        self.wait(2)

    @staticmethod
    def relu(x):
        return max(x, 0)


class LeakyRelu(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "function_color": BLUE,
        "axes_color": WHITE,
        "x_labeled_nums": range(-5, 6, 2)
    }

    def construct(self):
        text = TextMobject("Leaky ReLU")
        text.scale(2)
        text.move_to(3 * UP)

        self.setup_axes(animate=True)

        self.play(ApplyMethod(self.axes.scale, 0.75))

        func_graph = self.get_graph(self.leaky_relu, self.function_color)
        graph_lab = self.get_graph_label(func_graph, label=r"y = max(x, \alpha x)")

        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(graph_lab))
        self.play(ShowCreation(text))
        self.wait(2)

    @staticmethod
    def leaky_relu(x):
        return max(x, x / 4)


class SoftMax(GraphScene):
    def construct(self):
        equation = TexMobject(r"\sigma (x_j) = \frac{e^{x_j}}{\sum _i {e^{x_i}}")
        head = TextMobject("Softmax", color=GREEN)

        equation.scale(2)
        head.scale(2)
        head.move_to(2 * UP)

        self.play(ShowCreation(head))
        self.play(ShowCreation(equation))
        self.wait(2)


class LayerToLayer(Scene):
    def construct(self):
        nn = NeuralNetworkMobject([5, 1], 0.2)
        nn.scale(2)
        nn.add_input_labels()
        nn.add_y()
        nn.add_weight_labels()
        nn.shift(0.75 * UP)

        eq = TexMobject(r"y = \sigma (w_1x_1 + w_2x_2 + w_3x_3 + w_4x_4)")
        eq.scale(1.5)
        eq.shift(3 * DOWN)

        self.play(ShowCreation(nn))
        self.play(ShowCreation(eq))
        self.wait(2)


class BackProp(Scene):
    def construct(self):
        network = NeuralNetworkMobject([3, 4, 3])
        network.scale(2)

        back = Arrow(2.5 * UP + 1 * RIGHT, 2.5 * UP + 1 * LEFT, color=RED)
        text = TextMobject("Backpropagation")
        text.shift(3 * UP)

        self.play(ShowCreation(network))
        self.play(ShowCreation(back), ShowCreation(text))
        self.wait(2)


class NeuroEvolution(Scene):
    def construct(self):
        n = 3
        m = 1

        shift = [
            m * UP + n * LEFT,
            m * UP,
            m * UP + n * RIGHT,
            m * DOWN + n * LEFT,
            m * DOWN,
            m * DOWN + n * RIGHT
        ]
        scores = [
            "312",
            "434",
            "145",
            "254",
            "332",
            "521"
        ]
        scores2 = [
            "624",
            "512",
            "765",
            "432",
            "332",
            "521"
        ]

        head = TextMobject("Neuroevolution", color=RED)
        head.scale(2)
        head2 = TextMobject("Neuroevolution", color=RED)
        head2.scale(2)
        head2.shift(3 * UP)

        rep = TextMobject("This process is repeated", color=BLUE)
        rep.scale(2)

        one = TextMobject("1994", color=RED)
        one.scale(2)

        survival = TextMobject("Survival of the fittest")
        survival.scale(1.5)
        survival.shift(2 * DOWN)

        net_group = VGroup()
        text_group = VGroup()
        text_group2 = VGroup()

        circle1 = Circle(color=GREEN)
        circle1.shift(shift[5])

        circle2 = Circle(color=GREEN)
        circle2.shift(shift[1])

        circle3 = Circle(color=GREEN)
        circle3.shift(shift[0])

        circle4 = Circle(color=GREEN)
        circle4.shift(shift[2])

        for i in range(6):
            net = NeuralNetworkMobject([2, 3, 2])
            net.shift(shift[i])
            net_group.add(net)

            text = TextMobject(scores[i])
            text.shift(shift[i])
            text.scale(1.5)
            text_group.add(text)

            text2 = TextMobject(scores2[i])
            text2.shift(shift[i])
            text2.scale(1.5)
            text_group2.add(text2)

        self.play(ShowCreation(one))
        self.play(Transform(one, head))
        self.play(ShowCreation(survival))
        self.wait(2)

        self.play(ApplyMethod(one.shift, 3 * UP), Transform(survival, head2))
        self.play(ShowCreation(net_group))
        self.wait(2)

        self.play(ShowCreation(text_group))
        self.wait(2)

        self.play(ShowCreation(circle1), ShowCreation(circle2))
        self.wait(2)

        self.play(Transform(circle1, net_group),
                  Uncreate(circle2),
                  Uncreate(text_group),
                  Uncreate(net_group))
        self.wait(2)

        self.play(ShowCreation(text_group2))
        self.play(ShowCreation(circle3), ShowCreation(circle4))

        self.wait(2)

        self.play(Uncreate(circle1),
                  Uncreate(text_group2),
                  Uncreate(circle3),
                  Uncreate(circle4),
                  ShowCreation(rep)
                  )
        self.wait(2)


class TWEANN(Scene):
    def construct(self):
        network1 = NeuralNetworkMobject([3, 4, 3])
        network2 = NeuralNetworkMobject([2, 3, 3])
        network3 = NeuralNetworkMobject([4, 2, 3])
        network4 = NeuralNetworkMobject([3, 2, 3])

        f = 2
        network1.scale(f)
        network2.scale(f)
        network3.scale(f)
        network4.scale(f)

        sub = TextMobject("Topology and Weight Evolving Artificial Neural Networks")
        head = TextMobject("TWEANNs", color=BLUE)
        head.scale(1.5)

        head.shift(3.5 * UP)
        sub.shift(2.5 * UP)

        sub2 = TextMobject("Neuroevolution of Augmenting Topologies")
        head2 = TextMobject("NEAT", color=RED)
        head2.scale(1.5)

        head2.shift(3.5 * UP)
        sub2.shift(2.5 * UP)

        self.play(ShowCreation(head), ShowCreation(sub))
        self.play(ShowCreation(network1))
        self.wait()

        self.play(Transform(network1, network2))
        self.wait()

        self.play(Transform(network1, network3))
        self.wait()

        self.play(Transform(network1, network4))
        self.wait()

        self.play(Transform(sub, sub2), Transform(head, head2))
        self.wait(2)


class Commentary(Scene):
    def construct(self):
        head = TextMobject("Commentary")
        head.scale(2)
        head.shift(2 * UP)

        node1 = TextMobject("Thanking")
        node1.scale(1.5)
        node1.shift(3 * LEFT + 3 * DOWN)

        node2 = TextMobject("Actual Commentary")
        node2.scale(1.5)
        node2.shift(3 * RIGHT + 3 * DOWN)

        l1 = Line(1 * UP, ORIGIN, color=GREEN)
        l2 = Line(3 * RIGHT, 3 * LEFT, color=GREEN)
        l3 = Line(3 * RIGHT, 3 * RIGHT + 1 * DOWN, color=GREEN)
        l4 = Line(3 * LEFT, 3 * LEFT + 1 * DOWN, color=GREEN)

        self.play(ShowCreation(head), ShowCreation(l1), ShowCreation(l2))
        self.play(ShowCreation(l3), ShowCreation(l4))
        self.play(ShowCreation(node1), ShowCreation(node2))
