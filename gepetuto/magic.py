from IPython.core.magic import (
    Magics,
    line_magic,
    magics_class,
)


@magics_class
class DoNotLoadMagics(Magics):
    forceLoad = False

    @line_magic
    def do_not_load(self, line):
        if DoNotLoadMagics.forceLoad:
            get_ipython().run_line_magic("load", line)

    @line_magic
    def force_load(self, line):
        if line == "" or line == "on" or line == "True" or line == "1":
            DoNotLoadMagics.forceLoad = True
            print("Force load in ON")
        else:
            DoNotLoadMagics.forceLoad = False
            print("Force load is OFF")


ip = get_ipython()
ip.register_magics(DoNotLoadMagics)


def forceLoad(force=True):
    DoNotLoadMagics.forceLoad = force


print(
    """NB: as for all the tutorials, a magic command %do_not_load is introduced """
    """to hide the solutions to some questions. Change it for %load if you want to see """
    """(and execute) the solution.""",
)
