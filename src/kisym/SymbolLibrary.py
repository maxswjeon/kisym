from .Symbol import Symbol

VERSION = 20220914


class SymbolLibrary:
    def __init__(self):
        self.symbols = []

    def add_symbol(self, symbol: Symbol):
        self.symbols.append(symbol)

    def str(self):
        result = (
            f"(kicad_symbol_lib (version {VERSION}) (generator UMi_KiCAD_Generator)\n"
        )
        for symbol in self.symbols:
            result += f"{symbol.str(1)}\n"
        result += ")"
        return result
