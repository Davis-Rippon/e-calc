from .src.parser import parse_input
from .src.generator import generate_result
from .src.complex import Complex
import readline
import traceback

def print_help():
    print("""Welcome to e-calc!

e-calc is capable of a few operations:

        
""")

def main():
    print("Welcome to e-calc v0.0. Type \"help\" for list of commands.")
    stackTrace = None

    while True:

        try:
            usrIn = input("> ")

            match usrIn:
                case "help":
                    print_help()

                case "st":
                    print(stackTrace)

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

