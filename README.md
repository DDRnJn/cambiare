# Cambiare - A lightweight music format conversion framework

I developed this to help write music in the format used by QMK, but decided to convert it into a framework so other music formats could be easily implemented. Currently only supports single-staff inputs. 

### Input Plugins

Currently, the only input plugin is a MusicXML Importer. It uses the music21 library to parse input MusicXML files and retrieve the song's note list, after which each note is converted into the common CNote format used by the framework. Since the framework is meant to be used with single staff inputs, all chords in the input MusicXML file are replaced with the highest pitched note in the chord.

### Output Plugins

#### QMK

QMK is a popular open source firmware used with a wide range of different keyboards  [Link](https://github.com/qmk/qmk_firmware)

Some mechanical keyboards, like the Planck and Preonic, have built in speakers that can be used to play play music. Writing this music can be cumbersome, especially for longer songs, so I wrote an output plugin to facilitate converting MusicXML to a format that matches the format used in QMK.

Here's an example input

![](https://codeandchord-media.s3.amazonaws.com/blog_files/2019/03/19/0e4035fe-72e4-4909-ae0c-809def500a18.PNG)

Here's an example QMK output

![](https://codeandchord-media.s3.amazonaws.com/blog_files/2019/03/19/bb985804-ec77-478a-9248-e71a35d76d32.PNG)
 
#### Ocarina Tabs

The Ocarina is a small, easy to play wind instrument. A lot of ocarina players do not necessarily have a background in music and sometimes find reading sheet music difficult. Ocarina tabs are a popular visual solution allowing people who can't read sheet music to still be able to read and play notes on the ocarina.

The Ocarina output plugin accepts input songs from the main framework and outputs an image representing the visual tab of the song. It will also automatically "round" an input note to the closest octave if a note outside the range of the target ocarina is processed.

Here's an example input:

![](https://codeandchord-media.s3.amazonaws.com/blog_files/2019/03/03/a14acc9a-eb18-4d22-aae6-40b27412b0d2.PNG)

Here's an example Ocarina Tab output:

![](https://codeandchord-media.s3.amazonaws.com/blog_files/2019/03/03/ea034ac9-aa0e-45cb-b7c7-744c3d541096.png)

The ocarina output plugin only supports a standard A4-F6 12 hole ocarina right now. I am planning on adding support for double and triple chambered ocarinas as well.




New input plugins should implement the MusicImporter.py abstract class in the input_plugins directory. New output plugins should implement the MusicWriter abstract class in output_plugins.