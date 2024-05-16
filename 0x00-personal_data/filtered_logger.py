#!/usr/bin/env python3
"""
Script for handling Personal Data
"""


import logging
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    Obfuscate specified fields in a log message.

    Parameters:
    fields (list[str]): list of fields to be obfuscated
    redaction (str): the string to replace the obfuscated fields with
    message (str): the log message to be obfuscated
    separator (str): the separator used in the log message

    Returns:
    str: the obfuscated log message
    """
    pattern = f'({"|".join(fields)})=.*?(?={separator}|$)'
    return re.sub(pattern, lambda m: m.group(0).split('=')[0] + '=' + redaction, message)
 