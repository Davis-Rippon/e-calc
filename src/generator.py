from .complex import Complex
from .functions import FUNCTIONS_TABLE

class Generator():
    """
    Language Rules:

        S -> expr                                   print

        expr -> expr + expr                         add(expr, expr)
        expr -> expr / expr                         divide(expr, expr)
        expr -> expr - expr                         subtract(expr, expr)
        expr -> expr | expr                         parallel(expr, expr)
        expr -> ( expr )                            return expr

        expr ->  number                             return Complex(number)
        expr ->  cnumber                            return Complex(0, number)

        number -> CNUM                              return Complex(number)
        cnumber -> CNUM                             return Complex(0, number)

    """

    def __init__(self, tokenised_expression: list):
        self.expr = tokenised_expression


    def match_expr(self, expr): 
        print(f"Match! {expr}")

        for op, method in [('-', self.subtract), 
                           ('+', self.add), 
                           ('*', self.multiply), 
                           ('|', self.parallel),
                           ('/', self.divide)]:

            bFlag = 0
            for idx, ele in enumerate(expr):
                if ele == '(':
                    bFlag += 1
                elif ele == ')':
                    bFlag -= 1

                if (ele == op) & (bFlag == 0):
                    return method(expr[idx + 1:], expr[0:idx])



        for name, function in FUNCTIONS_TABLE:
            if expr[len(expr) - 1]== name:
                args = expr[1:-2][::-1]

                ele = None
                arglist = []
                current = []
                for ele in args:
                    if ele == ',':
                        arglist.append(current)
                        current = []
                        continue
                    current.append(ele)

                if ele is not None:
                    arglist.append(ele)

                print(f"ARGS: {arglist}")
                evaluated_arguments = []
                for argument in arglist:
                    print(argument)
                    evaluated_arguments.append(self.match_expr(argument))

                print(evaluated_arguments)



        if (expr[0] == ')') & (expr[-1] == '('):
            return self.match_expr(expr[1:-1])

        for idx, ele in enumerate(expr):
            match ele:
                case num if isinstance(num, float) & len(expr) == 1:
                    return Complex(ele)

                case complexnum if ((len(expr) == 1) & (ele == 'j')):
                    return Complex(0, 1)

                case complexnum2 if (isinstance(expr[1], float) & (len(expr) == 2) & (expr[0] == 'j')):
                    return Complex(0, expr[1])


        


    def brackets(self, expr):
        """
        Evaluate inside brackets
        """
        return self.match_expr(expr)

    def negate(self, expr):
        return -1 * self.match_expr(expr)

    def divide(self, expr1, expr2):
        l = self.match_expr(expr1)
        r = self.match_expr(expr2)

        return l / r

    def parallel(self, expr1, expr2):
        l = self.match_expr(expr1)
        r = self.match_expr(expr2)

        return l | r

    def multiply(self, expr1, expr2):
        r = self.match_expr(expr2)
        l = self.match_expr(expr1)

        return l * r

    def add(self, expr1, expr2):
        l = self.match_expr(expr1)
        r = self.match_expr(expr2)


        return l + r

    def subtract(self, expr1, expr2):
        l = self.match_expr(expr1)
        r = self.match_expr(expr2)

        return l - r

    def evaluate(self):
        return self.match_expr(self.expr[::-1])

def generate_result(expr):
    g = Generator(expr)
    return g.evaluate()

