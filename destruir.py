class Pelicula:
    #Contructor de clase
    def __init__ (self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print ('se a creado la pelicula', self.titulo)
    
    #Destructor de clase
    def __del__(self):
        print ('Se esta borrando la pelicula', self.titulo)
    

p = Pelicula("El Padrino",175,1972)
del(p)
