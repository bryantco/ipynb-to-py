from pathlib import Path

import nbformat


def nb_to_py(path: str, add_cell_markers: bool = False) -> None:
    nb = nbformat.read(path, as_version=4)
    cells = [cell.source for cell in nb.cells if cell.cell_type == "code"]

    if add_cell_markers:
        code = "\n\n".join(f"# %%\n{cell}" for cell in cells)
    else:
        code = "\n\n".join(cells)

    with open(path.replace(".ipynb", ".py"), "w") as f:
        f.write(code)


for nb_path in Path(".").glob("**/*.ipynb"):
    nb_to_py(str(nb_path), add_cell_markers=True)