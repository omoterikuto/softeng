from plot import Plot

class PlotDot(Plot):
    def plot_inside(self) -> None:
        print("*", end="")

    def plot_outside(self):
        print(" ", end="")

    def next_line(self):
        print()