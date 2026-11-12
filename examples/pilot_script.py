#!/usr/bin/env python3
"""Example script for the Copilot code review pilot."""

def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}! Welcome to the Copilot review pilot."


def main() -> None:
    print(greet("HeziLiu"))


if __name__ == "__main__":
    main()
