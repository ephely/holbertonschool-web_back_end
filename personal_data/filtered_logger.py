#!/usr/bin/python3
""" Regex-ing
"""
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        for field in self.fields:
            message = re.sub(r"({})=([^{}]*)".format(field, self.SEPARATOR),
                             r"\1={}".format(self.REDACTION), message)
        return message


def filter_datum(fields, redaction, message, separator):
    """ Returns the log message obfuscated """
    return re.sub(r"({})=([^{}]*)".format('|'.join(fields), separator),
                  r"\1={}".format(redaction), message)
