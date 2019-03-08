from .NotePitch import NotePitch
from .NoteType import NoteType


class CNote:

    def __init__(self, note_pitch: NotePitch, note_type: NoteType):
        self.pitch = note_pitch
        self.note_type = note_type
