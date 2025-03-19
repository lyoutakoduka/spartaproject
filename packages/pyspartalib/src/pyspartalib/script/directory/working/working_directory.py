#!/usr/bin/env python

from pathlib import Path


class WorkingDirectory:
    def _set_working_root(self, working_root: Path) -> None:
        self._working_root = working_root
