#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal
from pathlib import Path
from typing import List, Dict

Single = None | bool | int | float | str | Decimal | Path

Json = Single | Dict[str, 'Json'] | List['Json']
