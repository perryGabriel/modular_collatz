# Modular Collatz

A professionalized, installable Python implementation of the algorithms from the original `Collatz.ipynb` notebook, including:

- Traditional Collatz map
- Reduced Collatz map
- Modular Collatz state transitions
- Multi-register modular Collatz updates
- Base-Collatz decomposition and reconstruction

This repository now supports package installation, command-line usage, automated tests, and reproducible example scripts.

## Project structure

```text
.
├── notebooks/                     # Jupyter notebooks
│   ├── Collatz.ipynb              # Original exploratory notebook
│   └── Collatz_plots.ipynb        # Plotting and visualization notebook
├── src/modular_collatz/           # Installable Python package
│   ├── __init__.py
│   ├── core.py                    # Core algorithms
│   └── cli.py                     # CLI entrypoint
├── scripts/run_examples.py        # Example script
├── tests/test_core.py             # Unit tests
├── pyproject.toml                 # Packaging metadata
└── README.md
```

## Installation

### Development install (recommended)

```bash
python -m pip install -e .
```

### Standard install

```bash
python -m pip install .
```

## Quick start

### Python API

```python
from modular_collatz import collatz, reduced_collatz, BaseCollatz

print(collatz(7))         # 22
print(reduced_collatz(7)) # 11

n = BaseCollatz(17)
print(n.expression)       # [0, 2, 3, 4]
print(n.value())          # 17
```

### Command line

Run one Collatz step:

```bash
modular-collatz step 17
modular-collatz step 17 --mode reduced
```

Compute base-Collatz expression:

```bash
modular-collatz expression 17
```

### Example script

```bash
python scripts/run_examples.py
```

## Testing

```bash
pytest
```

## Publication

The associated paper is currently distributed as `Modular Collatz Algorithm.pdf` in this repository.
If/when an arXiv URL is available, add it here for canonical citation.

## Citation

```bibtex
@misc{perry2026_modular_collatz,
  author       = {Perry, Gabriel M.},
  title        = {Modular Collatz},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/perryGabriel/modular_collatz}}
}
```

## License

MIT License. See [LICENSE](LICENSE).
