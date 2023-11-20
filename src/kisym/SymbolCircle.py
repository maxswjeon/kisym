from Fill import Fill
from Stroke import Stroke
from SymbolItem import SymbolItem


class SymbolCircle(SymbolItem):
    def __init__(self, center, radius, stroke: Stroke, fill: Fill):
        super().__init__()
        if type(center) != tuple and len(center) != 2:
            raise TypeError("Center must be a tuple of length 2")

        self.center = center
        self.radius = radius
        self.stroke = stroke
        self.fill = fill

    def str(self, indent=0):
        return (
            f"{'  '*indent}(circle\n"
            + f"{'  '*indent}  (center {self.center[0]:0.2f} {self.center[1]:0.2f})\n"
            + f"{'  '*indent}  (end {self.radius:0.2f})\n"
            + f"{self.stroke.str(indent + 1)}\n"
            + f"{self.fill.str(indent + 1)}\n"
            + f"{'  '*indent})"
        )
