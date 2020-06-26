import importlib
import logging


log = logging.getLogger(__name__)

def load_source(source_config):
    source_name = source_config["name"]

    module = importlib.import_module("source." + source_name)
    try:
        settings = source_config["settings"] if "settings" in source_config else None
        source = getattr(module, "Source")(settings)
        log.info("Source {} loaded successfully.".format(source_name))
        return source
    except Exception as e:
        log.error("Loading source {} failed: {}".format(source_name, e))

    return None
