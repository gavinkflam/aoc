"""Reusable regular expression patterns."""

import re


SIGNED_INT = re.compile(r"-?\d+")
UNSIGNED_INT = re.compile(r"\d+")

WHITESPACES = re.compile(r"\s+")
