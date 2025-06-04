from .src.parser import parse_input

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
                    parse_input(usrIn)

        except KeyboardInterrupt:
            print("\nExiting e-calc...")
            break

main()
