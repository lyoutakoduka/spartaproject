#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to manage feature flags."""

from logging import Formatter, Handler, Logger, StreamHandler, getLogger


def _config_logger(handler_name: str, handler: Handler) -> Logger:
    logger: Logger = getLogger(handler_name)
    logger.addHandler(handler)

    handler.setFormatter(
        Formatter("%(levelname)s (%(asctime)s) [%(name)s] %(message)s")
    )
    return logger


def in_development(file: str | None = None) -> bool:
    """Check feature flag.

    Args:
        flag (str | None, optional): Defaults to None.
            file path is required if in development.

    Returns:
        bool: return True if in development.
    """
    if file is None:
        return False

    _config_logger("feature_flags", StreamHandler()).info(file)

    return True
