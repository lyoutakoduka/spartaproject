#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to execute CLI (Command Line Interface) script on subprocess."""

from subprocess import PIPE, Popen

from pyspartaproj.context.default.string_context import StrGene, Strs


def _cleanup_new_lines(text: str) -> str:
    for new_line in reversed("\r\n"):
        if text.endswith(new_line):
            text = text[:-1]

    return text


def execute_command(commands: Strs) -> StrGene:
    """Function to execute CLI script on subprocess.

    Args:
        commands (Strs): script you want to execute according to OS

    Raises:
        ValueError: raise error when execution of script fail

    Returns:
        StrGene: string generator, not string list

    Yields:
        Iterator[StrGene]: string generator
    """
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
