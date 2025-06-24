# capa de servicio/lógica de negocio
from ..transport import transport
from ...config import config
from ..utilities import translator



# función que devuelve un listado de cards. Cada card representa una imagen de la API de Pokemon
def getAllImages():
    raw_pokemon_data = transport.getAllImages()
    pokemon_cards = []  # Crea una lista vacía para almacenar las Card

    for pokemon_raw_data in raw_pokemon_data:  # Itera sobre cada Pokémon crudo
        try:
            # Convierte cada diccionario de datos crudos en un objeto Card
            card = translator.fromRequestIntoCard(pokemon_raw_data)
            pokemon_cards.append(card)  # Añade la Card a la lista
        except Exception as e:
            # Esto ayuda a depurar si hay un problema con un Pokémon específico
            print(
                f"[service.py]: Error al traducir Pokémon {pokemon_raw_data.get('name', 'desconocido')}: {e}")
            continue  # Continúa con el siguiente Pokémon si este falla

    return pokemon_cards  # Retorna la lista de Cards

# función que filtra según el nombre del pokemon.
def filterByCharacter(name):
    filtered_cards = []
    # Obtiene todas las imágenes/cards disponibles
    all_images = getAllImages()
    
    for card in all_images:
        # Verifica si el 'name' buscado (convertido a minúsculas) está contenido
        # en el nombre del Pokémon de la Card (también en minúsculas).
        if name.lower() in card.name.lower():
            filtered_cards.append(card)

    return filtered_cards

# función que filtra las cards según su tipo.
def filterByType(type_filter):
    filtered_cards = []
    # Obtiene todas las imágenes/cards disponibles
    all_images = getAllImages()

    for card in all_images:
        # Verifica si alguno de los tipos de la Card coincide con el tipo_filter
        # Se usa any() para comprobar si el tipo_filter (en minúsculas)
        # es igual a alguno de los tipos del Pokémon (también en minúsculas).
        if any(pokemon_type.lower() == type_filter.lower() for pokemon_type in card.types):
            filtered_cards.append(card)

    return filtered_cards

def get_type_icon_url_by_name(type_name):
    type_id = config.TYPE_ID_MAP.get(type_name.lower())
    if not type_id:
        return None
    return transport.get_type_icon_url_by_id(type_id)
