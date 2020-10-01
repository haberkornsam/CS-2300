from math import sqrt


class ImplicitEquation:
    def __init__(self, a, b, c, points):
        self.a = a
        self.b = b
        self.c = c
        self.points = points

    def print_distance_from_points(self):
        """
        This function iterates over the points supplied. For each point it calculates the distance away
        and prints the stats about it
        """
        norm = sqrt(pow(self.a, 2) + pow(self.b, 2))

        for point in self.points:
            dist = ((point[0] * self.a) + (point[1] * self.b) + self.c) / norm

            print(f"Distance from point [{point[0]: .1f}, {point[1]: .1f}] to the line is {dist: .1f}."
                  f"{' The point is on the line.' if dist == 0 else ''}")


    def print_implicit_form(self):
        """
        This is the easiest one to "compute". All the numbers have already been supplied
        """
        print(f"Implicit Form: {self.a: .1f}a + {self.b: .1f}b + {self.c: .1f} = 0")

    def print_parameter_form(self):
        """
        Convert implicit to parametric and print!
        """
        point1 = (0.0, (self.c * -1) / self.b) if abs(self.b) > abs(self.a) else ((self.c * -1) / self.a, 0.0)

        print(f"Parameter form: l(t) = [{point1[0]: .1f}, {point1[1]: .1f}] + t[{self.b: .1f}, {self.a * -1: .1f}]")

    def print_point_normal_form(self):
        """
        Calculates the point normal form and prints it out
        """
        print(
            f"Point Normal Form: "
            f"{self.a / abs(self.c): .1f}a + {self.b / abs(self.c): .1f}b + {self.c / abs(self.c): .1f} = 0"
        )

    def print_summary(self):
        """
        Makes my main function cleaner.
        """
        self.print_implicit_form()
        self.print_parameter_form()
        self.print_point_normal_form()
        self.print_distance_from_points()
