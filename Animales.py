class Animales:
    def __init__(self, raza , edad , color):
        self.raza = raza
        self.edad = edad
        self.color = color
        self.is_comer = False
    def start_comer(self):
        self.is_comer = True
        print("El animal esta comiendo")
    def hizo_popo(self):
        self.is_comer = False
        print("El animal hizo popo")
    def cumple_años(self):
        self.edad = self.edad + 1
        print("El animal cumplio un año mas")
mojito = Animales("conejo", "2", "blanco")  
print(mojito.raza, mojito.edad, mojito.color)
mojito.start_comer()
mojito.hizo_popo()
mojito.cumple_años()