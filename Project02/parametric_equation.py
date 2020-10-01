from Project02.implicit_equation import ImplicitEquation


class ParametricEquation(ImplicitEquation):
    """
    This class is needed because multiple constructors are not allowed in python ://
    All this does is convert the given parametric equation to implicit form, then pass
    it up the chain to the implicit class
    """
    def __init__(self, p: (float, float), v: (float, float), points):
        self.p = p
        self.v = v

        a = self.v[1] * -1, self.v[0]
        c = (-1 * a[0] * self.p[0]) - (a[1] * self.p[1])
        super(ParametricEquation, self).__init__(a[0], a[1], c, points)

    def print_parameter_form(self):
        """
        Override the other parameter form method so that we get the original from the file rather
        than a different equation for the same line
        """
        print(f"Parameter form: l(t) = [{self.p[0]: .1f}, {self.p[1]: .1f}] + t[{self.v[0]: .1f}, {self.v[1]: .1f}]")
