"""Little example program."""

# %jupyter_snippet example
import pinocchio as pin

oma = pin.SE3.Random()
omb = pin.SE3.Random()
amb = oma.inverse() * omb
# %end_jupyter_snippet
