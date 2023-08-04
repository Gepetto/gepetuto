"""Load / reload / hide code snippets from jupyter notebook."""
from IPython.core.magic import Magics, line_magic, magics_class


@magics_class
class DoNotLoadMagics(Magics):
    """Define a magic ipython command to help loading (or hiding) code snippets."""

    force_load = False

    @line_magic
    def do_not_load_snippet(self, line):
        """Magic command to hide the snippet and let the student code by themself."""
        if DoNotLoadMagics.force_load:
            get_ipython().run_line_magic("run", "-i " + line)
            get_ipython().run_line_magic("load", line)  # noqa: F821

    @line_magic
    def force_load(self, line):
        """Help the author to easily display even "do_not_load" snippets."""
        if line == "" or line == "on" or line == "True" or line == "1":
            DoNotLoadMagics.force_load = True
            print("Force load in ON")
        else:
            DoNotLoadMagics.force_load = False
            print("Force load is OFF")

    @line_magic
    def load_snippet(self, line):
        """Magic command to load and run the snippet, this only work on JupyterLab."""
        get_ipython().run_line_magic("run", "-i " + line)
        get_ipython().run_line_magic("load", line)


ip = get_ipython()  # noqa: F821
ip.register_magics(DoNotLoadMagics)


print(
    """NB: as for all the tutorials, a magic command %do_not_load is introduced to hide
    the solutions to some questions. Change it for %load if you want to see (and
    execute) the solution.""",
)
