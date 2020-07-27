import logging
import time

from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType

logger = logging.getLogger(__name__)

device_type_mapping = {
    "motherboard": 0,
    "mainboard": 0,
    "ram": 1,
    "gpu": 2,
    "cooler": 3,
    "ledstrip": 4,
    "keyboard": 5,
    "mouse": 6,
    "mousemat": 7,
    "headset": 8,
    "headset_stand": 9
}

def get_device_type(device):
    device = device.lower()
    if device in device_type_mapping:
        return device_type_mapping[device]
    raise ValueError("Invalid device {}".format(device))

def create_device(id):
    ret = {}
    ret["id"] = id
    return ret

class Backend():
    def __init__(self, settings):
        ip = "127.0.0.1"
        port = 6742
        if settings:
            ip = settings.get("ip_address", ip)
            port = settings.get("port", port)
        logger.info("Using OpenRGB backend at {}:{}".format(ip, port))
        self.client = OpenRGBClient(ip, port)

    def get_led_list(self, config):
        led_config = config["leds"]
        led_list = []
        logger.debug("Retrieving led list from OpenRGB backend")
        for led_entry in led_config:
            device_type = get_device_type(led_entry["type"])
            devices = self.client.get_devices_by_type(DeviceType(device_type))

            device_list =  list(map(create_device, range(len(devices))))
            if "devices" in led_entry:
                device_list = led_entry["devices"]
            for device in device_list:
                # Get the device
                device_id = device["id"]
                orgb_device = devices[device_id]

                # Set the target mode
                orgb_device.set_mode(led_entry["mode"])

                # Check if it requires specific zones and add LEDs
                if "zones" in device:
                    for zone_id in device["zones"]:
                        led_list.extend(reversed(orgb_device.zones[zone_id].leds))
                else:
                    led_list.extend(reversed(orgb_device.leds))
        if not led_list:
            logger.warning("Could not find any LEDs for backend request.")
        return led_list


    def apply(self, leds_colors):
        for led, color in leds_colors:
            r, g, b = color
            led.set_color(RGBColor(r, g, b), fast=True)
