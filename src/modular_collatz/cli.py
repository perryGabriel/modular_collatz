"""Command-line entry points for modular_collatz."""

from __future__ import annotations

import argparse

from .core import BaseCollatz, collatz, reduced_collatz


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run Modular Collatz utilities.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    step_parser = subparsers.add_parser("step", help="Run a single Collatz step")
    step_parser.add_argument("x", type=int, help="Input integer")
    step_parser.add_argument(
        "--mode",
        choices=["classic", "reduced"],
        default="classic",
        help="Step function to apply",
    )

    expr_parser = subparsers.add_parser("expression", help="Show base-Collatz expression")
    expr_parser.add_argument("x", type=int, help="Input integer")

    return parser


def main() -> None:
    args = build_parser().parse_args()

    if args.command == "step":
        value = collatz(args.x) if args.mode == "classic" else reduced_collatz(args.x)
        print(value)
    elif args.command == "expression":
        number = BaseCollatz(args.x)
        print(number.expression)
        print(number.value())


if __name__ == "__main__":
    main()
