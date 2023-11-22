#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module to execute CLI (Command Line Interface) script on subprocess."""

from subprocess import PIPE, Popen

from pyspartaproj.context.default.string_context import StrGene, Strs, Strs2


def _cleanup_new_lines(text: str) -> str:
    for new_line in reversed("\r\n"):
        if text.endswith(new_line):
            text = text[:-1]

    return text


def _execute(command: str) -> StrGene:
    subprocess = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
    if subprocess.stdout is None:
        raise ValueError

    while True:
        line: bytes = subprocess.stdout.readline()
        if line:
            yield _cleanup_new_lines(line.decode())
        else:
            if subprocess.poll() is not None:
                break


def execute_single(commands: Strs) -> StrGene:
    """Function to execute CLI script on subprocess.

    Args:
        commands (Strs): Script you want to execute corresponding to platform.

    Raises:
        ValueError: Raise error when execution of script fail.

    Returns:
        StrGene: String generator, not string list.

    Yields:
        Iterator[StrGene]: String generator.
    """
    return _execute(" ".join(commands))


def execute_multiple(command_multiple: Strs2) -> StrGene:
    """Function to execute CLI script which is multiple lines on subprocess.

    Args:
        command_multiple (Strs2):
            Script which is multiple lines
            you want to execute corresponding to platform.

    Raises:
        ValueError: Raise error when execution of script fail.

    Returns:
        StrGene: String generator, not string list.

    Yields:
        Iterator[StrGene]: String generator.
    """
    return _execute(
        "; ".join([" ".join(commands) for commands in command_multiple])
    )
