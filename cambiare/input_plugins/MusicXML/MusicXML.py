from core.CNote import CNote
from core.NotePitch import NotePitch
from core.NoteType import NoteType
from music21 import converter
from music21.note import Note
from input_plugins.MusicImporter import MusicImporter
from core.Song import Song
from enum import Enum
from music21.chord import Chord
import os


class MusicXML(MusicImporter):

    def __init__(self):
        self.music = None
        self.note_type_map = {
            4.0: NoteType.whole,  # Whole Note
            2.0: NoteType.half,  # Half Note
            1.0: NoteType.quarter,  # Quarter Note
            0.5: NoteType.eighth,  # Eighth Note
            0.25: NoteType.sixteenth,  # Sixteenth Note
            0.125: NoteType.thirtysecond, #thirtysecond
            6.0: NoteType.dotted_whole,  # Dotted Whole Note
            3.0: NoteType.dotted_half,  # Dotted Half Note
            1.5: NoteType.dotted_quarter,  # Dotted Quarter Note
            0.75: NoteType.dotted_eighth,  # Dotted Eighth Note
            0.375: NoteType.dotted_sixteenth,  # Dotted Sixteenth Note
            0.1875: NoteType.dotted_thirtysecond # Dotted Thirtysecond Note
        }

    def process_input(self, filename) -> Song:
        music = converter.parse(filename)
        notes = music.flat.notes
        song = self.parse_notes(notes)
        return song

    def parse_notes(self, notes):
        song = Song()
        for note in notes:
            if note.isChord:
                current_note = self.convert_chord_to_note(note)
            else:
                current_note = note
            current_note_pitch = self.parse_note_pitch(str(current_note.pitch))
            current_note_type = self.parse_note_type(float(current_note.quarterLength))
            new_cnote = CNote(current_note_pitch, current_note_type)
            song.add_note(new_cnote)
        return song

    #  Converts a chord to the highest pitched note in the chord
    def convert_chord_to_note(self, chord):
        note = chord[-1]
        note.quarterLength = chord.duration.quarterLength
        return note

    def parse_note_pitch(self, pitch):
        pitch = pitch.replace("#", "S")
        pitch = pitch.replace("-", "F")
        if pitch in NotePitch.__members__:
            return NotePitch[pitch]
        else:
            return NotePitch.REST

    def parse_note_type(self, note_type):
        if note_type in self.note_type_map:
            return self.note_type_map[note_type]
        else:
            return self.note_type_map[1.0]






