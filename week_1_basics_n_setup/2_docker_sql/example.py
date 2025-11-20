import argparse
import logging
from datetime import datetime
from pathlib import Path

#!/usr/bin/env python3
"""
example.py - Basic Python example showing functions, a class, argparse, logging, and simple file output.
"""



def greet(name: str) -> str:
    """Return a simple greeting for a given name."""
    return f"Hello, {name}!"


class Person:
    """Simple Person class with a greet method."""

    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return greet(self.name)


def build_messages(person: Person, count: int) -> list[str]:
    """Create a list of timestamped greetings."""
    now = datetime.utcnow().isoformat(timespec="seconds") + "Z"
    return [f"{now} - {person.greet()} ({i+1}/{count})" for i in range(count)]


def main():
    parser = argparse.ArgumentParser(description="Basic Python example script.")
    parser.add_argument("--name", "-n", default="World", help="Name to greet")
    parser.add_argument("--count", "-c", type=int, default=1, help="How many greetings to produce")
    parser.add_argument("--out", "-o", type=Path, help="Optional output file to save greetings")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logging.info("Starting example script")

    person = Person(args.name)
    messages = build_messages(person, max(1, args.count))

    for msg in messages:
        print(msg)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text("\n".join(messages) + "\n", encoding="utf-8")
        logging.info("Wrote greetings to %s", args.out)


if __name__ == "__main__":
    main()