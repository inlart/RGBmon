import importlib
import logging


log = logging.getLogger(__name__)

def load_backends(backends_config):
    backends = {}
    for backend_config in backends_config:
        backend_name = backend_config["name"]
        backend_ref = backend_config["reference"]
        if backend_ref in backends:
            log.error("Backend with reference name {} already exists.".format(backend_name))
            continue
        module = importlib.import_module("backend." + backend_name)
        try:
            backend = getattr(module, "Backend")(backend_config["settings"])
            backends[backend_ref] = backend
            log.info("Backend {} loaded successfully.".format(backend_name))
        except Exception as e:
            log.error("Loading backend {} failed: {}".format(backend_name, e))
    return backends
