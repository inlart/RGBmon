import logging
import argparse
import json
import sys

import core.rgbmon

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(fmt = " %(name)-16s :: %(levelname)-8s :: %(message)s")
handler.setFormatter(formatter)
root = logging.getLogger()
root.addHandler(handler)

def get_arguments():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--config', dest='config', help='path to config file')
    parser.add_argument('-v', '--verbose', dest='verbose', action='count', help='log verbosity')
    return parser.parse_args()

def setloglevel(verbose):
    global root
    if not verbose:
        root.setLevel(logging.ERROR)
    elif verbose == 1:
        root.setLevel(logging.WARNING)
    elif verbose == 2:
        root.setLevel(logging.INFO)
    elif verbose >= 3:
        root.setLevel(logging.DEBUG)

def main():
    args = get_arguments()

    setloglevel(args.verbose)

    with open(args.config) as json_file:
        core.rgbmon.run(json.load(json_file))

if __name__ == "__main__":
    main()