class textos:
    def __init__(self, Titulo, Autor, Editorial):
        self.Titulo = Titulo
        self.Autor = Autor
        self.Editorial = Editorial
        self.is_open = False
    def start_open(self):
        self.is_open = True
        print("El libro esta abierto")
    def finish_open(self):
        self.is_open = False
        print("El libro esta cerrado")
    def start_read(self):
        self.is_open = True
        print("El libro esta siendo leido")
    def star_change(self):
        self.is_open = True
        print("El libro fue cambiado")       
libro = textos("El principito", "Antoine de Saint-Exupéry", "Reynal & Hitchcock")
print(libro.Titulo, libro.Autor, libro.Editorial)
libro.start_open()
libro.finish_open()
libro.start_read()
libro.star_change()