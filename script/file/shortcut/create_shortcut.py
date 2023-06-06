#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from win32com.client import Dispatch
from win32com.client.dynamic import CDispatch


def create_shortcut(shortcut_target: Path, target_root: Path) -> Path:
    shortcut_path: Path = Path(target_root, shortcut_target.name + '.lnk')

    shell: CDispatch = Dispatch('WScript.Shell')
    shortcut: CDispatch = shell.CreateShortcut(shortcut_path.as_posix())
    shortcut.Targetpath = 'file:/' + shortcut_target.as_posix()
    shortcut.Save()

    return shortcut_path
