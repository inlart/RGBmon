import argparse
import json
import logging
import sys
import threading

import core.backend
import core.source
import core.converter

from core.task import Task

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
        config = json.load(json_file)

        # load backends
        backends = core.backend.load_backends(config["backends"])

        for task in config["tasks"]:
            # load task converters
            converters = []
            for converter_config in task["converters"]:
                converter = core.converter.load_converter(converter_config, backends)
                converters.append(converter)

            # load the source
            source = core.source.load_source(task["source"])

            # create a new thread for the task
            task = Task(task["interval"], source, converters)
            t = threading.Thread(target=task.run)
            t.start()

if __name__ == "__main__":
    main()
