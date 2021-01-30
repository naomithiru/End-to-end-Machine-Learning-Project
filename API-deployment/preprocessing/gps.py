from pyproj import Proj, transform
import requests


def longitude_latitude(address):
    """
    Sample address = 186,Kloosterstraat,Dilbeek,1702 
    Template = nb,street,city,pc = house_number,street,city,
    Seperator is , comma
    """
    words = address.split(",")
    nb = words[0]
    street = words[1]
    city = words[2]
    pc = int(words[3])
    x2, y2 = 0, 0

    if (1300 <= pc and pc <= 1499) or (4000 <= pc and pc <= 7999) \
                                   or (pc >= 1000 and pc <= 1299):  # 'W' + bxl
        req = requests.get(
            f"http://geoservices.wallonie.be/geolocalisation/rest/getPositionByCpRueAndNumero/{pc}/{street}/{nb}/").json()
        x1 = req['x']
        y1 = req['y']
    else:  # region = 'F'
        req = requests.get(
            f"https://api.basisregisters.dev-vlaanderen.be/v1/adresmatch?gemeentenaam={city}&straatnaam={street}&huisnummer={nb}&postcode={pc}").json()
        x1 = req['adresMatches'][0]['adresPositie']['point']['coordinates'][0]
        y1 = req['adresMatches'][0]['adresPositie']['point']['coordinates'][1]
    x2, y2 = transform(Proj(init='epsg:31370'),
                       Proj(init='epsg:4313'), x1, y1)
    return x2, y2
