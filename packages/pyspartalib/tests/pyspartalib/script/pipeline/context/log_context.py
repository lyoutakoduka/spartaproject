#!/usr/bin/env python

"""User defined types using class LogPipeline."""

from collections.abc import Callable

from pyspartalib.script.pipeline.log_pipeline import LogPipeline

LogFunc = Callable[[], LogPipeline]
