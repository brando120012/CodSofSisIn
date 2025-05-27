#Llamadas http / Requests

#get - Envia parametros atravez de la url                            stados Http.
#Post - Envia información en el cuerpo del mensaje / body            100
#Put - Envia infor en body - Inserta registros                        .
#Delete - Body - Eliminar registro                                    .
#Patch - Actualiza registro                                          600
 
#Mensajes                                                            <! Doctype xml/>
#XML                                                                   <name>                                                        
# JSON
#HTTP 
#Binarios 

from hashlib import md5
from requests import get
from datetime import datetime

class RestMarvel:
    timestamp = datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    pub_key = 'a2c3cdb138a7917154e2e8e015ebc548'
    priv_key = '72efd166ed1b558d2ced91aa820b1ece3348c07c'

    def hash_params(self):
        hash_md5 = md5()
        hash_md5.update(f'{self.timestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
        hashed_params =  hash_md5.hexdigest()
        return hashed_params
    
    def get_heroes(self):
        params = {'ts': self.timestamp, 'apikey': self.pub_key, 'hash': self.hash_params()}
        results = get('https://gateway.marvel.com:443/v1/public/characters', params=params)

        data = results.json()
        print(data)
        print(data['status'])

rest = RestMarvel()
rest.get_heroes