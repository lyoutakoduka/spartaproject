#!/usr/bin/env python

"""Module for executing CLI script in a subprocess."""

from subprocess import PIPE, Popen

from pyspartalib.context.default.string_context import StrGene, Strs, Strs2
from pyspartalib.script.error.error_force import ErrorForce
from pyspartalib.script.error.error_raise import ErrorNone
from pyspartalib.script.shell.context.process_context import PByte, POpen
from pyspartalib.script.string.encoding.set_decoding import set_decoding


class _ExecuteBefore:
    def _join_line(self, texts: Strs) -> str:
        return "; ".join(texts)

    def _join_text(self, texts: Strs) -> str:
        return " ".join(texts)

    def _join_commands(self, command_multiple: Strs2) -> Strs:
        return [self._join_text(commands) for commands in command_multiple]

    def get_command_single(self, commands: Strs) -> str:
        return self._join_text(commands)


class ExecuteCommand(_ExecuteBefore, ErrorForce, ErrorNone):
    """Class for executing CLI script in a subprocess."""

    def __initialize_super_class(self, fail_types: Strs | None) -> None:
        ErrorForce.__init__(self, fail_types)

    def _confirm_none(self, result: PByte | None) -> PByte:
        return self.error_none_walrus(result, "process")

    def _select_fail_condition(self, subprocess: POpen) -> PByte | None:
        return None if self.send_signal("process") else subprocess.stdout

    def _confirm_result(self, subprocess: POpen) -> PByte:
        return self._confirm_none(self._select_fail_condition(subprocess))

    def _get_subprocess_result(self, subprocess: POpen) -> bytes:
        return self._confirm_result(subprocess).readline()

    def _cleanup_new_lines(self, text: str) -> str:
        return text.rstrip("\r\n")

    def _break_condition(self, subprocess: POpen) -> bool:
        return subprocess.poll() is not None

    def _get_result_cycle(self, subprocess: POpen) -> StrGene:
        while True:
            if line := self._get_subprocess_result(subprocess):
                yield self._cleanup_new_lines(set_decoding(line))
            elif self._break_condition(subprocess):
                break

    def _execute(self, command: str) -> StrGene:
        return self._get_result_cycle(
            Popen(command, stdout=PIPE, stderr=PIPE, shell=True),
        )

    def execute_single(self, commands: Strs) -> StrGene:
        """Execute the single line CLI script on a subprocess.

        Args:
            commands (Strs):
                The single line CLI script
                    to be executed based on the platform.

        Returns:
            StrGene: The generator of strings, not a list of strings.

        """
        return self._execute(self.get_command_single(commands))

    def execute_multiple(self, command_multiple: Strs2) -> StrGene:
        """Execute the multi-line CLI script on a subprocess.

        Args:
            command_multiple (Strs2):
                The multi-line CLI script
                    to be executed based on the platform.

        Returns:
            StrGene: The generator of strings, not a list of strings.

        """
        return self._execute(
            self._join_line(self._join_commands(command_multiple)),
        )

    def __init__(self, fail_types: Strs | None = None) -> None:
        """Initialize the class variables.

        Args:
            force_fail (bool, optional): Defaults to False.
                If true, retrieving the stack frames will fail.

        """
        self.__initialize_super_class(fail_types)
