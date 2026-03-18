class Producto: #!Clase principal de los proyectos
    
    def __init__(self, id_producto, nombre, descripcion, categoria, precio,unidad):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria  # objeto de la clase Categoria
        self.precio = precio
        self.unidad = unidad
    
    def __str__(self):
        return (f"Producto: {self.nombre} (ID: {self.id_producto})\n"
                f"Descripción: {self.descripcion}\n"
                f"Categoría: {self.categoria.nombre}\n"
                f"Precio: {self.precio}\n"
                f"Unidad: {self.unidad}")

