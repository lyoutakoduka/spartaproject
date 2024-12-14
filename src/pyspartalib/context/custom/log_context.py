#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""User defined types using class LogPipeline."""

from typing import Callable

from pyspartalib.script.project.log_pipeline import LogPipeline

LogFunc = Callable[[], LogPipeline]
