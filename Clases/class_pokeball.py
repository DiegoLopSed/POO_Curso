from Clases.class_producto import Producto

class Pokeball(Producto):
    def __init__(self, id_producto, nombre, descripcion, categoria, precio, unidad, ratio_captura, tipo, bonificacion):
        super().__init__(id_producto, nombre, descripcion, categoria, precio,unidad)
        self.ratio_captura = ratio_captura  # Valor numérico de la ratio de captura
        self.tipo = tipo                    # String (por ejemplo: "Ultra Ball", "Master Ball")
        self.bonificacion = bonificacion    # Descripción o valor del bonus aplicado

    def __str__(self):
        return (super().__str__() +
                f"\nTipo de Pokeball: {self.tipo}\n"
                f"Ratio de Captura: {self.ratio_captura}\n"
                f"Bonificación: {self.bonificacion}")

