#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import PIPE, Popen

from pyspartaproj.context.default.string_context import StrGene, Strs


def execute_command(commands: Strs) -> StrGene:
    subprocess = Popen(
        " ".join(commands), stdout=PIPE, stderr=PIPE, shell=True
    )
    if subprocess.stdout is None:
        raise ValueError

    while True:
        line: bytes = subprocess.stdout.readline()
        if line:
            yield line.decode().replace("\n", "")

        if not line and subprocess.poll() is not None:
            break
