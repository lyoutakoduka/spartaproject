#!/usr/bin/env python

from pathlib import Path


class WorkingDirectory:
    def _set_working_root(self, working_root: Path) -> None:
        self._working_root = working_root

    def get_working_root(self) -> Path:
        return self._working_root
