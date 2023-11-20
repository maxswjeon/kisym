class Stroke:
    def __init__(self, width, type_, color=None):
        if color is not None and type(color) != tuple and len(color) != 4:
            raise TypeError("Color must be a tuple of length 4 (R G B A)")

        self.width = width
        self.type = type_
        self.color = color

    def str(self, indent=0):
        result = f"{'  '*indent}(stroke (width {self.width}) (type {self.type})"
        if self.color is not None:
            result += f"\n{'  '*indent}  (color {self.color[0]} {self.color[1]} {self.color[2]} {self.color[3]})\n{'  '*indent}"
        result += f")"
        return result
