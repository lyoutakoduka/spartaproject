#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from typing import List, Dict

SingleSafe = None | bool | int | float | str
Single = SingleSafe | Decimal | Path

JsonSafe = SingleSafe | Dict[str, 'JsonSafe'] | List['JsonSafe']
Json = Single | Dict[str, 'Json'] | List['Json']
