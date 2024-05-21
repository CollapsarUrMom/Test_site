# Напишите определение класса TemperatureConverter       
class TemperatureConverter:

    def __init__(self) -> None:
        pass

# Ниже код для проверки методов класса TemperatureConverter
assert TemperatureConverter.celsius_to_fahrenheit(0) == 32.0
assert TemperatureConverter.celsius_to_fahrenheit(10) == 50.0
assert TemperatureConverter.celsius_to_fahrenheit(15) == 59.0
assert TemperatureConverter.celsius_to_fahrenheit(20) == 68.0
assert TemperatureConverter.celsius_to_fahrenheit(25) == 77.0
assert TemperatureConverter.celsius_to_fahrenheit(30) == 86.0

assert TemperatureConverter.fahrenheit_to_celsius(86) == 30.0
assert TemperatureConverter.fahrenheit_to_celsius(77) == 25.0
assert TemperatureConverter.fahrenheit_to_celsius(68) == 20.0
assert TemperatureConverter.fahrenheit_to_celsius(59) == 15.0
assert TemperatureConverter.fahrenheit_to_celsius(50) == 10.0
assert TemperatureConverter.fahrenheit_to_celsius(32) == 0

converter = TemperatureConverter()
assert converter.celsius_to_kelvin(100) == 373.15
assert converter.kelvin_to_celsius(273.15) == 0
assert converter.fahrenheit_to_kelvin(50) == 283.15
assert converter.fahrenheit_to_kelvin(134.33) == 330.0
assert converter.kelvin_to_fahrenheit(54.0) == -362.47
assert converter.kelvin_to_fahrenheit(1653.0) == 2515.73
assert converter.format(1653.0, 'K') == '1653.0°K'
assert converter.format(45, 'F') == '45°F'
assert converter.format(36.6, 'C') == '36.6°C'

print('Good')