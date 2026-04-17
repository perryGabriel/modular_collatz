from modular_collatz import BaseCollatz, collatz, mod_collatz, recover_value_mod, reduced_collatz


def test_collatz_step_values() -> None:
    assert collatz(3) == 10
    assert reduced_collatz(3) == 5


def test_mod_state_update() -> None:
    x, k, r = mod_collatz(17, 0, 0)
    assert (x, k, r) == (8, 1, 2)
    assert recover_value_mod(x, k, r) == 26


def test_base_collatz_roundtrip() -> None:
    obj = BaseCollatz(17)
    assert obj.expression == [0, 2, 3, 4]
    assert obj.value() == 17
