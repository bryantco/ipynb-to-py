import argparse
from pathlib import Path

import nbformat


def nb_to_py(path: str) -> None:
    nb = nbformat.read(path, as_version=4)
    code = "\n\n".join(cell.source for cell in nb.cells if cell.cell_type == "code")
    with open(path.replace(".ipynb", ".py"), "w") as f:
        f.write(code)


def _iter_notebooks(target: Path):
    if target.is_file() and target.suffix == ".ipynb":
        yield target
    elif target.is_dir():
        yield from target.glob("**/*.ipynb")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Jupyter notebooks to Python files."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["."],
        help="Notebook files or directories to convert (defaults to current directory).",
    )
    args = parser.parse_args()

    for raw_path in args.paths:
        for nb_path in _iter_notebooks(Path(raw_path)):
            nb_to_py(str(nb_path))


if __name__ == "__main__":
    main()