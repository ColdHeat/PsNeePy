# PsNeePy
A Playstation 1 Modchip written in Python

The main code is derived partially from different versions of [PSNee](https://github.com/kalymos/PsNee).

## Install

1. To begin you need to install MicroPython onto an [ESP8266](https://amzn.to/2K4HdTq) by following the [MicroPython documentation](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html).

2. Setup the MicroPython WebREPL using the [instructions](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/repl.html#webrepl-a-prompt-over-wifi).

3. PsNeePy uses three pins to communicate to the PS1. It can be tricky to identify where to solder to but I've simplified it by mapping GPIO pins to MM3 pins.

    | GPIO        | MM3 Chip  |
    | ----------- | --------- |
    | GPIO14 (D5) | Pin 6     |
    | GPIO12 (D6) | Pin 5     |
    | GPIO13 (D7) | Pin 7     |
    | 3.3V        | Pin 1     |
    | GND         | Pin 8     |

    For power you merely need to provide GND and 3.3V which are marked in the diagram below.

    ![NodeMCU pinouts](https://raw.githubusercontent.com/wiki/ColdHeat/PsNeePy/images/nodemcu.png)

4. Solder the corresponding pins to the right pads on the PSX PCB.

    In my PS1 I soldered [stranded wire](https://amzn.to/2IaBHcL) onto [jumpers into a breadboard](https://amzn.to/2llKUG7).

    To reduce the amount of soldering I do and also make it easier to take apart later, I then use [more jumpers](https://amzn.to/2lloqoE) to connect to the NodeMCU.

5. Connect to the NodeMCU via WiFi and use the [WebREPL](http://micropython.org/webrepl/) to connect.

    The SSID will be `MicroPython-xxxxxx` where the x's are part of the NodeMCU's MAC address. The password is `micropythoN`.

6. Upload `main.py` through the "Send a file" interface.

7. Reboot the PS1. While the PS1 is on, the `MicroPython-xxxxxx` SSID should be available and you should be able to connect to it and update the modchip.

    **Note:** You can connect the NodeMCU to your network so that you do not need to connect to the `MicroPython-xxxxxx` network but I've never done it.