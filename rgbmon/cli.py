import logging
import argparse
import json
import sys

import core.rgbmon

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(fmt=" %(name)-16s :: %(levelname)-8s :: %(message)s")
handler.setFormatter(formatter)
root = logging.getLogger()
root.addHandler(handler)


def getArguments():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--config', dest='config', help='path to config file')
    parser.add_argument('-v', '--verbose', dest='verbose', action='count', help='log verbosity')
    parser.add_argument('--logfile', dest='logfile', help='log file')
    return parser.parse_args()


def setLogLevel(verbose):
    global root
    if not verbose:
        root.setLevel(logging.ERROR)
    elif verbose == 1:
        root.setLevel(logging.WARNING)
    elif verbose == 2:
        root.setLevel(logging.INFO)
    elif verbose >= 3:
        root.setLevel(logging.DEBUG)


def setLogOutput(logfile):
    global root
    if logfile:
        handler = logging.FileHandler(logfile)
        formatter = logging.Formatter(fmt=" %(name)-16s :: %(levelname)-8s :: %(message)s")
        handler.setFormatter(formatter)
        root.addHandler(handler)


def main():
    args = getArguments()

    setLogLevel(args.verbose)
    setLogOutput(args.logfile)

    with open(args.config) as json_file:
        core.rgbmon.run(json.load(json_file))


if __name__ == "__main__":
    main()
