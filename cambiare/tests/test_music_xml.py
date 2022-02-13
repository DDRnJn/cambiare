from cambiare.core.NotePitch import NotePitch
from cambiare.core.NoteType import NoteType
from music21.note import Note
from cambiare.tests.fixtures import MXMLImporter


class TestMusicXML:

    def test_note_pitch_parser_natural(self, MXMLImporter):
        pitches = ["A1", "B3", "C7", "D4", "E2", "F5", "G5",
                   "A10", "G12"]
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[0])
        assert parsed_pitch == NotePitch.A1
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[1])
        assert parsed_pitch == NotePitch.B3
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[2])
        assert parsed_pitch == NotePitch.C7
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[3])
        assert parsed_pitch == NotePitch.D4
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[4])
        assert parsed_pitch == NotePitch.E2
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[5])
        assert parsed_pitch == NotePitch.F5
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[6])
        assert parsed_pitch == NotePitch.G5
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[7])
        assert parsed_pitch == NotePitch.REST
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[8])
        assert parsed_pitch != NotePitch.G7

    def test_note_pitch_parser_sharp(self, MXMLImporter):
        pitches = ["A#1", "B#3", "C#7", "D#4", "E#2", "F#5", "G#5",
                   "A#10", "G#12", "BS2"]
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[0])
        assert parsed_pitch == NotePitch.AS1
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[1])
        assert parsed_pitch == NotePitch.BS3
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[2])
        assert parsed_pitch == NotePitch.CS7
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[3])
        assert parsed_pitch == NotePitch.DS4
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[4])
        assert parsed_pitch == NotePitch.ES2
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[5])
        assert parsed_pitch == NotePitch.FS5
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[6])
        assert parsed_pitch == NotePitch.GS5
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[7])
        assert parsed_pitch == NotePitch.REST
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[8])
        assert parsed_pitch != NotePitch.GS7
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[9])
        assert parsed_pitch == NotePitch.BS2

    def test_note_pitch_parser_flat(self, MXMLImporter):
        pitches = ["A-1", "B-3", "C-7", "D-4", "E-2", "F-5", "G-5",
                   "A-10", "G-12", "F-3"]
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[0])
        assert parsed_pitch == NotePitch.AF1
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[1])
        assert parsed_pitch == NotePitch.BF3
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[2])
        assert parsed_pitch == NotePitch.CF7
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[3])
        assert parsed_pitch == NotePitch.DF4
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[4])
        assert parsed_pitch == NotePitch.EF2
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[5])
        assert parsed_pitch == NotePitch.FF5
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[6])
        assert parsed_pitch == NotePitch.GF5
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[7])
        assert parsed_pitch == NotePitch.REST
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[8])
        assert parsed_pitch != NotePitch.GF7
        parsed_pitch = MXMLImporter.parse_note_pitch(pitches[9])
        assert parsed_pitch == NotePitch.FF3

    def test_parse_music21_note(self, MXMLImporter):
        note = Note("A3")
        note.quarterLength = 4.0
        parsed_pitch = MXMLImporter.parse_note_pitch(str(note.pitch))
        parsed_type = MXMLImporter.parse_note_type(note.quarterLength)
        assert parsed_pitch == NotePitch.A3
        assert parsed_type == NoteType.whole

        note = Note("G#5")
        note.quarterLength = 1.5
        parsed_pitch = MXMLImporter.parse_note_pitch(str(note.pitch))
        parsed_type = MXMLImporter.parse_note_type(note.quarterLength)
        assert parsed_pitch == NotePitch.GS5
        assert parsed_type == NoteType.dotted_quarter

        note = Note("A#99")
        note.quarterLength = 83.1
        parsed_pitch = MXMLImporter.parse_note_pitch(str(note.pitch))
        parsed_type = MXMLImporter.parse_note_type(note.quarterLength)
        assert parsed_pitch == NotePitch.REST
        assert parsed_type == NoteType.quarter

    def test_parse_song(self, MXMLImporter):
        song = self.create_c_major_scale()
        song = MXMLImporter.parse_notes(song)
        assert song.notes[0].pitch == NotePitch.C4
        assert song.notes[0].note_type == NoteType.quarter
        assert song.notes[1].pitch == NotePitch.D4
        assert song.notes[1].note_type == NoteType.quarter

    def create_c_major_scale(self):
        song = []
        song.append(Note('C4', quarterLength=1.0))
        song.append(Note('D4', quarterLength=1.0))
        song.append(Note('E4', quarterLength=1.0))
        song.append(Note('F4', quarterLength=1.0))
        song.append(Note('G4', quarterLength=1.0))
        song.append(Note('A4', quarterLength=1.0))
        song.append(Note('B4', quarterLength=1.0))
        song.append(Note('C5', quarterLength=1.0))
        return song
