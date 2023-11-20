from .Property import Property
from .SymbolItem import SymbolItem
from .SymbolPin import SymbolPin
from .SymbolRectangle import SymbolRectangle


class Symbol:
    def __init__(
        self,
        name,
        in_bom=None,
        on_board=None,
        unit_name=None,
        pin_count=0,
        pin_spacing=2.54,
        symbol_margin=2.54,
        symbol_width=25.4,
    ):
        self.name = name
        self.in_bom = in_bom
        self.on_board = on_board
        self.properties = []
        self.graphic_items = []
        self.pins = []
        self.units = []
        self.unit_name = unit_name
        self.pin_count = pin_count
        self.pos_index = 0
        self.pin_spacing = pin_spacing
        self.symbol_margin = symbol_margin
        self.symbol_width = symbol_width

    def add_property(self, property: Property):
        self.properties.append(property)

    def add_graphic_item(self, graphic_item: SymbolItem):
        self.graphic_items.append(graphic_item)

    def calculate_square(self, stroke, fill):
        if self.pin_count % 2 == 0:
            square_height = self.pin_count // 2
        else:
            square_height = (self.pin_count + 1) // 2 - 1

        square_height *= self.pin_spacing
        square_height += self.symbol_margin

        start = (-self.symbol_width / 2, square_height)
        end = (self.symbol_width / 2, -square_height)

        return SymbolRectangle(start, end, stroke, fill)

    def next_pin_position(self, direction=-1):
        if self.pin_count % 2 == 0:
            square_height = self.pin_count // 2 - 0.5
        else:
            square_height = (self.pin_count + 1) // 2 - 1

        pos = (square_height + direction * self.pos_index) * self.pin_spacing
        self.pos_index += 1
        return pos

    def add_pin(self, pin: SymbolPin):
        self.pins.append(pin)

    def add_unit(self, unit: "Symbol"):
        self.units.append(unit)

    def str(self, indent=0):
        result = f'{"  "*indent}(symbol "{self.name}"'
        if self.in_bom is not None:
            result += f' (in_bom {"yes" if self.in_bom else "no"})'
        if self.on_board is not None:
            result += f' (on_board {"yes" if self.on_board else "no"})'
        result += "\n"
        for property in self.properties:
            result += f"{property.str(indent + 1)}\n"
        for graphic_item in self.graphic_items:
            result += f"{graphic_item.str(indent + 1)}\n"
        for pin in self.pins:
            result += f"{pin.str(indent + 1)}\n"
        for unit in self.units:
            result += f"{unit.str(indent + 1)}\n"
        if self.unit_name is not None:
            result += f'{"  "*indent}  (unit_name "{self.unit_name}")\n'
        result += f"{'  '*indent})"
        return result
