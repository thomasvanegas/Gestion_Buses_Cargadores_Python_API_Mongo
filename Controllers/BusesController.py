# Importando paquetes
from fastapi import APIRouter
from DbContexts.MongoDbContext import cliente
from Services.BusService import BusesService, BusService

# Instaciamiento
router = APIRouter()

# Definicion de ruta raiz
@router.get('/')
def read_root() -> str:
    return 'Hola, Bienvenido a la Implementación de la API como Desarrollo del Parcial N°4'

# Rutas (HTTP VERBS) para la Entidad/Coleccion Buses

@router.get('/buses')
def find_all_buses():
    return BusesService(cliente.local.buses.find())

@router.get('/buses/{id}')
def find_bus_by_id():
    return {'placa': 'ABC123'}

@router.post('/buses')
def insert_new_bus():
    return {'placa': 'ABC123'}

@router.put('/buses/{id}')
def update_bus():
    return {'placa': 'ABC123'}

@router.delete('/buses/{id}')
def delete_bus():
    return {'placa': 'ABC123'}