#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from typing import List, Dict

SingleSafe = None | bool | int | float | str

JsonSafe = SingleSafe | Dict[str, 'JsonSafe'] | List['JsonSafe']
Single = SingleSafe | Decimal | Path

Json = Single | Dict[str, 'Json'] | List['Json']
