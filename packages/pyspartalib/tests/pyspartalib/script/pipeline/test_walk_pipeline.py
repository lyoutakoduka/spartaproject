#!/usr/bin/env python

"""Test module to iterate contents in a directory like walk module."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pyspartalib.context.custom.callable_context import Func
from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.default.integer_context import Ints
from pyspartalib.context.default.string_context import Strs
from pyspartalib.context.extension.path_context import PathFunc, PathGene
from pyspartalib.script.path.iterate_directory import walk_iterator
from pyspartalib.script.path.temporary.create_temporary_tree import (
    create_temporary_tree,
)
from pyspartalib.script.pipeline.log_pipeline import LogPipeline
from pyspartalib.script.pipeline.walk_pipeline import WalkPipeline
from pyspartalib.script.stdout.format_indent import format_indent
from pyspartalib.script.stdout.off_stdout import OffStdout
from pyspartalib.script.stdout.send_stdout import send_stdout


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _inside_temporary_directory(function: PathFunc) -> None:
    with TemporaryDirectory() as temporary_path:
        function(Path(temporary_path))


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


class Shared:
    def restart_timer(self, pipeline: LogPipeline) -> None:
        pipeline.restart(override=True)

    def decorate_function(self, function: Func) -> str:
        off_stdout = OffStdout()

        @off_stdout.decorator
        def _messages() -> None:
            function()

        _messages()

        return off_stdout.show()

    def compare_walk(self, result: str, expected: str) -> None:
        _difference_error(result, format_indent(expected, stdout=True))


class TestLaunch(Shared):
    def _get_expected_launch(self) -> str:
        return """
            0.0s: begin
            launch
            0.0s: end
        """

    def _edit_pipeline_launch(self) -> None:
        pipeline = LaunchTest()
        self.restart_timer(pipeline)
        pipeline.launch_pipeline()

    def _get_pipeline_launch(self) -> Func:
        def _wrapper() -> None:
            self._edit_pipeline_launch()

        return _wrapper

    def _get_result_launch(self) -> str:
        return self.decorate_function(self._get_pipeline_launch())

    def test_launch(self) -> None:
        """Test to execute a pipeline module from sub module."""
        self.compare_walk(
            self._get_result_launch(),
            self._get_expected_launch(),
        )


class TestBreak(Shared):
    def _set_temporary_root(self, temporary_root: Path) -> None:
        self._temporary_root: Path = temporary_root

    def _set_break_count(self, break_count: int) -> None:
        self._break_count: int = break_count

    def _get_expected_break(self) -> str:
        return """
            0.0s: begin
            0.0s: find [0] file.json
            0.0s: find [1] file.ini
            0.0s: break
            0.0s: end
        """

    def _get_expected_through(self) -> str:
        return """
            0.0s: begin
            0.0s: find [0] file.json
            0.0s: find [1] file.ini
            0.0s: find [2] file.txt
            0.0s: end
        """

    def _get_expected_pair(self) -> Strs:
        return [self._get_expected_break(), self._get_expected_through()]

    def _get_break_pair(self) -> Ints:
        return [2, 3]

    def _edit_pipeline_break(self) -> None:
        pipeline = BreakTest(self._temporary_root)
        self.restart_timer(pipeline)
        pipeline.launch_pipeline(break_count=self._break_count)

    def _get_pipeline_break(self) -> None:
        self._edit_pipeline_break()

    def _replace_root(self, result: str) -> str:
        return result.replace(self._temporary_root.as_posix() + "/", "")

    def _get_result_break(self) -> str:
        return self.decorate_function(self._get_pipeline_break)

    def _replace_result_break(self) -> str:
        return self._replace_root(self._get_result_break())

    def _individual_test(self, temporary_root: Path) -> None:
        self._set_temporary_root(temporary_root)
        create_temporary_tree(self._temporary_root, tree_deep=1)

        for expected, break_count in zip(
            self._get_expected_pair(),
            self._get_break_pair(),
            strict=True,
        ):
            self._set_break_count(break_count)
            self.compare_walk(self._replace_result_break(), expected)

    def test_break(self) -> None:
        _inside_temporary_directory(self._individual_test)
