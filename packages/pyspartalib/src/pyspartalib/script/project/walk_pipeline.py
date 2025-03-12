#!/usr/bin/env python

from pyspartalib.script.project.log_pipeline import LogPipeline


class WalkPipeline(LogPipeline):
    def __initialize_super_class(self, enable_shown: bool) -> None:
        LogPipeline.__init__(self, enable_shown=enable_shown)

    def launch_pipeline(self) -> None:
        pass

    def __init__(self, enable_shown: bool) -> None:
        self.__initialize_super_class(enable_shown)
