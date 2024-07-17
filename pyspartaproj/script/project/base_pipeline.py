#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from pyspartaproj.script.project.project_context import ProjectContext
from pyspartaproj.script.time.count.log_timer import LogTimer


class BasePipeline(ProjectContext, LogTimer):
    def _initialize_super_class(
        self, platform: str | None, forward: Path | None
    ) -> None:
        ProjectContext.__init__(self, platform=platform, forward=forward)
        LogTimer.__init__(self)

    def __init__(
        self, platform: str | None = None, forward: Path | None = None
    ) -> None:
        self._initialize_super_class(platform, forward)
