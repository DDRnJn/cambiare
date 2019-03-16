from src.output_plugins.MusicWriter import MusicWriter
from src.core import Song
from .OC12HoleNote import OC12HoleNote
from datetime import datetime
from PIL import Image
from pathlib import Path
import math


class OC12HoleMusicWriter(MusicWriter):

    def __init__(self):
        self.output_folder = Path("../output")
        self.max_row_length = 12
        self.max_width = 3840
        self.max_height = 2160

    def process_output(self, song: Song, filename):
        oc_output = []
        for cnote in song.notes:
            oc_image_path = OC12HoleNote(cnote.pitch)
            oc_output.append(oc_image_path)
        out_filename = filename.stem.upper()
        out_timestamp = str(datetime.timestamp(datetime.now())).split(".")[0]
        out_filename_full = "{0}{1}.png".format(out_filename, out_timestamp)
        image_list = [Image.open(x.note_pitch_img_path.resolve()) for x in oc_output]
        new_image = self.make_new_image(image_list)
        new_image = self.resize_image(new_image)
        output_path = self.output_folder / out_filename_full
        new_image.save(output_path)

    def resize_image(self, image):
        new_image = image.resize((self.max_width, self.max_height))
        return new_image

    def make_new_image_old(self, image_list):
        width = image_list[0].size[0]  # assumes all images have the same width
        height = image_list[0].size[1]  # assumes all images have the same height
        total_width = width * len(image_list)
        #  image_size = (image_list[0].size[0] * len(image_list), image_list[0].size[0])
        background_color = (255, 255, 255)
        output_image = Image.new("RGB", (total_width, height), background_color)
        for i, image in enumerate(image_list):
            current_width = width * i
            current_height = height * 0
            output_image.paste(image, (current_width, current_height))
        return output_image

    def make_new_image(self, image_list):
        width = image_list[0].size[0]  # assumes all images have the same width
        height = image_list[0].size[1]  # assumes all images have the same height
        total_width = width * self.max_row_length
        total_height = height * math.ceil(len(image_list) / self.max_row_length)
        background_color = (255, 255, 255) # set background color to white
        output_image = Image.new("RGB", (total_width, total_height), background_color)
        img_num = 0
        for i in range(len(image_list)):
            for j in range(self.max_row_length):
                if (j+img_num) >= len(image_list):
                    break
                image = image_list[j+img_num]
                current_width = width * j
                current_height = height * i
                output_image.paste(image, (current_width, current_height))
            img_num += self.max_row_length
        return output_image
