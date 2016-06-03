#/bin/python

from escpos import *

ep = printer.Serial("/dev/ttyUSB0", 38400)

ep.set(align="CENTER", bold=True , size='normal')

ep.text("Welcome to\n")

ep.set(align="CENTER", bold=True , size='2x')

ep.text("X-CTF\n")

ep.set(align="CENTER", bold=True , size='2h')

ep.text("\n\nGetting Started\n\n")

ep.set(align="LEFT", bold=False , size='normal')

ep.text("The Neander is a microcontroller platform that is created for NUS Greyhats' X-CTF.\n\n")
ep.text("This board is based on the ESP8266 microcontroller series by Espressif and derives certain")
ep.text(" components from Adafruit's Feather and Sparkfun's Thing based on the same microcontroller platform.\n\n")

ep.text("For more information, visit ")
ep.text("https://github.com/nushackers/neander\n")

ep.set(align="CENTER")
ep.text("\n")

ep.qr("https://github.com/nushackers/neander")

ep.text("\n")
ep.set(align="CENTER", bold=True , size='2h')

ep.text("Safety Precautions\n\n")

ep.set(align="LEFT", bold=False , size='normal')

ep.text("This board is fitted with a Lithium Polymer battery fitted with limited protection circuitry.\n\n")
ep.text("In order to ensure operational safety, please refrain from overexerting force on the battery")
ep.text(" connector and wires. Whenever non-operational, the battery should be disconnected from the")
ep.text(" board to prevent undervoltage failures.\n\n")

ep.set(align="CENTER", bold=True , size='2h')

ep.text("LCD Contrast\n\n")

ep.set(align="LEFT", bold=False , size='normal')

ep.text("The contrast of the liquid crystal display is dependent on the ambient temperature.")
ep.text(" Please adjust the contrast accordingly.\n\n")

ep.set(align="CENTER", bold=True , size='2h')

ep.text("USB-Serial Adaptor\n\n")

ep.set(align="LEFT", bold=False , size='normal')

ep.text("The on-board USB-Serial Adaptor is based on a Silabs CP2102 chip.")
ep.text(" OS specific drivers can be found on the manufacturer's website.\n")

ep.set(align="CENTER")
ep.text("\n")

ep.qr("http://www.silabs.com/products/mcu/Pages/USBtoUARTBridgeVCPDrivers.aspx")
ep.text("\n")

ep.set(align="CENTER", bold=True , size='2h')

ep.text("Sponsors\n")

ep.set(size='normal')
ep.text("\n")
ep.set(bold=True)
ep.text("Platinum Sponsors\n\n")
ep.set(bold=False)
ep.image("./VantagePoint.png")
ep.text("\n")
'''
ep.text("Vantage Point\n\n")
'''

ep.set(bold=True)
ep.text("Gold Sponsors\n\n")
ep.set(bold=False)
ep.image("./baml.jpg")
ep.text("\n")
'''
ep.text("Bank of America Merrill Lynch\n")
'''
ep.image("./CSA.jpg")
ep.text("\n")
'''
ep.text("Cyber Security Agency of Singapore\n")
'''
ep.image("./cybertestsystems.png")
ep.text("\n")
'''
ep.text("Cyber Test Systems\n")
'''
ep.cut()