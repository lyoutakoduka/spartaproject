#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to handle all functionalities of any script called pipeline."""

from pathlib import Path

from pyspartaproj.script.project.log_pipeline import LogPipeline
from pyspartaproj.script.project.project_context import ProjectContext


class BasePipeline(ProjectContext, LogPipeline):
    """Class to handle all functionalities of any script called pipeline."""

    def __initialize_super_class(
        self, platform: str | None, forward: Path | None
    ) -> None:
        ProjectContext.__init__(self, platform=platform, forward=forward)
        LogPipeline.__init__(self)

    def __init__(
        self, platform: str | None = None, forward: Path | None = None
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
        """
        self.__initialize_super_class(platform, forward)
