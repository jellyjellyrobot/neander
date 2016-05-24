# Neander

![Neander](/Hardware/neander.jpg)

The Neander is a microcontroller platform that is created for NUS GreyHat's XCTF.

This board is based on the ESP8266 microcontroller series by Espressif and derives certain components from Adafruit's Feather and Sparkfun's Thing based on the same microcontroller platform.

## Specifications

- ESP8266 32 bit Microcontroller platform with Integrated 802.11 b/g/n
- Auto-Reset
- Deep Sleep option (enabled)
- 500mA 3.3V Voltage Regulator
- USB-Serial Interface (CP2102)
- 6 Buttons (including Reset)
- Lithium Polymer Charger
- Indicator LEDs (Charge, Power)
- Backlight LEDs and Switches

## Neander Accessory kit

The Neander comes with an accessory kit which includes the following

- Lithium Polymer Battery
- MicroUSB cable
- Short Lanyard (For CP2102)
- 10cm Dupont Jumper Cables (10 each: M-M, F-F, F-M)
- Single Row Headers 1*40 pin
- Double Row Headers 2*6 pin
- 6 Jumpers
- 2 Stickers

## Using the USB-Serial Adaptor

The on-board USB-Serial Adaptor is based on a Silabs CP2102 chip.

OS specific drivers can be found on the [manufacturer's website](http://www.silabs.com/products/mcu/Pages/USBtoUARTBridgeVCPDrivers.aspx). A tutorial on how to use this device can be found [here](https://learn.sparkfun.com/tutorials/cp2102-usb-to-serial-converter-hook-up-guide). The datasheet can be found [here](https://cdn.sparkfun.com/datasheets/BreakoutBoards/CP2102_v1.2.pdf).

## Interfacing with other electronics

The USB-Serial adaptor is supplied as a breakout board. If you need a serial adaptor "out in the field", you can choose to break it and solder on any 2.54mm compatible headers for convenience.

To interface the serial adaptor with other serial devices with the CP2102 in-situ, you may solder the double row headers found in the accessory packs and disconnect (desolder) all 5 SMD jumper pads.

## Contributors

Jacob
Darell
Yu Siang
Jeremias