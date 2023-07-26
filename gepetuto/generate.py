"""Add "generate" action for the "gepetuto" program."""

import logging

LOG = logging.getLogger("gepetuto.generate")


def generate(**kwargs):
    """Parse python scripts to generate snippets."""
    LOG.info("generating snippets from tutorial sources.")
