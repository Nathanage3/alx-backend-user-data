#!/usr/bin/env python3
"""
Module for 'filtered_logger'
"""
import bcrypt
from mysql.connector import connection
import logging
import mysql.connector
from typing import List
import os
import re


# Define the PII_FIELDS constant
PII_FIELDS = ("name", "email", "ssn", "phone", "address")


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


def get_db() -> connection.MySQLConnection:
    """
    Connects to the database using credentials stored in environment variables
    and returns the MySQLConnection object.
    """
    db_user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    conn = mysql.connector.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        database=db_name
    )
    return conn


def get_logger() -> logging.Logger:
    """
    Creates a logger named "user_data" that logs up to INFO level
    with a StreamHandler using RedactingFormatter.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create a StreamHandler with RedactingFormatter
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


def main():
    """
    Obtain a database connection, retrieve all rows from the users table,
    and log each row with sensitive information obfuscated.
    """
    db_connection = get_db()
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")

    logger = get_logger()

    for row in cursor:
        message = "; ".join([f"{key}={value}" for key, value in row.items()])
        logger.info(message)
    cursor.close()
    db_connection.close()
    
