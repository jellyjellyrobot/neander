# nEanDer Firmware

The nEanDer is a microcontroller platform that is created for NUS GreyHat's XCTF.

This board is based on the ESP8266 microcontroller series by Espressif and derives certains parts from Adafruit's Feather and Sparkfun's Thing based on the same microcontroller platform.

## Specifications

- ESP8266 32 bit Microcontroller platform with Integrated 802.11 b/g/n
- AutoReset Feature
- 500mA 3.3V Voltage Regulator
- USB-Serial Interface (CP2102)
- 7 Buttons (including Reset)
- Lithium Polymer Battery
- Lithium Polumer Charger

## Codenames

FeTChX

## Contributors

Jacob
Darell
Yu Siang
Jeremias

Shell

1
2
3
4
5
sudo python ./esptool.py --port /dev/ttyUSB0 write_flash 0x00000 ../nodemcu_integer_0.9.6-dev_20150704.bin
[sudo] password for jaufranc:
Connecting...
Erasing flash...
Writing at 0x00048000... (65 %)


Read more: http://www.cnx-software.com/2015/10/29/getting-started-with-nodemcu-board-powered-by-esp8266-wisoc/#ixzz459CQPVxu


esptool.py -p /dev/cu.SLAB_USBtoUART write_flash 0x00000 ./nodemcu_float_0.9.6-dev_20150704.binq




brew tap homebrew/dupes
brew install binutils coreutils automake wget gawk libtool gperf gnu-sed --with-default-names grep
export PATH="/usr/local/opt/gnu-sed/libexec/gnubin:$PATH"
sudo hdiutil create ~/Documents/case-sensitive.dmg -volname "case-sensitive" -size 10g -fs "Case-sensitive HFS+"
sudo hdiutil mount ~/Documents/case-sensitive.dmg
cd /Volumes/case-sensitive

git clone --recursive https://github.com/pfalcon/esp-open-sdk.git
#https://github.com/pfalcon/esp-open-sdk/issues/45
cd esp-open-sdk
make

brew install gnu-sed
ln -s /usr/local/Cellar/gnu-sed/4.2.2/bin/sed /usr/local/bin/gsed

gsed -i '1s/^/#include <stddef.h>\n/' crosstool-NG/.build/src/gcc-4.8.2/gcc/graphite.c 
gsed -i '1s/^/#include <stddef.h>\n/' crosstool-NG/.build/src/gcc-4.8.2/gcc/graphite-blocking.c 
gsed -i '1s/^/#include <stddef.h>\n/' crosstool-NG/.build/src/gcc-4.8.2/gcc/graphite-clast-to-gimple.c
gsed -i '1s/^/#include <stddef.h>\n/' crosstool-NG/.build/src/gcc-4.8.2/gcc/graphite-dependences.c 
gsed -i '1s/^/#include <stddef.h>\n/' crosstool-NG/.build/src/gcc-4.8.2/gcc/graphite-interchange.c 
gsed -i '1s/^/#include <stddef.h>\n/' crosstool-NG/.build/src/gcc-4.8.2/gcc/graphite-optimize-isl.c 
gsed -i '1s/^/#include <stddef.h>\n/' crosstool-NG/.build/src/gcc-4.8.2/gcc/graphite-poly.c 
gsed -i '1s/^/#include <stddef.h>\n/' crosstool-NG/.build/src/gcc-4.8.2/gcc/graphite-scop-detection.c 
gsed -i '1s/^/#include <stddef.h>\n/' crosstool-NG/.build/src/gcc-4.8.2/gcc/graphite-sese-to-poly.c



#Xtensa toolchain is built, to use it:
sudo hdiutil mount ~/Documents/case-sensitive.dmg
export PATH=/Volumes/case-sensitive/esp-open-sdk/xtensa-lx106-elf/bin:$PATH

## xtensa-lx106-elf-gcc -I$(THISDIR)/sdk/include -L$(THISDIR)/sdk/lib
