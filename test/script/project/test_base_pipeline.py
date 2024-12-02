#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test module to handle I/O functionality of any script called pipeline."""

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.context.extension.path_context import PathPair
from pyspartaproj.script.path.modify.get_resource import get_resource
from pyspartaproj.script.project.base_pipeline import BasePipeline


def _get_expected() -> Strs:
    return ["root", "body", "head"]


def _get_config_file() -> Path:
    return get_resource(local_path=Path("base_pipeline", "forward.json"))


def _get_path_context(pipeline: BasePipeline) -> PathPair:
    return pipeline.get_path_context("test")


def _get_path(pipeline: BasePipeline) -> Path:
    return _get_path_context(pipeline)["print.path"]


def _read_path(pipeline: BasePipeline) -> Strs:
    return list(Path(_get_path(pipeline)).parts)


def _create_pipeline() -> BasePipeline:
    return BasePipeline(forward=_get_config_file())


def test_print() -> None:
    """Test ot show message as log to stdout."""
    assert _get_expected() == _read_path(_create_pipeline())
