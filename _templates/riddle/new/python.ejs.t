---
to: <%= year %>/<%= day %>/python/main.py
---
#!/usr/bin/env python

from os.path import join, dirname

# Day <%= day %>

# Common


def read_input(filename):
    data = join(dirname(__file__), '..', filename)
    with open(data) as f:
        return f.read().strip()

# 1

# 2
