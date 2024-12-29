#!/usr/bin/env python

"""Module to execute CLI (Command Line Interface) script on subprocess."""

from subprocess import PIPE, Popen

from pyspartalib.context.default.string_context import StrGene, Strs, Strs2
from pyspartalib.script.string.encoding.set_decoding import set_decoding


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
            yield _cleanup_new_lines(set_decoding(line))
        elif subprocess.poll() is not None:
            break


def _join_text(texts: Strs) -> str:
    return " ".join(texts)


def _join_line(texts: Strs) -> str:
    return "; ".join(texts)


def execute_single(commands: Strs) -> StrGene:
    """Execute CLI script on subprocess.

    Args:
        commands (Strs): Script you want to execute corresponding to platform.

    Raises:
        ValueError: Throw an exception if execution of script is failed.

    Returns:
        StrGene: String generator, not string list.

    Yields:
        Iterator[StrGene]: String generator.

    """
    return _execute(_join_text(commands))


def execute_multiple(command_multiple: Strs2) -> StrGene:
    """Execute CLI script which is multiple lines on subprocess.

    Args:
        command_multiple (Strs2):
            Script which is multiple lines
            you want to execute corresponding to platform.

    Raises:
        ValueError: Throw an exception if execution of script is failed.

    Returns:
        StrGene: String generator, not string list.

    Yields:
        Iterator[StrGene]: String generator.

    """
    return _execute(
        _join_line([_join_text(commands) for commands in command_multiple]),
    )
