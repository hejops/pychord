#!/usr/bin/env python3
# An example to create MIDI file with PyChord and pretty_midi
# Prerequisite: pip install pretty_midi
# pretty_midi: https://github.com/craffel/pretty-midi


import pretty_midi

from pychord import Chord
from pychord import ChordProgression
from midi2audio import FluidSynth

def create_midi(chords, scale=None):
    midi_data = pretty_midi.PrettyMIDI()
    piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
    piano = pretty_midi.Instrument(program=piano_program)
    length = 1
    for n, chord in enumerate(chords):
        for note_name in chord.components_with_pitch(root_pitch=4):
            note_number = pretty_midi.note_name_to_number(note_name)
            note = pretty_midi.Note(velocity=100, pitch=note_number, start=n * length, end=(n + 1) * length)
            piano.notes.append(note)
    midi_data.instruments.append(piano)

    midi = 'chord.mid'
    midi_data.write(midi)
    msg = f"Playing chords: {chords}"
    if scale:
        msg += f" (scale: {scale})"
    print(msg)
    FluidSynth().play_midi(midi)

def main():
    chords_str = ["C", "Dm7", "G", "C"]
    chords = [Chord(c) for c in chords_str]
    create_midi(chords)

    for i in range(3):
        cp, scale = ChordProgression().make_chord_progression()
        create_midi(cp, scale)

if __name__ == '__main__':
    main()
