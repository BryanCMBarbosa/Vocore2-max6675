# This library is public domain. Enjoy!
# Based on the original C++ library made by https://learn.adafruit.com/thermocouple/
# Made by Bryan Barbosa from UFJF and CREA Lab - UC Berkeley

from vocoreGPIO import *

class max6675:
    '''
    *Inicialize a MAX6675 sensor*
    SCLK The Arduino pin connected to Clock
    CS The Arduino pin connected to Chip Select
    MISO The Arduino pin connected to Data Out
    '''
    def __init__(self, SCLK:int, CS:int, MISO:int):
        self.sclk = SCLK
        self.cs = CS
        self.miso = MISO

        pinMode(self.cs, 'OUTPUT')
        pinMode(self.sclk, 'OUTPUT')
        pinMode(self.miso, 'INPUT')

        digitalWrite(self.cs, 'HIGH')


    '''
    *Read the Celsius temperature*
    =Returns Temperature in C or NaN on failure!=
    '''
    def read_celsius(self):
        digitalWrite(self.cs, 'LOW')
        delayMicroseconds(10)

        v = self.spiread()
        v <<= 8
        v |= self.spiread()

        digitalWrite(self.cs, 'HIGH')

        if(v & 0x4):
            # uh oh, no thermocouple attached!
            return float("NaN")

        v >>= 3

        return v * 0.25


    '''
    *Read the Fahrenheit temperature*
    =Returns Temperature in F or NaN on failure!=
    '''
    def read_fahrenheit(self):
        return self.read_celsius() * 9.0 / 5.0 + 32


    '''
    *Read the Kelvin temperature*
    =Returns Temperature in K or NaN on failure!=
    '''
    def read_kelvin(self):
        return self.read_celsius() + 273.15


    def spiread(self):
        d = 0

        for i in range(7, -1, -1):
            digitalWrite(self.sclk, 'LOW')
            delayMicroseconds(10)
            if(digitalRead(self.miso)):
                # set the bit to 0 no matter what
                d |= (1 << i)

            digitalWrite(self.sclk, 'HIGH')
            delayMicroseconds(10)

        return d
