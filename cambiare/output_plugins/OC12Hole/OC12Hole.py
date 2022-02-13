from cambiare.output_plugins.MusicWriter import MusicWriter
from cambiare.core import Song
from cambiare.output_plugins.OC12Hole.OC12HoleNote import OC12HoleNote
from datetime import datetime
from PIL import Image
from pathlib import Path
import math


class OC12Hole(MusicWriter):

    def __init__(self):
        self.max_row_length = 12
        self.max_width = 3840
        self.max_height = 2160
        self.resize_scale = 8
        self.current_image_width = 0
        self.current_image_height = 0

    def process_output(self, song: Song, filename):
        oc_output = []
        for cnote in song.notes:
            oc_image_path = OC12HoleNote(cnote.pitch)
            oc_output.append(oc_image_path)
        image_list = [self.resize_oc_image(Image.open(x.note_pitch_img_path.resolve())) for x in oc_output if x.note_pitch_img_path is not None]
        new_image = self.make_new_image(image_list)
        output_path = filename
        new_image.save(output_path)

    def resize_oc_image(self, img):
        new_width = int(img.size[0] / self.resize_scale)
        new_height = int(img.size[1] / self.resize_scale)
        new_image = img.resize((new_width, new_height))
        return new_image

    def resize_image(self, image):
        new_width = int(self.current_image_width / self.resize_scale)
        new_height = int(self.current_image_height / self.resize_scale)
        new_image = image.resize((new_width, new_height))
        return new_image

    def make_new_image(self, image_list):
        width = image_list[0].size[0]  # assumes all images have the same width
        height = image_list[0].size[1]  # assumes all images have the same height
        total_width = width * self.max_row_length
        total_height = height * math.ceil(len(image_list) / self.max_row_length)
        self.current_image_width = total_width
        self.current_image_height = total_height
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
