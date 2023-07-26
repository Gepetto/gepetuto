"""Add "test" action for the "gepetuto" program."""

import logging

LOG = logging.getLogger("gepetuto.test")


def test(**kwargs):
    """Test python scripts."""
    LOG.info("testing tutorial sources.")
