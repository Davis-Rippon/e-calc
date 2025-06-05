from .src.parser import parse_input
from .src.generator import generate_result
from .src.complex import Complex

def print_help():
    print("""Welcome to e-calc!

e-calc is capable of a few operations:

        
""")

def main():
    print("Welcome to e-calc v0.0. Type \"help\" for list of commands.")
    while True:
        try:
            print("> ", end="")
            usrIn = input()

            match usrIn:
                case "help":
                    print_help()

                case _:
                    tokenised = parse_input(usrIn)
                    result = generate_result(tokenised)
                    print(result)

        except KeyboardInterrupt:
            print("\nExiting e-calc...")
            break

main()
