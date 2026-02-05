class Categoria:
    
    def __init__(self, id_categoria, nombre, descripcion):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.descripcion = descripcion
        
    def __str__(self):
        return f"'{self.nombre}' Descripcion:'{self.descripcion}')"
        
   

