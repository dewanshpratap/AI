"""Basic Python starter file."""

def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}! Welcome to your basic Python script."


def main() -> None:
    """Run the main program flow."""
    name = input("Enter your name: ")
    message = greet(name)
    print(message)


if __name__ == "__main__":
    main()
