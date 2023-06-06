#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from win32com.client import Dispatch
from win32com.client.dynamic import CDispatch


def read_shortcut(shortcut_path: Path) -> Path:
    shell: CDispatch = Dispatch('WScript.Shell')
    shortcut: CDispatch = shell.CreateShortcut(shortcut_path.as_posix())
    return Path(shortcut.Targetpath)
