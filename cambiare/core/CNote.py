from cambiare.core.NotePitch import NotePitch
from cambiare.core.NoteType import NoteType


class CNote:

    def __init__(self, note_pitch: NotePitch, note_type: NoteType):
        self.pitch = note_pitch
        self.note_type = note_type
