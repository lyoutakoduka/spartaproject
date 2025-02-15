#!/usr/bin/env python


from pathlib import Path

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.extension.path_context import Paths


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_directories(path: Path) -> Paths:
    return [Path(path, group) for group in ["source", "symbolic"]]
