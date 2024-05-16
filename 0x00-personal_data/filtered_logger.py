#!/usr/bin/env python3
"""
Module for 'filtered_logger'
"""

import logging
import re
from typing import List

def filter_datum(
                fields: List[str], 
                redaction: str,
                message: str, 
                separator: str
                ) -> str:
    """
    Obfuscate specified fields in a log message.

    Parameters:
    fields (List[str]): Fields to obfuscate
    redaction (str): Obfuscation string
    message (str): Log message
    separator (str): Separator character in log message

    Returns:
    str: Obfuscated log message
    """
    pattern = f'({"|".join(fields)})=.*?(?={separator}|$)'
    return re.sub(
        pattern,
        lambda m: m.group(0).split('=')[0] + '=' + redaction,
        message
    )

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format a log record to include obfuscation.

        Parameters:
        record (logging.LogRecord): Log record to be formatted

        Returns:
        str: Formatted log record with obfuscated fields
        """
        original_message = super(RedactingFormatter, self).format(record)
        """
        Filter out sensitive data from a log message.

        Parameters:
        fields (List[str]): Fields to obfuscate
        redaction (str): Obfuscation string
        message (str): Log message
        separator (str): Separator character in log message

        Returns:
        str: Obfuscated log message
        """
        return filter_datum(
            self.fields, self.REDACTION, original_message, self.SEPARATOR
        )
