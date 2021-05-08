import json
import urllib3
from beautifulsoup4 import BeautifulSoup

def lambda_handler(event, context):
    http = urllib3.PoolManager()
    xpath_columnas = "/html/body/div[2]/div/table/tbody/tr[1]/td" # Forzada a la primera fila de la tabla!
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
        rutSalida = cols[0].text.strip()
        return {
            'statusCode': 200,
            'body': {
                'nombre': nombre,
                'rutSalida': rutSalida
            }
        }