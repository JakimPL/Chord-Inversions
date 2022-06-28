LOWEST_NOTE = 40
HIGHEST_NOTE = 90
KEYS = {
    0: 'C',
    1: 'C#',
    2: 'D',
    3: 'D#',
    4: 'E',
    5: 'F',
    6: 'F#',
    7: 'G',
    8: 'G#',
    9: 'A',
    10: 'A#',
    11: 'B'
}

CHORDS = {
    '': (0, 4, 7),
    'm': (0, 3, 7),
    'dim': (0, 3, 6),
    'aug': (0, 4, 8),
    'sus2': (0, 2, 7),
    'sus4': (0, 5, 7),
    '7': (0, 4, 7, 10),
    'maj7': (0, 4, 7, 11),
    'm7': (0, 3, 7, 10),
    'm(maj7)': (0, 3, 7, 11)
}

INTERVAL_NAMES = {
    0: 'prime',
    1: 'minor second',
    2: 'major second',
    3: 'minor third',
    4: 'major third',
    5: 'perfect fourth',
    6: 'tritone',
    7: 'perfect fifth',
    8: 'minor sixth',
    9: 'major sixth',
    10: 'minor seventh',
    11: 'major seventh',
    12: 'octave'
}