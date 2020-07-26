import threading

import core.backend
import core.source
import core.converter

from core.task import Task

def run(config):
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
