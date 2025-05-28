import requests
import os

def obtener_imagen_pokemon(nombre_pokemon):
    # Convertir el nombre a minúsculas para la búsqueda
    nombre_pokemon = nombre_pokemon.lower()
    
    # URL de la API de Pokémon
    url = f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}'
    
    # Realizar la solicitud a la API
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        # Obtener datos del Pokémon
        datos = respuesta.json()
        # Obtener la URL de la imagen
        imagen_url = datos['sprites']['front_default']
        
        # Descargar la imagen
        imagen_respuesta = requests.get(imagen_url)
        
        if imagen_respuesta.status_code == 200:
            # Definir el nombre del archivo
            nombre_archivo = f"{nombre_pokemon}.png"
            # Guardar la imagen en la misma carpeta
            with open(nombre_archivo, 'wb') as archivo:
                archivo.write(imagen_respuesta.content)
            print(f"Imagen guardada como: {nombre_archivo}")
        else:
            print("Error al descargar la imagen.")
    else:
        print("Pokémon no encontrado.")

# Ejemplo de uso
nombre = input("Introduce el nombre de un Pokémon: ")
obtener_imagen_pokemon(nombre)
