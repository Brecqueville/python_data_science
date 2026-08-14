# ft_package

A sample Python package that provides a function for counting occurrences
of an item in a list.

## Installation

Install the package from its wheel:

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

or

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

How to prove the license "MIT":

```bash
python -c 'import importlib.metadata as m; print(m.metadata("ft_package")["License-Expression"])'
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))
```

Expected output:

```text
2
0
```