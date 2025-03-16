#!/usr/bin/env python

"""Test module to iterate contents in a directory like walk module."""

from pathlib import Path

from pyspartalib.context.custom.callable_context import Func
from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.default.integer_context import Ints
from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import PathGene
from pyspartalib.script.path.iterate_directory import walk_iterator
from pyspartalib.script.pipeline.log_pipeline import LogPipeline
from pyspartalib.script.pipeline.walk_pipeline import WalkPipeline
from pyspartalib.script.stdout.format_indent import format_indent
from pyspartalib.script.stdout.off_stdout import OffStdout
from pyspartalib.script.stdout.send_stdout import send_stdout


class LaunchTest(WalkPipeline):
    """Class for test to iterate contents in a directory."""

    def __initialize_super_class(self) -> None:
        super().__init__(True)

    def launch_override(self) -> None:
        """Show message when a pipeline module is executed."""
        send_stdout("launch")

    def __init__(self) -> None:
        """Initialize super class and variables."""
        self.__initialize_super_class()


class BreakTest(WalkPipeline):
    def __initialize_super_class(self) -> None:
        super().__init__(True)

    def __initialize_variables(self, iterate_root: Path) -> None:
        self._iterate_root: Path = iterate_root

    def _iteration(self, _: Path) -> bool:
        return True

    def _get_walk(self) -> PathGene:
        return walk_iterator(self._iterate_root, directory=False)

    def launch_override(self) -> None:
        self.walk_directory(self._get_walk, self._iteration)

    def __init__(self, iterate_root: Path) -> None:
        self.__initialize_super_class()
        self.__initialize_variables(iterate_root)


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_expected_launch() -> str:
    return """
        0.0s: begin
        launch
        0.0s: end
    """


def _get_expected_break() -> str:
    return """
        0.0s: begin
        0.0s: find [0] file.json
        0.0s: find [1] file.ini
        0.0s: break
        0.0s: end
    """


def _get_expected_through() -> str:
    return """
        0.0s: begin
        0.0s: find [0] file.json
        0.0s: find [1] file.ini
        0.0s: find [2] file.txt
        0.0s: end
    """


def _get_expected_pair() -> Strs:
    return [_get_expected_break(), _get_expected_through()]


def _get_break_pair() -> Ints:
    return [2, 3]


def _restart_timer(pipeline: LogPipeline) -> None:
    pipeline.restart(override=True)


def _edit_pipeline_launch() -> None:
    pipeline = LaunchTest()
    _restart_timer(pipeline)
    pipeline.launch_pipeline()


def _edit_pipeline_break(break_count: int, iterate_root: Path) -> None:
    pipeline = BreakTest(iterate_root)
    _restart_timer(pipeline)
    pipeline.launch_pipeline(break_count=break_count)


def _get_pipeline_launch() -> Func:
    def _wrapper() -> None:
        _edit_pipeline_launch()

    return _wrapper


def _get_pipeline_break(interrupt: int, iterate_root: Path) -> Func:
    def _wrapper() -> None:
        _edit_pipeline_break(interrupt, iterate_root)

    return _wrapper


def _decorate_function(function: Func) -> str:
    off_stdout = OffStdout()

    @off_stdout.decorator
    def _messages() -> None:
        function()

    _messages()

    return off_stdout.show()


def _get_result_launch() -> str:
    return _decorate_function(_get_pipeline_launch())


def _compare_walk(result: str, expected: str) -> None:
    _difference_error(result, format_indent(expected, stdout=True))


def test_launch() -> None:
    """Test to execute a pipeline module from sub module."""
    _compare_walk(_get_result_launch(), _get_expected_launch())
