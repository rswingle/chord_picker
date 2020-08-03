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
             ['I','V','iv','IV'],
             ['I','vi','ii','V'],
             ['I', 'VI7', 'ii', 'IV', 'VII', 'I', 'VI7', 'ii7', 'V7', 'ii', 'V'],
             #['ii', 'V', 'I'],
             #['I', 'vi', 'ii', 'V'],
             #['vi', 'IV', 'I', 'V'],
             #['I', 'II', 'IV', 'I'],
             #['i', 'VII', 'VI', 'V'],
             #['III', 'I', 'i', 'V7', 'i'],
             #[i-V7-i-VII],
             #[I iii IV V],
             #[I IV I V I],
             #[I VI7 ii IV VII I VI7 ii7 V7 ii V],
             #[ii V I],
             #[I I+ I6 I7],
             #[I VI7 II7 V7i]
             ]


x = sample(notes, randint(3,4))

print(x)
