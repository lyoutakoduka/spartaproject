#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import PIPE, Popen

from pyspartaproj.context.default.string_context import Strs


def execute_command(commands: Strs) -> Strs:
    subprocess = Popen(
        ' '.join(commands), stdout=PIPE, stderr=PIPE, shell=True
    )
    stdout_byte, _ = subprocess.communicate()
    stdout: str = stdout_byte.decode()
    return stdout.splitlines()
