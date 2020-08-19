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

'''
Ionian = none
Dorian = b3, b7
Phrygian = b2, b3, b6, b7
Lydian = #4
Mixolydian = b7
Aeolian (Natural Minor) = b3, b6, b7
Locrian = b2, b3, b5, b6, b7

Ionian = Major : none
Dorian = Minor: #6
Phrygian = Minor: b2
Lydian = Major: #4
Mixolydian = Major: b7
Aeolian = Minor : none
Locrian = Minor: b2,  b5

C Major: CDEFGAB
D Dorian: DEFGABC
E Phrygian: EFGABCD

'''
