#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path


import setup_pool
from type_info import InitialContext, Strs, Strs_list, Strs_lists, Pair, Pairs


# Messages.
_PLAN_NAME: str = "global_test"
_PLAN_DESCRIPTION: str = "test for all python scripts"

# Paths.
_current_file_path = Path(__file__)  # project/tests/__main__.py
_test_root_path: Path = _current_file_path.parent  # project/tests/
_project_root_path: Path = _test_root_path.parent  # project/
_report_root_path = Path(_test_root_path, 'report')  # project/tests/report/

# Report.
_REPORT_FORMATS: Strs = [
    'json',  # project/tests/report/<_PLAN_NAME>.json
    'pdf',  # project/tests/report/<_PLAN_NAME>.pdf
]

# Assertion.
# result: not show if success
# assertion_detail: maximum level assertion
_REPORT_STYLES: Pairs = {
    'console': {
        'success': 'assertion_detail',
        'error': 'assertion_detail',
    },
    'json': {
        'success': 'assertion_detail',
        'error': 'assertion_detail',
    },
    'pdf': {
        'success': 'assertion_detail',
        'error': 'assertion_detail',
    },
}

# Multi Process testing.
_POOL_NAME: str = 'pool_global'
_PROCESS_COUNT: int = 4  # Max 10
_MODULE_NAME: str = 'process_work'  # tests/process.py

# Test target.
_TEST_TARGETS: Strs_lists = [
    [
        ['tests', '__main__.py'],
        ['scripts', 'sandwich_lines.py'],
    ],
]


def _get_report_paths() -> Pair:
    dot: str = '.'

    report_paths: Pair = {}

    for report_format in _REPORT_FORMATS:
        file_name: str = _PLAN_NAME + dot + report_format
        report_file_path = Path(_report_root_path, file_name)
        report_paths[report_format] = str(report_file_path)

    return report_paths


def _get_module_paths() -> Strs_list:
    process_modules_paths: Strs_list = []

    for process_targets in _TEST_TARGETS:
        module_paths: Strs = []

        for process_target in process_targets:
            module_path: Path = _project_root_path

            for name in process_target:
                module_path = Path(module_path, name)

            module_paths += [str(module_path)]
        process_modules_paths += [module_paths]

    return process_modules_paths


_report_paths: Pair = _get_report_paths()
_process_modules_paths: Strs_list = _get_module_paths()

names: Pair = {
    'pool': _POOL_NAME,
    'module': _MODULE_NAME,
}

_test_conditions = InitialContext(
    report=_report_paths,
    module=_process_modules_paths,
    log=_REPORT_STYLES,
    name=names,
)


def _main() -> bool:
    return setup_pool.run(_test_conditions)


def test() -> bool:
    return _main()


if __name__ == '__main__':
    sys.exit(_main())
