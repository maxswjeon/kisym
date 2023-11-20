from Effects import Effects
from Position import Position


class SymbolPin:
    def __init__(
        self,
        type_,
        style,
        position: Position,
        length,
        name,
        number,
        name_effects: Effects,
        number_effects: Effects,
    ):
        super().__init__()

        if type_ not in [
            "input",
            "output",
            "bidirectional",
            "tri_state",
            "passive",
            "free",
            "power_in",
            "power_out",
            "open_collector",
            "open_emitter",
            "no_connect",
        ]:
            raise ValueError(
                "Type must be one of input, output, bidirectional, tri_state, passive, free, power_in, power_out, open_collector, open_emitter, no_connect"
            )

        if style not in [
            "line",
            "inverted",
            "clock",
            "inverted_clock",
            "input_low",
            "clock_low",
            "output_low",
            "edge_clock_high",
            "non_logic",
        ]:
            raise ValueError(
                "Style must be one of line, inverted, clock, inverted_clock, input_low, clock_low, output_low, edge_clock_high, non_logic"
            )

        self.type = type_
        self.style = style
        self.position = position
        self.length = length
        self.name = name
        self.number = number
        self.name_effects = name_effects
        self.number_effects = number_effects

    def str(self, indent=0):
        return (
            f"{'  '*indent}(pin {self.type} {self.style} {self.position.str()} (length {self.length})\n"
            + f'{"  "*indent}  (name "{self.name}" {self.name_effects.str()})\n'
            + f'{"  "*indent}  (number "{self.number}" {self.number_effects.str()})\n'
            + f"{'  '*indent})"
        )
