# Servicio para obtener un solo bus -> find_bus_by_id
def BusService(bus) -> dict:
    return {
        "id": bus["id"],
        "placa": bus["placa"],
        "marca": bus["marca"],
        "estado": bus["estado"]
    }


# Servicio para obtener todos los buses -> find_all_buses
def BusesService(buses_list) -> list:
    [BusesService(bus) for bus in buses_list]