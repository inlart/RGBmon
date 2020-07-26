import logging
import argparse
import json
import sys

import core.rgbmon

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(fmt = " %(name)-16s :: %(levelname)-8s :: %(message)s")
handler.setFormatter(formatter)
root = logging.getLogger()
root.setLevel(logging.NOTSET)
root.addHandler(handler)

def get_arguments():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--config', dest='config', help='path to config file')
    return parser.parse_args()

def main():
    args = get_arguments()

    with open(args.config) as json_file:
        core.rgbmon.run(json.load(json_file))

if __name__ == "__main__":
    main()