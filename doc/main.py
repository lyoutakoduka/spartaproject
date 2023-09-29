#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""First module called from index.html.

Create simple REPL widget for outside developer.
"""

from asyncio import ensure_future, sleep


async def _main() -> None:
    for i in range(100):
        print(i)
        await sleep(0.01)


ensure_future(_main())
