#!/usr/bin/env python

"""Module to execute CLI (Command Line Interface) script on subprocess."""

from subprocess import PIPE, Popen

from pyspartalib.context.custom.type_context import Type
from pyspartalib.context.default.string_context import StrGene, Strs, Strs2
from pyspartalib.script.error.error_raise import ErrorNone
from pyspartalib.script.string.encoding.set_decoding import set_decoding


def _none_error(result: Type | None) -> Type:
    if result is None:
        raise ValueError

    return result


class ExecuteCommand(ErrorNone):
    def __initialize_variables(self, force_fail: bool) -> None:
        self._force_fail: bool = force_fail

    def _get_subprocess_result(self, subprocess: Popen[bytes]) -> bytes:
        return self.error_none_walrus(subprocess.stdout, "process").readline()

    def _cleanup_new_lines(self, text: str) -> str:
        for new_line in reversed("\r\n"):
            if text.endswith(new_line):
                text = text[:-1]

        return text

    def _execute(self, command: str) -> StrGene:
        subprocess = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)

        while True:
            line: bytes = self._get_subprocess_result(subprocess)

            if line:
                yield self._cleanup_new_lines(set_decoding(line))
            elif subprocess.poll() is not None:
                break

    def _join_text(self, texts: Strs) -> str:
        return " ".join(texts)

    def _join_line(self, texts: Strs) -> str:
        return "; ".join(texts)

    def _join_commands(self, command_multiple: Strs2) -> Strs:
        return [self._join_text(commands) for commands in command_multiple]

    def execute_single(self, commands: Strs) -> StrGene:
        """Execute CLI script on subprocess.

        Args:
            commands (Strs): Script you want to execute corresponding to platform.

        Returns:
            StrGene: String generator, not string list.

        """
        return self._execute(self._join_text(commands))

    def execute_multiple(self, command_multiple: Strs2) -> StrGene:
        """Execute CLI script which is multiple lines on subprocess.

        Args:
            command_multiple (Strs2):
                Script which is multiple lines
                you want to execute corresponding to platform.

        Returns:
            StrGene: String generator, not string list.

        """
        return self._execute(
            self._join_line(self._join_commands(command_multiple)),
        )

    def __init__(self, force_fail: bool = False) -> None:
        self.__initialize_variables(force_fail)
