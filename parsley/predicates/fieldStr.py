#!/bin/env python

from functools import reduce


def fieldStr(message, key):
    try:
        val = reduce(lambda m, k: m[k], key if isinstance(key, list) else [key], message)
        return isinstance(val, str)
    except:
        return False
