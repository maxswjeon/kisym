from Fill import Fill
from Stroke import Stroke
from SymbolItem import SymbolItem


class SymbolRectangle(SymbolItem):
    def __init__(self, start, end, stroke: Stroke, fill: Fill):
        super().__init__()
        if type(start) != tuple and len(start) != 2:
            raise TypeError("Start must be a tuple of length 2 (X Y)")
        if type(end) != tuple and len(end) != 2:
            raise TypeError("End must be a tuple of length 2 (X Y)")

        self.start = start
        self.end = end
        self.stroke = stroke
        self.fill = fill

    def str(self, indent=0):
        return (
            f"{'  '*indent}(rectangle\n"
            + f"{'  '*indent}  (start {self.start[0]:0.2f} {self.start[1]:0.2f})\n"
            + f"{'  '*indent}  (end {self.end[0]:0.2f} {self.end[1]:0.2f})\n"
            + f"{self.stroke.str(indent + 1)}\n"
            + f"{self.fill.str(indent + 1)}\n"
            + f"{'  '*indent})"
        )
