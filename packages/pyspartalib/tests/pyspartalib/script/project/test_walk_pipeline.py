#!/usr/bin/env python

from pyspartalib.context.custom.callable_context import Func
from pyspartalib.context.custom.type_context import Type
from pyspartalib.script.project.log_pipeline import LogPipeline
from pyspartalib.script.project.walk_pipeline import WalkPipeline
from pyspartalib.script.stdout.off_stdout import OffStdout
from pyspartalib.script.stdout.send_stdout import send_stdout


class LaunchTest(WalkPipeline):
    def __initialize_super_class(self) -> None:
        super().__init__(True)

    def launch_pipeline(self) -> None:
        send_stdout("launch")

    def __init__(self) -> None:
        self.__initialize_super_class()


def _difference_error(result: Type, expected: Type) -> None:
    if result != expected:
        raise ValueError


def _get_expected_launch() -> str:
    return """
        0.0s: begin
        launch
        0.0s: end
    """


def _restart_timer(pipeline: LogPipeline) -> None:
    pipeline.restart(override=True)


def _edit_pipeline_launch() -> None:
    pipeline = LaunchTest()
    _restart_timer(pipeline)
    pipeline.initialize_pipeline()


def _get_pipeline_launch() -> Func:
    def _wrapper() -> None:
        _edit_pipeline_launch()

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
