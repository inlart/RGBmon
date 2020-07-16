*************
Configuration
*************

The configuration in RGBmon is done in a `.json` file.

The top level entries are:

- **tasks**: A list of tasks
- **backends**: A list of backends

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

- **reference**: Name that is referenced in the tasks
- **name**: Backend name; currently only "openrgb" is available
- **settings**: An object containing the **ip_address** and the **port**

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

Tasks
#####

Content of a task entry:

- **interval**: Task execution interval
- **source**: Data that will get converted to color
- **converters**: Takes the output of a source and decides how LEDs should be colored

The example task that up:

.. code-block:: JSON

  {
      "interval": 0.5,
      "source" : {
        "name": "cpu"
      },
      "converters" : [
          {
              "name": "fill",
              "settings": {
                  "colors": [
                      "FF0000",
                      "00FF00"
                  ],
                  "leds": [
                      {
                          "type": 1,
                          "mode": "direct"
                      }
                  ]
              },
              "backend": "openrgbref"
          }
      ]
  }
