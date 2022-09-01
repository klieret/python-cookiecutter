from __future__ import annotations

import logging
from {{cookiecutter.package_name}}.util.log import logger, get_logger


def test_logger():
    logger.info("Hello world")


def test_get_logger():
    assert isinstance(get_logger(), logging.Logger)
