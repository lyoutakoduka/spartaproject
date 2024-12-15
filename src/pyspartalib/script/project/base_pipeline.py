#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to handle all functionalities of any script called pipeline."""

from pathlib import Path

from pyspartalib.script.project.log_pipeline import LogPipeline
from pyspartalib.script.project.project_context import ProjectContext


class BasePipeline(ProjectContext, LogPipeline):
    """Class to handle all functionalities of any script called pipeline."""

    def __initialize_super_class(
        self, platform: str | None, forward: Path | None, enable_shown: bool
    ) -> None:
        ProjectContext.__init__(self, platform=platform, forward=forward)
        LogPipeline.__init__(self, enable_shown=enable_shown)

    def __init__(
        self,
        platform: str | None = None,
        forward: Path | None = None,
        enable_shown: bool = False,
    ) -> None:
        """Initialize super class and variables.

        Args:
            platform (str | None, optional): Defaults to None.
                You can select an execution platform from "linux" or "windows".
                Current execution platform is selected if argument is None.
                It's used for argument "platform" of class "ProjectContext".

            forward (Path | None, optional): Defaults to None.
                Path of setting file in order to place
                    project context file to any place.
                It's used for argument "forward" of class "ProjectContext".

            enable_shown (bool, optional): Defaults to False.
                Log messages are shown if True.
                It's used for argument "enable_shown" of class "LogPipeline".
        """
        self.__initialize_super_class(platform, forward, enable_shown)
