#! /usr/bin/env python

"""Module to manage feature flags."""

from logging import Formatter, Handler, Logger, StreamHandler, getLogger


def in_development(file: str | None = None) -> bool:
    """Check feature flag.

    Args:
        file (str | None, optional): Defaults to None.
            File path is required if in development.

    Returns:
        bool: True if in development.

    """
    return file is not None
