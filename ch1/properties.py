class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property # means the getter .
    def celsius(self):
        print("📖 Lecture de la température")
        return self._celsius

    @celsius.setter
    def celsius(self, valeur):
        print(f"✍️ Changement de température à {valeur}°C")
        if valeur < -273.15:
            raise ValueError("Température en dessous du zéro absolu !")
        self._celsius = valeur
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @property
    def kelvin(self):
        return self._celsius + 273.15

temp = Temperature(25)

print(temp.celsius)

temp.celsius = 30

print(f"{temp.celsius}°C = {temp.fahrenheit}°F = {temp.kelvin}K")

try:
    temp.celsius = -300
except ValueError as e:
    print(f"Erreur : {e}")
