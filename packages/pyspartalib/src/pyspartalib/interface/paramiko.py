#!/usr/bin/env python

"""Interface module of "paramiko".

Separate pure python code and other.
"""

from paramiko import (
    AutoAddPolicy,
    Channel,
    SFTPAttributes,
    SFTPClient,
    SSHClient,
)

__all__ = [
    "AutoAddPolicy",
    "Channel",
    "SFTPAttributes",
    "SFTPClient",
    "SSHClient",
]
