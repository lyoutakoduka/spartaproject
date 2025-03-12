#!/usr/bin/env python

from pyspartalib.script.project.walk_pipeline import WalkPipeline


class LaunchTest(WalkPipeline):
    def __initialize_super_class(self) -> None:
        super().__init__(True)

    def __init__(self) -> None:
        self.__initialize_super_class()
