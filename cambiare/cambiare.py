import argparse
import framework.MusicConverterFramework as mcf
import os


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
    input_module = __import__(f"input_plugins.{input_plugin}.{input_plugin}",
                              fromlist=f"input_plugins.{input_plugin}")
    output_module = __import__(f"output_plugins.{output_plugin}.{output_plugin}",
                              fromlist=f"output_plugins.{output_plugin}")
    input_class = getattr(input_module, input_plugin)
    output_class = getattr(output_module, output_plugin)
    input_instance = input_class()
    output_instance = output_class()
    framework.add_input_plugin(input_instance)
    framework.add_output_plugin(output_instance)
    framework.process_file(input_path)
    framework.output_data(output_path)


if __name__ == "__main__":
    main()
