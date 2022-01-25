import argparse
import framework.MusicConverterFramework as mcf


def main():
    parser = argparse.ArgumentParser(prog="cambiare",
                                     description="A lightweight single staff music format conversion program")
    parser.add_argument("-i", help="input file path", type=str, required=True)
    parser.add_argument("-o", help="output file path", type=str, required=True)
    parser.add_argument("-iplug", help="input plugin", type=str, required=True)
    parser.add_argument("-oplug", help="output plugin", type=str, required=True)
    args = vars(parser.parse_args())
    input_path = args['i']
    output_path = args['o']
    input_plugin = args['iplug']
    output_plugin = args['oplug']
    framework = mcf.MusicConverterFramework()
    input_module = __import__(f"cambiare.input_plugins.{input_plugin}.{input_plugin}",
                              fromlist=f"cambiare.input_plugins.{input_plugin}")
    output_module = __import__(f"cambiare.output_plugins.{output_plugin}.{output_plugin}",
                              fromlist=f"cambiare.input_plugins.{output_plugin}")



if __name__ == "__main__":
    main()
