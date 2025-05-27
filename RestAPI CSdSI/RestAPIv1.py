from hashlib import md5
from requests import get
from datetime import datetime

class RestMarvel:
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Agregado espacio entre fecha y hora
    pub_key = 'a2c3cdb138a7917154e2e8e015ebc548'
    priv_key = '72efd166ed1b558d2ced91aa820b1ece3348c07c'

    def hash_params(self):
        hash_md5 = md5()
        hash_md5.update(f'{self.timestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
        hashed_params = hash_md5.hexdigest()
        return hashed_params
    
    def get_heroes(self):
        params = {'ts': self.timestamp, 'apikey': self.pub_key, 'hash': self.hash_params()}
        results = get('https://gateway.marvel.com:443/v1/public/characters', params=params)

        if results.status_code == 200:
            data = results.json()
            print(data)
        else:
            print(f"Error: {results.status_code} - {results.text}")  # Manejo de errores

rest = RestMarvel()
rest.get_heroes()  # Llamada correcta al método
