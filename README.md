# RGBmon

RGBmon is a system monitoring tool that lights up your components to indicate system status.

**Note:** This is really early stage. Expect the project and configuration to change a lot.
You should only use modes on devices that can handle frequent color updates. If the device supports such updates they are often refered to as *direct* mode.

## Dependencies

* Python >=3.7
* [OpenRGB](https://gitlab.com/CalcProgrammer1/OpenRGB)
* [openrgb-python](https://github.com/jath03/openrgb-python)

## Installation

* Install and set up [OpenRGB](https://gitlab.com/CalcProgrammer1/OpenRGB/-/blob/master/README.md)
* `pip install rgbmon`

## Usage

Firstly start the OpenRGB SDK server.

The script takes a the path to the config file as argument. There is an example directory which contains a `ram.json`. An example execution of `rgbmon` could look like:

`rgbmon --config=path/to/ram.json`
