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


test = read_input('test.txt')
data = read_input('input.txt')

# 1
print('1.')

# 2
print('\n2.')
