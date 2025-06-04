class Parser:
    UNIT_PREFIXES = { 
            "G": "e9",    # giga
            "M": "e6",    # mega
            "k": "e3",    # kilo
            "h": "e2",    # hecto
            "da": "e1",   # deka

            "": "e0",     # no prefix (base unit)

            "d": "e-1",   # deci
            "c": "e-2",   # centi
            "m": "e-3",   # milli
            "µ": "e-6",   # micro (unicode mu symbol)
            "u": "e-6",   # micro (alternative)
            "n": "e-9",   # nano
    }
    def __init__(self, expr: str):
        self.current_char = 0
        self.expr_string = expr
        self.tokenised_string = []

    def pfloat(self):
        # Token begins with a number
        output = ""
        ch = self.expr_string[self.current_char]

        while ch.isdigit() or ch == '.':
            try:
                output += ch
                self.current_char += 1
                ch = self.expr_string[self.current_char]
            except IndexError:
                return output

        if ch in Parser.UNIT_PREFIXES:
            output += Parser.UNIT_PREFIXES[ch]

        return output # is it better to return outputs or add them to class' list?

    def parse(self) -> list[str]:
        tokenised_list = []
        return tokenised_list

            


def parse_input(expr):
    p = Parser(expr)
    print(p.pfloat())

