import sys
from pathlib import Path

# Añadir la raíz del proyecto para que se resuelvan Clases y Objetos
raiz = Path(__file__).resolve().parent.parent
if str(raiz) not in sys.path:
    sys.path.insert(0, str(raiz))
    
from Functions.main import *
from Clases.class_pokeball import Pokeball
from Objetos.Categorias import *

pokeball_normal = Pokeball(
    id_producto=101,
    nombre="Poké Ball",
    descripcion="Una Poké Ball estándar para capturar Pokémon.",
    categoria=Pokeballs,
    precio=200,
    unidad=6,
    ratio_captura=1.0,
    tipo="Poké Ball",
    bonificacion="Ninguna bonificación especial"
)

superball = Pokeball(
    id_producto=102,
    nombre="Super Ball",
    descripcion="Mejor que una Poké Ball normal. Aumenta las posibilidades de captura.",
    categoria=Pokeballs,
    precio=600,
    unidad=1,
    ratio_captura=1.5,
    tipo="Super Ball",
    bonificacion="Aumenta el ratio de captura un 50%"
)

ultraball = Pokeball(
    id_producto=103,
    nombre="Ultra Ball",
    descripcion="Poké Ball de alto rendimiento con una gran tasa de captura.",
    categoria=Pokeballs,
    precio=1200,
    unidad=1,
    ratio_captura=2.0,
    tipo="Ultra Ball",
    bonificacion="Duplica el ratio de captura base"
)

masterball = Pokeball(
    id_producto=104,
    nombre="Master Ball",
    descripcion="La mejor Poké Ball. Captura cualquier Pokémon sin fallar.",
    categoria=Pokeballs,
    precio=2000,
    unidad=1,
    ratio_captura=3.0,
    tipo="Master Ball",
    bonificacion="Captura cualquier Pokémon sin fallar"
)


pokeballs = [pokeball_normal, superball, ultraball]



listar_productos(pokeballs)

nueva_pokeball = agregar_producto(categoria=Pokeballs)
pokeballs.append(nueva_pokeball)

listar_productos(pokeballs)  