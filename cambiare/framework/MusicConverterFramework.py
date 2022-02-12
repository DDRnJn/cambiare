

class MusicConverterFramework:

    def __init__(self):
        self.input_plugin = None
        self.output_plugin = None
        self.input_file = None
        self.output_file = None
        self.song = None

    def add_input_plugin(self, input_plugin):
        self.input_plugin = input_plugin

    def add_output_plugin(self, output_plugin):
        self.output_plugin = output_plugin

    def process_file(self, filename):
        self.input_file = filename
        self.song = self.input_plugin.process_input(filename)

    def output_data(self, filename):
        self.output_file = filename
        self.output_plugin.process_output(self.song, self.output_file)
