from src.output_plugins.MusicWriter import MusicWriter
from src.core import Song
from .QmkNote import QmkNote
from datetime import datetime

class QMKMusicWriter(MusicWriter):

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
        output_str_notes = list(map(lambda x: x.parse_to_qmk_string(), qmk_note_list))
        qmk_str_list = ["#define {0}".format(filename)]
        qmk_str_list += output_str_notes
        return ", \\\n".join(qmk_str_list)