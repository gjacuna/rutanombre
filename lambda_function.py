import json
import urllib3
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    http = urllib3.PoolManager()
    
    r = http.request(
        'POST',
        'https://www.nombrerutyfirma.com/rut',
        fields={'term': event['rut']}
    )
    
    soup = BeautifulSoup(r.data, "html.parser")
    
    table = soup.find('table', attrs={'class':'table table-hover'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    if len(rows) == 0:
        return {
            'statusCode': 404,
            'body': 'Rut no encontrado'
        }
    else:
        cols = rows[0].find_all('td')
        nombre = cols[0].text.strip()
        rutSalida = cols[1].text.strip()
        return {
            'statusCode': 200,
            'body': {
                'nombre': nombre,
                'rutSalida': rutSalida
            }
        }