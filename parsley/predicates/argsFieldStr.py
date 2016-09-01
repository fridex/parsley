#!/bin/env python

from functools import reduce


def argsFieldStr(node_args, key):
    try:
        val = reduce(lambda m, k: m[k], key if isinstance(key, list) else [key], node_args)
        return isinstance(val, str)
    except:
        return False
