from core.colormanager import ColorManager

class Effect:
    def __init__(self, config, backend, backend_config):
        self.backend = backend
        self.leds = backend.get_led_list(backend_config)
        self.colors = ColorManager(config["colors"])

    def convert(self, value):
        out = []
        for i in range(len(self.leds)):
            out.append((self.leds[i], self.colors[0]))
        return out
