from pytest import fixture
from cambiare.input_plugins.MusicXML.MusicXML import MusicXML


@fixture()
def MXMLImporter():
    music_xml_plugin = MusicXML()
    return music_xml_plugin
