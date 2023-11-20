class Points:
    def __init__(self):
        self.points = []

    def __getitem__(self, index):
        return self.points[index]

    def __setitem__(self, index, value):
        if type(value) != tuple and len(value) != 2:
            raise TypeError("Value must be a tuple of length 2 (X Y)")
        self.points[index] = value

    def str(self, indent=0):
        result = f"{'  '*indent}(pts\n"
        for point in self.points:
            result += f"{'  '*indent}  (xy {point[0]} {point[1]})\n"
        result += f"{'  '*indent})"

        return result
