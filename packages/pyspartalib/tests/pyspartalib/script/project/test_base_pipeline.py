#!/usr/bin/env python

"""Test module to handle all functionalities of any script called pipeline."""

from pathlib import Path

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import PathPair
from pyspartalib.script.path.modify.get_resource import get_resource
from pyspartalib.script.pipeline.base_pipeline import BasePipeline


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_expected() -> Strs:
    return ["root", "body", "head"]


def _get_config_file() -> Path:
    return get_resource(local_path=Path("base_pipeline", "forward.json"))


def _get_path_context(pipeline: BasePipeline) -> PathPair:
    return pipeline.get_path_context("test")


def _get_path(pipeline: BasePipeline) -> Path:
    return _get_path_context(pipeline)["print.path"]


def _get_result(pipeline: BasePipeline) -> Strs:
    return list(Path(_get_path(pipeline)).parts)


def _create_pipeline() -> BasePipeline:
    return BasePipeline(forward=_get_config_file())


def test_print() -> None:
    """Test to import strings from module outside."""
    _difference_error(_get_result(_create_pipeline()), _get_expected())
