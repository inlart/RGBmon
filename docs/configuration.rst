*************
Configuration
*************

The configuration in RGBmon is done in a `.json` file.

The top level entries are:

- **tasks**: a list of tasks
- **backends**: a list of backends

.. code-block:: JSON

  {
      "tasks": [
      ],
      "backends": [
      ]
  }

Backends
########

There is currently only the openrgb backend available.
However, it might still make sense to have multiple backends in the configuration if you want to control LEDs on different PCs.

Content of a backend entry:

- **reference**: name that is referenced in the tasks
- **name**: backend name; currently only "openrgb" is available
- **settings**: an object containing the **ip_address** and the **port**

If the OpenRGB SDK server uses the default IP address (127.0.0.1) and port (6742) you may also omit the settings entry.

Example backend:

.. code-block:: JSON

  {
      "reference": "openrgbref",
      "name": "openrgb",
      "settings" : {
          "ip_address": "127.0.0.1",
          "port": 6742
      }
  }

LEDs
****

- **type**: the device type; see list of device types for available types
- **mode**: mode that is used to do per-LED color updates
- **devices** (optional): list of devices of the given type to be controlled; if devices isn't set it will use all devices of that type
    - **id**: the device id of the device to be used
    - **zones** (optional): list of zone ids to further restrict the device LEDs used

list of available device types:

+------------------------+
| device type            |
+========================+
| motherboard, mainboard |
+------------------------+
| ram                    |
+------------------------+
| gpu                    |
+------------------------+
| cooler                 |
+------------------------+
| ledstrip               |
+------------------------+
| keyboard               |
+------------------------+
| mouse                  |
+------------------------+
| mousemat               |
+------------------------+
| headset                |
+------------------------+
| headset_stand          |
+------------------------+

Example configuration to use a cooler with device id 0 and zone id 0:

.. code-block:: JSON

  {
      "type": "cooler",
      "mode": "fixed",
      "devices": [
          {
              "id": 0,
              "zones": [
                  0
              ]
          }
      ]
  }

Tasks
#####

Content of a task entry:

- **interval**: task execution interval
- **source**: data that will get converted to color
- **effects**: takes the output of a source and decides how LEDs should be colored

The example task that up:

.. code-block:: JSON

  {
      "interval": 0.5,
      "source" : {
        "name": "cpu"
      },
      "effects" : [
          {
              "name": "fill",
              "settings": {
                  "colors": [
                      "FF0000",
                      "00FF00"
                  ]
              },
              "backend": {
                  "name": "openrgbref",
                  "leds": [
                      {
                          "type": 1,
                          "mode": "direct"
                      }
                  ]
              }
          }
      ]
  }

Sources
#######

Generally a source json entry contains:

- **name**: name of the source
- **settings**: source dependent configuration


CPU
***

Outputs the cpu usage.
Configuration:

- **name**: "cpu"
- **settings**: none

Memory
******

Outputs the memory usage.
Configuration:

- **name**: "memory"
- **settings**: none

Temperature
***********

Outputs sensor temperature.
Configuration:

- **name**: "temperature"
- **settings**:
    - **driver**: sensor driver name (e.g. k10temp)
    - **label**: key name of the temperature entry in the sensor driver (e.g. Tdie)
    - **min** (optional, default=20): minimum temperature value, every temperature below will make the source output the same value as at min temperature
    - **max** (optional, default=100): maximum temperature value, every temperature above will make the source output the same value as at max temperature

This source is currently only available on Linux.

Sawtooth
********

Outputs a sawtooth signal with the given period.
Configuration:

- **name**: "sawtooth"
- **settings**:
    - **period**: period length of the signal in seconds

Sine
****

Outputs a sine signal with the given period.
Configuration:

- **name**: "sine"
- **settings**:
    - **period**: period length of the signal in seconds


Effects
#######

The effect configuration generally consists of these entries:

- **name**: the effect name
- **settings**: effect specific settings
- **backend**: effect independent thus won't be mentioned in the effect specific documentation
    - **name**: name of the backend reference specified in the backend list
    - **leds**: LEDs controlled by this effect; see the LEDs section in your used backend

All colors used in the effects json are strings in the format "RRGGBB".

Dot
***

Colors one LED differently.

- **name**: "dot"
- **settings**:
    - **colors**: array of two colors; first color is the default color; second color is the color of the dot

Fade
****

Fades between colors.

- **name**: "fade"
- **settings**:
    - **colors**: array of at least two colors; fades between the given colors

Fill
****

Fills the LEDs with a color.

- **name**: "fill"
- **settings**:
    - **colors**: array of two colors; first color is the default color; LED colors are converted to the second color as the source output increases

Rainbow
*******

A rainbow effect.

- **name**: "rainbow"
- **settings**: none

Static
******

Sets the LEDs to the colors. This effect ignores the value it receives from the source.

- **name**: "static"
- **settings**:
    - **colors**: array of colors. If there are more LEDs than colors, the colors get repeated.
