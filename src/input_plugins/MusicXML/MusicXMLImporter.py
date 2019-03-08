from src.core.CNote import CNote
from src.core.NotePitch import NotePitch
from src.core.NoteType import NoteType
from music21 import converter
from music21.note import Note
from src.input_plugins.MusicImporter import MusicImporter
from src.core.Song import Song
from enum import Enum
import os

class MusicXMLImporter(MusicImporter):

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
            current_note_pitch = self.parse_note_pitch(str(note.pitch))
            current_note_type = self.parse_note_type(float(note.quarterLength))
            new_cnote = CNote(current_note_pitch, current_note_type)
            song.add_note(new_cnote)
        return song

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
            return "quarter"






