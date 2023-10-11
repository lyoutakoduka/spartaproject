#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import PIPE, Popen

from pyspartaproj.context.default.string_context import StrGene, Strs


def _cleanup_new_lines(text: str) -> str:
    for new_line in reversed("\r\n"):
        if text.endswith(new_line):
            text = text[:-1]

    return text


def execute_command(commands: Strs) -> StrGene:
    subprocess = Popen(
        " ".join(commands), stdout=PIPE, stderr=PIPE, shell=True
    )
    if subprocess.stdout is None:
        raise ValueError

    while True:
        line: bytes = subprocess.stdout.readline()
        if line:
            yield _cleanup_new_lines(line.decode())
        else:
            if subprocess.poll() is not None:
                break
