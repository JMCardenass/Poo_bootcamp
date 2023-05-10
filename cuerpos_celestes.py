class cuerposcelstes:
    def __init__(self,nombre,ubicacion,distancia):
        self.nombre=nombre
        self.ubicacion=ubicacion
        self.distancia=distancia
        self.is_on=False
    def start_light(self):
        self.is_on=True
        print("El cuerpo celeste brilla")
    def stop_light(self):
        self.is_on=False
        print("El cuerpo celeste explota")
sol=cuerposcelstes("sol","centro",1000000)
print(sol.nombre,sol.ubicacion,sol.distancia)
sol.start_light()
sol.stop_light()