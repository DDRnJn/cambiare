from src.output_plugins.MusicWriter import MusicWriter
from src.core import Song
from .QmkNote import QmkNote
from datetime import datetime

class QMKMusicWriter(MusicWriter):

    def __init__(self):
        self.max_row_length = 8

    def process_output(self, song: Song, filename):
        qmk_output = []
        for cnote in song.notes:
            qmk_note = QmkNote(cnote.pitch, cnote.note_type)
            qmk_output.append(qmk_note)
        out_filename = filename.stem.upper()
        output_string = self.parse_to_qmk_string(qmk_output, out_filename)
        out_timestamp = str(datetime.timestamp(datetime.now())).split(".")[0]
        output_file = open("../output/{0}_out_{1}.txt".format(out_filename, out_timestamp), 'w')
        output_file.write(output_string)
        output_file.close()

    def parse_to_qmk_string(self, qmk_note_list, filename):
        output_str_notes = list(map(lambda x: "{0}".format(x.parse_to_qmk_string()), qmk_note_list))
        qmk_head_str = "#define {0} \\\n".format(filename)
        output_str_list = []
        for i in range(len(output_str_notes)):
            if i % self.max_row_length == 0 and i != 0:
                out_str = "{0}, \\\n  ".format(output_str_notes[i])
            else:
                out_str = "{0}, ".format(output_str_notes[i])
            output_str_list.append(out_str)
        output_str = "{0}  {1}".format(qmk_head_str, "".join(output_str_list))
        return output_str
