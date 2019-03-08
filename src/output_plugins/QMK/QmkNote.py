from src.core.NoteType import NoteType
from src.core.NotePitch import NotePitch

class QmkNote:

    def __init__(self, note_pitch, note_type):
        # Dictionary mapping cambiare note types to QMK note types
        self.qmk_duration_mapping = {
            NoteType.whole: "W__NOTE",  # Whole Note
            NoteType.half: "H__NOTE",  # Half Note
            NoteType.quarter: "Q__NOTE",  # Quarter Note
            NoteType.eighth: "E__NOTE",  # Eighth Note
            NoteType.sixteenth: "S__NOTE",  # Sixteenth Note
            NoteType.dotted_whole: "WD_NOTE",  # Dotted Whole Note
            NoteType.dotted_half: "HD_NOTE",  # Dotted Half Note
            NoteType.dotted_quarter: "QD_NOTE",  # Dotted Quarter Note
            NoteType.dotted_eighth: "ED_NOTE",  # Dotted Eighth Note
            NoteType.dotted_sixteenth: "SD_NOTE",  # Dotted Sixteenth Note
        }

        self.note_type = self.parse_note_type(note_type)
        self.note_pitch = self.parse_note_pitch(note_pitch)
        #self.qmk_string = self.parse_to_qmk_string(music21_note)

    def parse_note_type(self, note_type):
        if note_type in self.qmk_duration_mapping:
            return self.qmk_duration_mapping[note_type]
        else:
            return NoteType.quarter

    def parse_note_pitch(self, note_pitch):
        return "_{0}".format(str(note_pitch.name))

    def parse_to_qmk_string(self):
        return "{0}({1})".format(self.note_type, self.note_pitch)
