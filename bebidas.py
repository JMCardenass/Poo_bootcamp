class bebidas:
    def __init__(self, nombre, precio, sabor):
        self.nombre = nombre
        self.precio = precio
        self.sabor = sabor 
        self.is_on_cup = False
    def start_on_cup(self):
        self.is_on_cup = True
        print("La bebida esta en la taza")
    def finish_on_cup(self):
        self.is_on_cup = False
    print("No hay bebida en la taza")
sprite = bebidas("sprite", "10k", "limon")
print(sprite.nombre, sprite.precio, sprite.sabor)
sprite.start_on_cup()
sprite.finish_on_cup()