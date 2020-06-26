import importlib
import logging


log = logging.getLogger(__name__)

def load_converter(converter_config, backends):
    converter_name = converter_config["name"]

    module = importlib.import_module("converter." + converter_name)
    try:
        settings = converter_config["settings"] if "settings" in converter_config else None
        converter = getattr(module, "Converter")(settings, backends[converter_config["backend"]])
        log.info("Converter {} loaded successfully.".format(converter_name))
        return converter
    except Exception as e:
        log.error("Loading converter {} failed: {}".format(converter_name, e))

    return None
