# Vocore 2 max6675 thermocouple module library

This is an Arduino inspired library for interfacing between Vocore2 and the module max6675 for thermocouples.

Made by Bryan Barbosa from [Federal University of Juiz de Fora](https://ufjf.br/) and [CREA - University of California, Berkeley](https://crea.berkeley.edu/).

## Importing

The library can be used simply by importing the Python file to your project.

```python
import max6675
```
Or, for an easier usage and more Arduino-like, you can import it like this:
```python
from max6675 import *
```

## Usage
The usage of the library is simple. Follow the steps:

1. Define variables for the pins where the 6675 module is connected.
2. Create an instance of the max6675 passing the three variables as parameteres.
3. Get the temperature readings by calling the functions ".read_[...]", that can return values in Celsius, Fahrenheit and Kelvin.

Here's a code example:

```python
from max6675 import *
from vocoreGPIO import *

#1. Defining pins
sclk = 39
cs = 40
miso = 41

#2. Creating an instance of the max6675 class
t = max6675(sclk, cs, miso)

while(1):
    c = t.read_celsius() #Getting reading in Celsius
    f = t.read_fahrenheit() #Getting reading in Fahrenheit
    k = t.read_kelvin() #Getting reading in Kelvin

    print("C:", c, "   F:", f, "   K:", k)
    delay(15000)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
