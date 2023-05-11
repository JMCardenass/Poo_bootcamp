class Animales:
    def __init__(self, raza , edad , color):
        self._raza = raza
        self.edad = edad
        self.color = color
        self.is_comer = False
    def get_raza(self):
        return self._raza
    def start_comer(self):
        self.is_comer = True
        print("El animal esta comiendo")
    def salio_corriendo(self):
        self.is_comer = False
        print("El animal salio corriendo")
    def cumple_años(self):
        self.edad = int(self.edad) + 1

        print("El animal cumplio un año mas")
    def habla(self):
        pass
mojito = Animales("conejo", "2", "blanco")  
print(mojito.get_raza(), mojito.edad, mojito.color)
mojito.start_comer()
mojito.salio_corriendo()
mojito.cumple_años()
class Gato(Animales):
    def __init__(self, raza , edad , color, nombre):
        super().__init__(raza, edad, color)
        self.nombre = nombre
    def start_comer(self):
        self.is_comer = True
        print("El gato esta comiendo")
    def salio_corriendo(self):
        print("El gato salio corriendo")
    def cumple_años(self):
        self.edad = int(self.edad) + 1
        print("El gato cumplio un año mas")
    def habla(self):
        return"miau"
Romeo = Gato("persa", "3", "blanco", "Romeo")
print(Romeo.get_raza, Romeo.edad, Romeo.color, Romeo.nombre)
Romeo.start_comer() 
Romeo.salio_corriendo()
Romeo.cumple_años()
print(Romeo.habla())