#!/usr/bin/env python

"""Module to define types about default module "subprocess"."""

from subprocess import Popen
from typing import IO

POpen = Popen[bytes]
PByte = IO[bytes]
