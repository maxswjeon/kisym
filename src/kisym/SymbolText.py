from Effects import Effects
from Position import Position
from SymbolItem import SymbolItem


class SymbolText(SymbolItem):
    def __init__(self, text, position: Position, effects: Effects):
        super().__init__()
        self.text = text
        self.position = position
        self.effects = effects

    def str(self, indent=0):
        return (
            f'{"  "*indent}(text "{self.text}" {str(self.position)}\n'
            + f"{self.effects.str(indent + 1)}\n"
            + f"{'  '*indent})"
        )
