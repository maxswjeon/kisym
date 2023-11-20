class Position:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def str(self, indent=0):
        return f"{'  '*indent}(at {self.x:.02f} {self.y:.02f} {self.angle})"
