# -*- coding, utf-8 -*-

from collections import OrderedDict

QUALITY_DICT = OrderedDict((
    # chords consist of 2 notes
    ('5', [0, 7]),
    # 3 notes
    ('', [0, 4, 7]),
    ('maj', [0, 4, 7]),
    ('m', [0, 3, 7]),
    ('min', [0, 3, 7]),
    ('dim', [0, 3, 6]),
    ('aug', [0, 4, 8]),
    ('sus2', [0, 2, 7]),
    ('sus4', [0, 5, 7]),
    # 4 notes
    ('6', [0, 4, 7, 9]),
    ('7', [0, 4, 7, 10]),
    ('7-5', [0, 4, 6, 10]),
    ('7+5', [0, 4, 8, 10]),
    ('7sus4', [0, 5, 7, 10]),
    ('m7', [0, 3, 7, 10]),
    ('m7-5', [0, 3, 6, 10]),
    ('dim6', [0, 3, 6, 9]),
    ('M7', [0, 4, 7, 11]),
    ('M7+5', [0, 4, 8, 11]),
    ('mM7', [0, 3, 7, 11]),
    ('add9', [0, 4, 7, 14]),
    ('2', [0, 4, 7, 14]),
    ('add11', [0, 4, 7, 17]),
    ('4', [0, 4, 7, 17]),
    # 5 notes
    ('6/9', [0, 4, 7, 9, 14]),
    ('9', [0, 4, 7, 10, 14]),
    ('m9', [0, 3, 7, 10, 14]),
    ('M9', [0, 4, 7, 11, 14]),
    ('9sus4', [0, 5, 7, 10, 14]),
    ('7-9', [0, 4, 7, 10, 13]),
    ('7+9', [0, 4, 7, 10, 15]),
    ('11', [0, 7, 10, 14, 17]),
    ('7+11', [0, 4, 7, 10, 18]),
    ('7-13', [0, 4, 7, 10, 20]),
    # 6 notes
    ('13', [0, 4, 7, 10, 14, 21]),
))
