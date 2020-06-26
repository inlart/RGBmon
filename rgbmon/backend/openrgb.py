import logging
import time

from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType

logger = logging.getLogger(__name__)

class Backend():
    def __init__(self, settings):
        ip = settings["ip_address"]
        port = settings["port"]
        logger.info("Using OpenRGB backend at {}:{}".format(ip, port))
        self.client = OpenRGBClient(ip, port)

    def get_led_list(self, led_config):
        led_list = []
        logger.debug("Retrieving led list from OpenRGB backend")
        for led_entry in led_config:
            devices = self.client.get_devices_by_type(DeviceType(led_entry["type"]))

            for device_id in led_entry["device_ids"]:
                device = devices[device_id]
                device.set_mode(led_entry["mode"])
                led_list.extend(reversed(device.leds))
        return led_list


    def apply(self, leds_colors):
        for led, color in leds_colors:
            led.set_color(RGBColor(color.r, color.g, color.b))
