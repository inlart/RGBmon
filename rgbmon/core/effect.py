import importlib
import logging


log = logging.getLogger(__name__)

def load_effect(effect_config, backends):
    effect_name = effect_config["name"]

    module = importlib.import_module("effect." + effect_name)
    try:
        settings = effect_config["settings"] if "settings" in effect_config else None
        backend = backends[effect_config["backend"]["name"]]
        effect = getattr(module, "Effect")(settings, backend, effect_config["backend"])
        log.info("Effect {} loaded successfully.".format(effect_name))
        return effect
    except Exception as e:
        log.error("Loading effect {} failed: {}".format(effect_name, e))

    return None
