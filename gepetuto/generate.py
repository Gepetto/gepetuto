"""Add "generate" action for the "gepetuto" program."""

import json
import logging
from pathlib import Path
from typing import List

LOG = logging.getLogger("gepetuto.generate")
HASHTAGS = ["jupyter_snippet"]


def generate(tp_id: List[int], **kwargs):
    """Parse python scripts to generate snippets."""
    LOG.info("generating snippets from tutorial sources.")
    for n in tp_id:
        LOG.debug("Looking for tp %s", n)
        generate_from_id(n)


def generate_from_id(tp_id: int):
    """Find the corresponding ipynb and folder for a given tp_id."""
    folder = Path() / f"tp{tp_id}"
    ipynb = next(Path().glob(f"{tp_id}-*.ipynb"))
    generate_ipynb(ipynb, folder)


def generate_ipynb(ipynb, folder, force_load=False):  # noqa: C901
    """Cut python files in bits loadable by ipython."""
    LOG.info("processing '%s' with scripts in '%s'", ipynb, folder)
    with ipynb.open() as f:
        data = json.load(f)
    for cell in data["cells"]:
        if "outputs" in cell:
            cell["outputs"] = []
    cells_copy = data["cells"].copy()
    generated = folder / "generated"
    generated.mkdir(exist_ok=True)
    for generated_file in generated.glob("*"):
        Path.unlink(generated_file)
    for filename in folder.glob("*.py"):
        LOG.info(" processing '%s'", filename)
        content = []
        dest = None
        with filename.open() as f_in:
            for line_number, line in enumerate(f_in):
                if any(f"# %{hashtag}" in line for hashtag in HASHTAGS):
                    if dest is not None:
                        msg = (
                            f"%{HASHTAGS[0]} block open twice at line {line_number + 1}"
                        )
                        raise SyntaxError(msg)
                    dest = generated / f"{filename.stem}_{line.split()[2]}"
                elif any(line.strip() == f"# %end_{hashtag}" for hashtag in HASHTAGS):
                    if dest is None:
                        msg = (
                            f"%{HASHTAGS[0]} block before open "
                            f"at line {line_number + 1}"
                        )
                        raise SyntaxError(msg)
                    with dest.open("w") as f_out:
                        f_out.write("".join(content))
                    for cell_number, cell in enumerate(cells_copy):
                        if len(cell["source"]) == 0:
                            continue
                        if cell["source"][0].endswith(f"%load {dest}"):
                            data["cells"][cell_number]["source"] = [
                                f"# %load {dest}\n",
                                *content,
                            ]
                        elif cell["source"][0].endswith(f"%load_snippet {dest}"):
                            data["cells"][cell_number]["source"] = [
                                f"# %load {dest}\n",
                                *content,
                            ]
                        elif force_load and cell["source"][0].endswith(
                            f"%do_not_load_snippet {dest}",
                        ):
                            data["cells"][cell_number]["source"] = [
                                f"# %load {dest}\n",
                                *content,
                            ]
                        # if f'%do_not_load {dest}' in cell['source'][0]:
                        # data['cells'][cell_number]['source'] \
                        # = [f'%do_not_load {dest}\n']
                    content = []
                    dest = None
                elif dest is not None:
                    content.append(line)
    with ipynb.open("w") as f:
        f.write(json.dumps(data, indent=1))
