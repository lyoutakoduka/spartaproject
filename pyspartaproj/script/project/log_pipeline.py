#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyspartaproj.script.time.count.log_timer import LogTimer


class LogPipeline(LogTimer):
    def __initialize_super_class(self) -> None:
        super().__init__()

    def _show_message(self, message: str) -> None:
        print(message)

    def _log_with_timer(self, message: str, force: bool) -> None:
        if message_timer := self.get_readable_time(force=force):
            self._show_message(message_timer + ": " + message)

    def __init__(self) -> None:
        self.__initialize_super_class()
