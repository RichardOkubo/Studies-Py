#!/usr/bin/env python3

import collections


def tokenize(source):
    spaced = source.replace('(', ' ( ').replace(')', ' ) ')
    return collections.deque(spaced.split())


def parse_exp(tokens):
    head = tokens.popleft()
    if head == '(':
        ast = []
        while tokens[0] != ")":
            ast.append(parse_exp(tokens))
        tokens.popleft()  # drop ')'
        return ast
    try:
        return int(head)
    except ValueError:
        return head


if __name__ == '__main__':
    import sys
    print(parse_exp(tokenize(sys.stdin.read())))
