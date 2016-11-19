#!/usr/bin/env python

def distance(strandA, strandB):
    return len(
        [ a for a, b in zip(
            [i for i in strandA], [i for i in strandB]
        ) if a != b ])

if __name__ == '__main__':
    print distance('ABC','ABC')

