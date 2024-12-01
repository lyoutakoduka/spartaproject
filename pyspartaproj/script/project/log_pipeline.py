#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.script.time.count.log_timer import LogTimer


class LogPipeline(LogTimer):
    def __initialize_super_class(self) -> None:
        super().__init__()

    def __init__(self) -> None:
        self.__initialize_super_class()
