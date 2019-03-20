from .OCNotePitch import OCNotePitch
from pathlib import Path


class OC12HoleNote:

    def __init__(self, note_pitch):
        self.base_path = Path(__file__).parent
        self.image_folder_path = (self.base_path / "images").resolve()
        self.min_pitch = 4
        self.max_pitch = 6
        self.note_pitch_img_map = self.get_note_pitch_img_map()
        self.note_pitch_img_path = self.get_note_pitch_img(note_pitch)
        print(self.note_pitch_img_path)

    def get_note_pitch_img_map(self):
        note_pitch_img_map = {}
        for item in OCNotePitch:
            note_pitch_img_map[item.name] = item.name
        return note_pitch_img_map

    def get_note_pitch_img(self, note_pitch):
        img_path = None
        if note_pitch.name in self.note_pitch_img_map:
            img_path = self.image_folder_path / "{0}.png".format(note_pitch.name)
        else:
            note_pitch_octave = self.get_closest_note_pitch(note_pitch)
            if note_pitch_octave:
                img_path = self.image_folder_path / "{0}.png".format(note_pitch_octave)
        return img_path

    def get_closest_note_pitch(self, note_pitch):
        if note_pitch.name == "REST":
            return None
        octave = int(note_pitch.name[-1])
        pitch = note_pitch.name[:-1]
        if octave <= self.min_pitch:
            for pitch_octave in range(self.min_pitch, self.max_pitch+1, 1):
                new_note = "{0}{1}".format(pitch, pitch_octave)
                if new_note in self.note_pitch_img_map:
                    return "{0}{1}".format(pitch, pitch_octave)
        elif octave >= self.max_pitch:
            for pitch_octave in range(self.max_pitch, self.min_pitch-1, -1):
                new_note = "{0}{1}".format(pitch, pitch_octave)
                if new_note in self.note_pitch_img_map:
                    return "{0}{1}".format(pitch, pitch_octave)
        return None
