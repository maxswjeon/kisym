from .Fill import Fill
from .Points import Points
from .Stroke import Stroke
from .SymbolItem import SymbolItem


class SymbolCurve(SymbolItem):
    def __init__(self, points: Points, stroke: Stroke, fill: Fill):
        super().__init__()
        self.points = points
        self.stroke = stroke
        self.fill = fill

    def str(self, indent=0):
        return (
            f"{'  '*indent}(curve\n"
            + f"{self.points.str(indent + 1)}\n"
            + f"{self.stroke.str(indent + 1)}\n"
            + f"{self.fill.str(indent + 1)}\n"
            + f"{'  '*indent})"
        )


class SymbolBezier(SymbolCurve):
    pass
