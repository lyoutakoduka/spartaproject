#!/usr/bin/env python

"""User defined types using class LogPipeline."""

from collections.abc import Callable

from pyspartalib.script.project.log_pipeline import LogPipeline

LogFunc = Callable[[], LogPipeline]
