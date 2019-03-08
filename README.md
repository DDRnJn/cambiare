# Cambiare - A lightweight music format conversion framework

I developed this to help write music in the format used by QMK, but decided to convert it into a framework so other music formats could be easily implemented. Currently only supports single-staff inputs. 

I'm planning this framework to mainly be used to convert common input formats into esoteric output formats. After QMK, the next output formats I'm planning to implement are Ocarina tabs.

The only input module included right now is for MusicXML files. The only output module included right now is for QMK.

New input plugins should implement the MusicImporter.py abstract class in the input_plugins directory. New output plugins should implement the MusicWriter abstract class in output_plugins.