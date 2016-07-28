# Firmwares

## Firmware 1: XCTF

You can find the firmware provided during the competition [here](https://github.com/geekman/badger)! The writeup's [here](http://irq5.io/2016/07/19/x-ctf-2016-badge-firmware/)!

## Firmware 2: Test harness

This repository hosts the test harness for the ESP-8266 based Neander board.

## Arduino programming setup

The [Arduino IDE](https://www.arduino.cc/en/Main/Software) can be used to upload code to the Neander board.

To setup your Arduino IDE environment to compile and upload code to the Neander, you may refer to [this tutorial](https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/using-arduino-ide).

## Serial programming/debugging setup

There are many serial programming utilities for the ESP8266 chips, we support [this](https://github.com/themadinventor/esptool). You can also use [this](https://github.com/igrr/esptool-ck). **YMMV**

``` sh
# installs esptool.py, a python utility that allows for serial programming and debugging of ESP8266 chips
pip install esptool
```

## Firmware Upload

The flash mode, size and frequency have to be set to the specific values based on the ESP12-F modules.

``` sh
esptool.py -p {insert port here} write_flash 0x00000 firmware/0x00000.bin 0x40000 firmware/0x40000.bin --flash_mode dio --flash_size 32m --flash_freq 40m
```

## Firmware Dump

This command dumps the flash memory from the region 0x0000 to 0x7490 to firmware/0x00000.bin.dump

``` sh
esptool.py -p {insert port here} read_flash 0x0000 0x7490 firmware/0x00000.bin.dump
```

## GCC Toolchain setup

We use [esp-open-sdk](https://github.com/pfalcon/esp-open-sdk), a collection of open-source utilities for compilation of source code to the xtensa instruction set architecture (used in ESP8266).

Once set up, you may reference the xtensa toolchain by 

```
export PATH={installation_dir}/esp-open-sdk/xtensa-lx106-elf/bin:$PATH
```

## Compilation and Upload of test suite

```sh
make rebuild
```

## Wiki

You can refer to [esp8266-wiki](https://github.com/esp8266/esp8266-wiki/wiki) learn more about the ESP8266, its features, architecture, boot process and memory map.
