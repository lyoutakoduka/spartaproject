#!/usr/bin/env python

"""Module to handle I/O functionalities of any script called pipeline."""

from pyspartalib.context.default.string_context import Strs
from pyspartalib.script.time.count.log_timer import LogTimer


class LogPipeline(LogTimer):
    """Class to handle I/O functionalities of any script called pipeline."""

    def __initialize_super_class(self) -> None:
        super().__init__()

    def __initialize_variables(self, enable_shown: bool) -> None:
        self._enable_shown: bool = enable_shown
        self._still_removed: bool = False
        self._log: Strs = []

    def _show_message(self, message: str) -> None:
        if self._enable_shown:
            print(message)
        else:
            self._log += [message]

    def _build_log(self, message_timer: str, messages: Strs) -> str:
        return message_timer + ": " + " ".join(messages)

    def _log_with_timer(self, messages: Strs, force: bool) -> None:
        if message_timer := self.get_readable_time(force=force):
            self._show_message(self._build_log(message_timer, messages))

    def _force_log(self, message: str) -> None:
        self.show_log([message], force=True)

    def _initialize_message(self) -> None:
        self._force_log("begin")

    def _finalize_message(self) -> None:
        self._force_log("end")

    def _confirm_removed(self) -> bool:
        if self._still_removed:
            return True

        self._still_removed = True

        return False

    def get_log(self) -> Strs | None:
        """Get recorded log messages.

        The log is recorded to instance inside
            if you set option to disable showing log.

        You can get the recorded log messages all together from this method.

        Returns:
            Strs | None: Recorded log messages.
        """
        if 0 == len(self._log):
            return None

        log: Strs = self._log[:]
        self._log.clear()

        return log

    def show_log(self, messages: Strs, force: bool = False) -> None:
        """Show log message to stdout.

        Args:
            messages (Strs): Message list which will merged by space character.

            force (bool, optional): Defaults to False.
                Timer count is forcibly returned if it's True.
                It's used for argument "force" of
                    method "get_readable_time" in class "LogTimer".
        """
        self._log_with_timer(messages, force)

    def close_log(self) -> Strs | None:
        """Finalize instance and get logs recorded in instance inside manually.

        Returns:
            Strs | None: Log messages recorded in instance inside.
        """
        if self._confirm_removed():
            return None

        self._finalize_message()

        return self.get_log()

    def __del__(self) -> None:
        """Finalize instance and get logs recorded in instance inside."""
        self.close_log()

    def __init__(self, enable_shown: bool = False) -> None:
        """Initialize super class and variables.

        Args:
            enable_shown (bool, optional): Defaults to False.
                Log messages are shown if True.
        """
        self.__initialize_super_class()
        self.__initialize_variables(enable_shown)
        self._initialize_message()
