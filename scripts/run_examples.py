"""Quick demonstration script for modular_collatz."""

from modular_collatz import BaseCollatz, collatz, reduced_collatz


def run() -> None:
    print("x -> classic -> reduced")
    for x in range(1, 11):
        print(f"{x:>2} -> {collatz(x):>2} -> {reduced_collatz(x):>2}")

    n = BaseCollatz(17)
    print("\nBaseCollatz expression for 17:", n.expression)
    print("Recovered value:", n.value())


if __name__ == "__main__":
    run()
