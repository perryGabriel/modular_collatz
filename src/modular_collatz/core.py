"""Core algorithms for the Modular Collatz project."""

from __future__ import annotations

from dataclasses import dataclass, field


def collatz(x: int) -> int:
    """Apply one step of the traditional Collatz map.

    If ``x`` is odd, return ``3x + 1``; otherwise return ``x/2``.
    """
    return int((3 * x + 1) * (x % 2) + x / 2 * (1 - (x % 2)))


def reduced_collatz(x: int) -> int:
    """Apply one step of the reduced Collatz map."""
    return int((x + (2 * x + 1) * (x % 2)) / 2)


def mod_collatz(x: int, k: int, r: int) -> tuple[int, int, int]:
    """Apply one step of the modular Collatz map.

    Returns the updated state ``(x, k, r)``.
    """
    if x % 2 == 1:
        r += 3**k
    if r % 2 == 1:
        k += 1
        r = 3 * r + 1
    r = r // 2
    x = x // 2
    return x, k, r


def recover_value_mod(x: int, k: int, r: int) -> int:
    """Recover integer value from modular state."""
    return x * 3**k + r


def multi_mod_collatz(
    r: list[int],
    k: list[int],
    threshold: int,
    verbose: int = 0,
) -> tuple[list[int], list[int]]:
    """Apply one step of the multi-register modular Collatz map.

    Parameters are mutable lists and are updated in place to match the original
    notebook implementation.
    """
    if len(r) < 2:
        r.append(0)
        k.append(0)
        if verbose > 0:
            print(r, k, "Created a new register")

    i = 0
    while i < len(r) - 1:
        if r[i] % 2 == 1:
            r[i] -= 1
            r[i + 1] += 3**k[i]
        r[i] //= 2

        if verbose > 0:
            print(r, k, f"Collatz on index {i}")

        if r[i] == 0:
            del r[i]
            if i > 0:
                k[i - 1] += k[i]
            del k[i]
            if verbose > 0:
                print(r, k, f"Dropped register at {i}")
        else:
            i += 1

    if r == [1, 0] and k == [0, 0]:
        return [1], [0]

    if r[-1] > threshold:
        r.append(0)
        k.append(0)
        if verbose > 0:
            print(r, k, "Created a new register")

        if r[-2] % 2 == 1:
            r[-2] -= 1
            r[-1] += 3**k[-2]
        r[-2] //= 2
        if verbose > 0:
            print(r, k, "Collatz on second to last register")

    if r[-1] % 2 == 1:
        r[-1] = 3 * r[-1] + 1
        if len(k) > 1:
            k[-2] += 1
    r[-1] //= 2

    if verbose > 0:
        print(r, k, "Collatz on last register")

    return r, k


def recover_value_multi(r: list[int], k: list[int]) -> int:
    """Recover integer value from multi-register representation."""
    value = 0
    for i in range(len(r)):
        value += r[i]
        value *= 3**k[i]
    return value


@dataclass
class BaseCollatz:
    """Representation of a number in base-Collatz decomposition form."""

    x: int = 1
    tail: list[int] = field(default_factory=lambda: [2])
    expression: list[int] = field(default_factory=lambda: [0])

    def __post_init__(self) -> None:
        self.assign(self.x)

    def assign(self, x: int) -> None:
        """Run Collatz decomposition and assign the expression."""
        self.expression = [0]
        while x != 1:
            if x % 2 == 1:
                x = 3 * x + 1
                self.expression.append(0)
            if x == 1:
                break
            x //= 2
            self.expression[-1] += 1

    def value(self) -> int:
        """Recover the represented value using reverse Collatz mapping."""
        d, k, r, y = 0, 0, 0, 0
        x = self.expression.copy()

        while len(x) > 0:
            while len(x) > 0 and x[0] == 0:
                if r % 2 == 0:
                    y += 2**d
                    r += 3**k
                r = 3 * r + 1
                k += 1
                del x[0]

            if r % 2 == 1:
                y += 2**d
                r += 3**k

            d += 1
            r //= 2
            if len(x) > 0:
                x[0] -= 1

        return y


def branches(x: int, k: int, r: int) -> list[int]:
    """Return branch options for diagram generation."""
    del x  # retained for signature compatibility with notebook usage
    if r % 2 == 0:
        stay = r // 2
        up = (3 * r + 3 ** (k + 1) + 1) // 2
    else:
        stay = (r + 3**k) // 2
        up = (3 * r + 1) // 2
    return [stay, up]


def x_bar(k: int, r: int) -> float:
    """Compute x-bar for state visualization."""
    return -r / 3**k
