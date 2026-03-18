def listar_productos(productos):
    
    for producto in productos:
        print("~"*10)
        print(producto)   
        print("~"*10)

 
def agregar_producto(categoria):
    id_producto = int(input("Dame el id de tu producto: "))
    nombre = input("Ingresa el nombre de tu producto: ")
    descripcion = input("Ingresa la descripcion de tu producto:")
    precio = float(input("Ingresa el precio de tu producto: "))
    unidad = int(input("Ingresa la unidad de tu producto: "))
    ratio_captura = float(input("Ingresa el ratio de captura de tu producto: "))
    tipo = input("Ingresa el tipo de tu producto: ")
    bonificacion = input("Ingresa la bonificacion de tu producto: ")

    # Import local para evitar dependencias circulares al cargar módulos.
    from Clases.class_pokeball import Pokeball

    return Pokeball(
        id_producto=id_producto,
        nombre=nombre,
        descripcion=descripcion,
        categoria=categoria,
        precio=precio,
        unidad=unidad,
        ratio_captura=ratio_captura,
        tipo=tipo,
        bonificacion=bonificacion,
    )