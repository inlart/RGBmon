import importlib
import logging


log = logging.getLogger(__name__)


def load_color(color_config):
    if not isinstance(color_config, dict):
        log.debug("Loading static color {} without color object".format(color_config))
        color_config = {
            "name": "static",
            "settings": {
                "value": color_config
            }
        }

    color_name = color_config["name"]

    module = importlib.import_module("color." + color_name)
    try:
        settings = color_config["settings"] if "settings" in color_config else None
        color = getattr(module, "Color")(settings)
        log.info("Color {} loaded successfully.".format(color_name))
        return color
    except Exception as e:
        log.error("Loading color {} failed: {}".format(color_name, e))

    return None
