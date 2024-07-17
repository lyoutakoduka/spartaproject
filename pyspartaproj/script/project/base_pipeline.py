#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.context.default.string_context import Strs
from pyspartaproj.script.project.project_context import ProjectContext
from pyspartaproj.script.time.count.log_timer import LogTimer


class BasePipeline(ProjectContext, LogTimer):
    def _initialize_super_class(
        self, platform: str | None, forward: Path | None
    ) -> None:
        ProjectContext.__init__(self, platform=platform, forward=forward)
        LogTimer.__init__(self)

    def _show_message(self, message: str) -> None:
        print(message)

    def _log_with_timer(self, message: str) -> None:
        if message_timer := self.get_readable_time(force=True):
            self._show_message(message_timer + ": " + message)

    def show_log(self, messages: Strs) -> None:
        self._log_with_timer(" ".join(messages))

    def __init__(
        self, platform: str | None = None, forward: Path | None = None
    ) -> None:
        self._initialize_super_class(platform, forward)
