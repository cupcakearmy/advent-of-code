---
to: <%= year %>/<%= day %>/python/main.py
---
#!/usr/bin/env python

from os.path import join, dirname

# Day 01

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read()

# 1

# 2
