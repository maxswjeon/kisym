class Fill:
    def __init__(self, type):
        self.type = type

    def str(self, indent):
        return f"{'  '*indent}(fill (type {self.type}))"
