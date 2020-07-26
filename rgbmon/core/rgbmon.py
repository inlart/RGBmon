import threading

import core.backend
import core.source
import core.effect

from core.task import Task

def run(config):
    # load backends
    backends = core.backend.load_backends(config["backends"])

    for task in config["tasks"]:
        # load task effects
        effects = []
        for effect_config in task["effects"]:
            effect = core.effect.load_effect(effect_config, backends)
            effects.append(effect)

        # load the source
        source = core.source.load_source(task["source"])

        # create a new thread for the task
        task = Task(task["interval"], source, effects)
        t = threading.Thread(target=task.run)
        t.start()
