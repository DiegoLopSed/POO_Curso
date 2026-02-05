from class_producto import Producto

class Pocion(Producto):
    def __init__(self, id_producto, nombre, descripcion, categoria, precio, ps_recuperacion, efecto_adicional):
        super().__init__(id_producto, nombre, descripcion, categoria, precio)
        self.ps_recuperacion = ps_recuperacion  # Cantidad de PS que recupera
        self.efecto_adicional = efecto_adicional  # Descripción o nombre del efecto adicional

    def __str__(self):
        base_str = super().__str__()
        adicional = f"\nPS Recuperación: {self.ps_recuperacion}"
        if self.efecto_adicional:
            adicional += f"\nEfecto Adicional: {self.efecto_adicional}"
        return base_str + adicional

