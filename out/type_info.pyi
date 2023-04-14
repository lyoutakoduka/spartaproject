from typing import Dict, List, TypedDict

Strs = List[str]
Pair = Dict[str, str]
Strs_list = List[Strs]
Pairs = Dict[str, Pair]
Strs_lists = List[Strs_list]

class InitialContext(TypedDict):
    report: Pair
    module: Strs_list
    log: Pairs
    name: Pair
