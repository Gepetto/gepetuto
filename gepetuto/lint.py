"""Add "lint" action for the "gepetuto" program."""

import logging

LOG = logging.getLogger("gepetuto.lint")


def lint(**kwargs):
    """Lint python scripts."""
    LOG.info("linting tutorial sources.")
