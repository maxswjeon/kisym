from .Effects import Effects
from .Position import Position


class Property:
    def __init__(self, key, value, position: Position, effects: Effects):
        self.key = key
        self.value = value
        self.position = position
        self.effects = effects

    def str(self, indent=0):
        return (
            f'{"  "*indent}(property "{self.key}" "{self.value}" '
            + f"{self.position.str()}\n"
            + f"{self.effects.str(indent + 1)}\n"
            + f"{'  '*indent})"
        )
