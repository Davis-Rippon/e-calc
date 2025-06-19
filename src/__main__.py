from .src.parser import parse_input
from .src.generator import generate_result
from .src.complex import Complex
from .src.pager import pager
import argparse
import sys
import readline
import traceback

def print_help():
    print("""
          Expressions:
            e-calc evaluates any maths expression with
                Addition: expr + expr
                Division: expr / expr
                Parallel Addition: expr | expr = 1/(1/expr + 1/expr)
                Multiplication: expr * expr
        
          Functions:
            Expressions can also include the following functions:

                  toCart(magnitude, "cos" or "sin", phase (degrees))
                  Convert a sinusoid to its cartesion complex equivalent
                        
                  vdiv(Voltage, r1, r2)
                  do a voltage divider, finding the voltage across r1

                  toPhasor(expr)
                  print the Phasor representation of a complex number value

                  cdiv(Current, r1, r2)
                  Do a current divider, finding the current across r1

                  pow(x, y)
                  x^y
            
                  capz(frequency, capacitance)
                  Find the impedance of a capacitor

                  indz(frequency, inductance)
                  Find the impedance of a inductor

                  mag(expr)
                  Find the magnitude of expr

                  conj(expr)
                  Find the complex conjugate of expr

          Solver:
          If ran with the '-s' flag, e-calc can solve simultaneous equations:
            
            Example Usage:
              > se
              Equation 1: x + 1 = y
              Equation 2: y*j - 13 = z
              Equation 3: z + x = 12
              variables (space-separated): x y z
              Solution:
                x = 12 - 13*j
                y = 13 - 13*j
                z = 13*j

""")






def main():
    print("Welcome to e-calc v0.0. Type \"help\" for list of commands.")
    stackTrace = None

    sm = 0
    ps = argparse.ArgumentParser()
    ps.add_argument('-s', '--solver', action='store_true',
                        help='Enable Solver (slower startup)')

    args = ps.parse_args()

    if args.solver:
        sm = 1

    while True:

        try:
            usrIn = input("> ")

            match usrIn:
                case "help":
                    print_help()

                case "st":
                    print(stackTrace)

                case newPage if "np" in newPage:
                    try:
                        tokens = newPage.split(" ")
                        num = tokens[1]

                        pager.new_page(num)
                    except IndexError:
                        print("Syntax Error")

                case swPage if "sw" in swPage:
                    try:
                        tokens = newPage.split()
                        num = tokens[1]

                        pager.switch_page(num)
                    except IndexError:
                        print("Syntax Error")

                case assignment if "=" in assignment:

                    try:
                        lst = usrIn.split("=")
                        var = lst[0].strip()
                        value = generate_result(parse_input(lst[1].strip()))
                        pager.add(var, value)
                    except:
                        print("Error in assignment.")

                case "se":
                    if sm:
                        try:
                            equations = []

                            equations.append(input("Equation 1: "))
                            equations.append(input("Equation 2: "))
                            equations.append(input("Equation 3: "))

                            variables = input("variables (space-separated): ")

                            solutions = solve_simultaneous_sympy(equations, variables)

                            if solutions:
                                for sol in solutions:
                                    print("Solution:")
                                    for var, val in sol.items():
                                        print(f"  {var} = {val}")
                            else:
                                print("No solution or infinite solutions")
                        except Exception as e:
                            print(f"An error occured ({e}). Type \"st\" to view Stack Trace") 
                            stackTrace = traceback.format_exc()
                        
                    else:
                        print("Simultaneous Equation Solver Disabled. Run e-calc with -s flag to enable.")

                case "sr":
                    try:
                        pager.show_references()
                    except Exception as e:
                        print(f"An error occured ({e}). Type \"st\" to view Stack Trace") 
                        stackTrace = traceback.format_exc()


                case _:
                    stackTrace = None
                    tokenised = parse_input(usrIn)
                    try:
                        result = generate_result(tokenised)
                        print(result)
                    except Exception as e:
                        print(f"An error occured ({e}). Type \"st\" to view Stack Trace") 
                        stackTrace = traceback.format_exc()

        except KeyboardInterrupt:
            print("\nExiting e-calc...")
            return


def solve_simultaneous_sympy(equations, variable_string):
    from sympy import symbols, Eq, solve, sympify, I
    from sympy.core.sympify import SympifyError
    # Define variables as sympy symbols plus 'j' for imaginary unit
    vars = symbols(variable_string)
    
    # Define a local dictionary to map 'j' to imaginary unit I when sympifying
    local_dict = {'j': I}
    
    eqs = []
    for eq in equations:
        try:
            if '=' not in eq:
                continue
            left, right = eq.split('=')
            eqs.append(Eq(sympify(left.strip(), locals=local_dict),
                          sympify(right.strip(), locals=local_dict)))
        except (ValueError, SympifyError) as e:
            print(f"Skipping invalid equation: {eq} — {e}")
            continue

    if not eqs:
        return "No valid equations provided."

    solution = solve(eqs, vars, dict=True)

    return solution if solution else "No solution or infinitely many solutions."
