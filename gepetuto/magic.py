"""Load / reload / hide code snippets from jupyter notebook."""
import logging

from IPython.core.magic import Magics, line_magic, magics_class

LOG = logging.getLogger("gepetuto.magic")


@magics_class
class DoNotLoadMagics(Magics):
    """Define a magic ipython command to help loading (or hiding) code snippets."""

    force_load = False

    @line_magic
    def do_not_load_snippet(self, line):
        """Magic command to hide the snippet and let the student code by themself."""
        if DoNotLoadMagics.force_load:
            self.run("run", "-i " + line)
            self.run("load", line)

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
        self.run("run", "-i " + line)
        self.run("load", line)

    def run(self, magic, line):
        """Run magic command."""
        get_ipython().run_line_magic(magic, line)  # noqa: F821


try:
    ip = get_ipython()
    ip.register_magics(DoNotLoadMagics)
except NameError:
    LOG.warning("didn't found function get_ipython()")


print(
    """NB: as for all the tutorials, a magic command %do_not_load is introduced to hide
    the solutions to some questions. Change it for %load if you want to see (and
    execute) the solution.""",
)
