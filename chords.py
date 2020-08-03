#!/usr/bin/env python3

from random import *

notes = ['A','Bb','B','C','C#','D','D#','E','F','F#','G','G#']

#intervals = ['I','II','III','IV','V','VI','VII']
#Define what intervals sound right for rock
def interval(prog):
    inter = [['I,III','V'],
    ['I','IV','V'],
    ['I','IV','V','VI'],
    ['I','V','IV','IV'],
    ['I','IV','V'],
    ['V','IV','I'],
    ['I','V','iv','IV']
    ]


x = sample(notes, randint(3,4))

#if interval(x) "matches"

print(x)
