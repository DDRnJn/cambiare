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

        #  Added because the default tempo in QMK is 100, which is way too fast
        #  So this dict instead maps to double the actual note value
        #  Except for whole notes, since there's no double whole/breve type in QMK
        #  Maybe I'll add that later
        self.qmk_duration_mapping_slow = {
            NoteType.whole: "B__NOTE",  # Whole Note
            NoteType.half: "W__NOTE",  # Half Note
            NoteType.quarter: "H__NOTE",  # Quarter Note
            NoteType.eighth: "Q__NOTE",  # Eighth Note
            NoteType.sixteenth: "E__NOTE",  # Sixteenth Note
            NoteType.dotted_whole: "BD_NOTE",  # Dotted Whole Note
            NoteType.dotted_half: "WD_NOTE",  # Dotted Half Note
            NoteType.dotted_quarter: "HD_NOTE",  # Dotted Quarter Note
            NoteType.dotted_eighth: "QD_NOTE",  # Dotted Eighth Note
            NoteType.dotted_sixteenth: "ED_NOTE",  # Dotted Sixteenth Note
        }

        self.note_type = self.parse_note_type(note_type)
        self.note_pitch = self.parse_note_pitch(note_pitch)
        #self.qmk_string = self.parse_to_qmk_string(music21_note)

    def parse_note_type(self, note_type):
        if note_type in self.qmk_duration_mapping_slow:
            return self.qmk_duration_mapping_slow[note_type]
        else:
            return NoteType.quarter

    def parse_note_pitch(self, note_pitch):
        return "_{0}".format(str(note_pitch.name))

    def parse_to_qmk_string(self):
        return "{0}({1})".format(self.note_type, self.note_pitch)
