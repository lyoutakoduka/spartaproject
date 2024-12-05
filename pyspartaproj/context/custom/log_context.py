#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable

from pyspartaproj.script.project.log_pipeline import LogPipeline

LogFunc = Callable[[], LogPipeline]
