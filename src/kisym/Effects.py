class Effects:
    def __init__(
        self,
        width,
        height,
        face=None,
        thickness=None,
        bold=False,
        italic=False,
        line_spacing=None,
        justify=None,
        hide=False,
    ):
        self.width = width
        self.height = height
        self.face = face
        self.thickness = thickness
        self.bold = bold
        self.italic = italic
        self.line_spacing = line_spacing
        self.justify = None
        self.hide = hide

        if justify is not None and type(justify) is not tuple:
            raise TypeError("Justify must be a tuple")

        if justify is not None:
            self.justify = [None] * 3

            index = 0

            if justify[index] == "left" or justify[index] == "right":
                self.justify[0] = justify[index]
                index += 1
            if justify[index] == "top" or justify[index] == "bottom":
                self.justify[1] = justify[index]
                index += 1
            if justify[index] == "mirror":
                self.justify[2] = justify[index]
                index += 1

    def str(self, indent=0):
        effects = f"{'  '*indent}(effects (font"
        if self.face is not None:
            effects += f" (face {self.face})"
        effects += f" (size {self.height} {self.width})"
        if self.thickness is not None:
            effects += f" (thickness {self.thickness})"
        if self.bold:
            effects += f" (bold)"
        if self.italic:
            effects += f" (italic)"
        if self.line_spacing is not None:
            effects += f" (line_spacing {self.line_spacing})"
        effects += ")"
        if self.justify is not None:
            effects += f" (justify "
            if self.justify[0] is not None:
                effects += f"{self.justify[0]} "
            if self.justify[1] is not None:
                effects += f"{self.justify[1]} "
            if self.justify[2] is not None:
                effects += f"{self.justify[2]} "
            effects += ")"
        if self.hide:
            effects += " hide"
        effects += ")"

        return effects
