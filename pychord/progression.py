# -*- coding: utf-8 -*-

from .chord import as_chord, Chord
from .constants.scales import RELATIVE_KEY_DICT, NOTE_VAL_DICT


class ChordProgression(object):
    """ Class to handle chord progressions.

    :param list[pychord.Chord] _chords: component chords of chord progression.
    """

    def __init__(self, initial_chords=None):
        """ Constructor of ChordProgression instance.

        :type initial_chords: str|pychord.Chord|list
        :param initial_chords: Initial chord or chords of the chord progressions
        """
        if initial_chords is None:
            initial_chords = []
        if isinstance(initial_chords, Chord):
            self._chords = [initial_chords]
        elif isinstance(initial_chords, str):
            self._chords = [as_chord(initial_chords)]
        elif isinstance(initial_chords, list):
            self._chords = [as_chord(chord) for chord in initial_chords]
        else:
            raise TypeError("Cannot initialize ChordProgression with argument of {} type".format(type(initial_chords)))

    def __unicode__(self):
        return " | ".join([chord.chord for chord in self._chords])

    def __str__(self):
        return " | ".join([chord.chord for chord in self._chords])

    def __repr__(self):
        return "<ChordProgression: {}>".format(" | ".join([chord.chord for chord in self._chords]))

    def __add__(self, other):
        self._chords += other.chords
        return self

    def __len__(self):
        return len(self._chords)

    def __getitem__(self, item):
        return self._chords[item]

    def __setitem__(self, key, value):
        self._chords[key] = value

    def __eq__(self, other):
        if not isinstance(other, ChordProgression):
            raise TypeError("Cannot compare ChordProgression object with {} object".format(type(other)))
        if len(self) != len(other):
            return False
        for c, o in zip(self, other):
            if c != o:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def chords(self):
        """ Get component chords of chord progression

        :rtype: list[pychord.Chord]
        """
        return self._chords

    def append(self, chord):
        """ Append a chord to chord progressions

        :type chord: str|pychord.Chord
        :param chord: A chord to append
        :return:
        """
        self._chords.append(as_chord(chord))

    def insert(self, index, chord):
        """ Insert a chord to chord progressions

        :param int index: Index to insert a chord
        :type chord: str|pychord.Chord
        :param chord: A chord to insert
        :return:
        """
        self._chords.insert(index, as_chord(chord))

    def pop(self, index=-1):
        """ Pop a chord from chord progressions

        :param int index: Index of the chord to pop (default: -1)
        :return: pychord.Chord
        """
        return self._chords.pop(index)

    def transpose(self, trans):
        """ Transpose whole chord progressions

        :param int trans: Transpose key
        :return:
        """
        for chord in self._chords:
            chord.transpose(trans)

    def make_chord_progression(self) -> tuple[list[Chord], str]:

        import random

        root = random.choice(list(NOTE_VAL_DICT)) 
        mode = random.choice(list(RELATIVE_KEY_DICT)) 
        scale = root + mode

        FUNCTIONS = {
            "tonic": 1,
            "predominant": [2, 3, 6],
            "dominant": [4, 5, 7],
        }

        p = random.choice(list(FUNCTIONS["predominant"]))
        d = random.choice(list(FUNCTIONS["dominant"]))

        T1 = Chord.from_note_index(note=1, quality=random.choice(["", "7"]), scale=scale, diatonic=True)
        P = Chord.from_note_index(note=p, quality=random.choice(["", "7"]), scale=scale, diatonic=True)
        D = Chord.from_note_index(note=d, quality=random.choice(["", "7"]), scale=scale, diatonic=True)
        T2 = Chord.from_note_index(note=1, quality=random.choice(["", "7"]), scale=scale, diatonic=True)

        progression = [T1, P, D, T2]
        return progression, scale
