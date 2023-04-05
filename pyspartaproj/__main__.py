#!/usr/bin/env python
# -*- coding: utf-8 -*-

def show_application():
    import pysparta

    sparta_gui = pysparta.PySpartaGUI()
    sparta_gui.show()


def add_current_path():
    import os

    module_path = __file__
    directory_path = os.path.dirname(module_path)

    import sys

    sys.path.append(directory_path)


def startup():
    add_current_path()
    show_application()


if __name__ == '__main__':
    startup()
