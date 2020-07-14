# RGBmon

[![PyPI Status](https://badge.fury.io/py/rgbmon.svg)](https://badge.fury.io/py/rgbmon)
[![Documentation Status](https://readthedocs.org/projects/rgbmon/badge/?version=latest)](https://rgbmon.readthedocs.io/en/latest/?badge=latest)

RGBmon is a system monitoring tool that lights up your components to indicate system status.

**Note:**
Only use modes on devices that can handle frequent color updates. If the device supports such updates they are often refered to as *direct* mode.

## Installation

* Install and set up [OpenRGB](https://gitlab.com/CalcProgrammer1/OpenRGB/-/blob/master/README.md)
* `pip install --user rgbmon`

## Usage

* Start the OpenRGB SDK server
* Run RGBmon `rgbmon --config=path/to/config.json`

RGBmon always needs a path to a valid configuration in the json format.
The project provides sample configurations in the `examples/` directory which you can try.
If you want to create your own configuration file please have a look at the [documentation](https://rgbmon.readthedocs.io/en/latest/).

## Dependencies

* Python >=3.7
* [OpenRGB](https://gitlab.com/CalcProgrammer1/OpenRGB)
* [openrgb-python](https://github.com/jath03/openrgb-python)
