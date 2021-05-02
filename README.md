# International Standard Atmosphere
Python functions for calculating ISA 1976 values as a function of height.

The isa.py file contains three functions, getDensity(h), getTemperature(h) and getPressure(h). They each take the height above mean sea level in meters as argument, and returns values in SI units, i.e. getDensity returns the density in kg/m³, getTemperature returns the temperature in K, and getPressure returns the pressure in Pa.

While both getDensity and getPressure approaches zero as height approaches infinity, getTemperature only returns a temperature while h < 84852 m. Above this height, the getTemperature function returns false.
