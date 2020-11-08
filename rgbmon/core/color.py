import importlib
import logging


log = logging.getLogger(__name__)

def load_color(color_config):
    if not isinstance(color_config, dict):
        logging.debug("Loading static color {} without color object".format(color_config))
        color_config = {
            "name": "static",
            "settings": {
                "value": color_config
            }
        }

    color_name = color_config["name"]

    module = importlib.import_module("color." + color_name)
    try:
        color = getattr(module, "Color")(color_config["settings"])
        log.info("Color {} loaded successfully.".format(color_name))
        return color
    except Exception as e:
        log.error("Loading color {} failed: {}".format(color_name, e))

    return None
