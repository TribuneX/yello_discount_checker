import requests
from lxml import html 
import re

def get_discount(plz):
    energy_amount = '4500'
    params = ({ 'sparte':'Strom', 
                'Plz': plz, 
                'Vertragsart':'Privatkunde',
                'auswahl':energy_amount,
                'verbrauch':energy_amount,
                'Einzugsart':'WohntLaengerAls4WochenVorOrt',
                'lieferbeginn':'01.12.2020'})

    r = requests.get('https://www.yello.de/strom/stromtarife?wt_from=1', params=params)

    tree = html.fromstring(r.content)
    discount_text = tree.xpath('//*[@id="page-top"]/body/main/section[2]/div/div[2]/div/div[1]/div/div[1]/text()')
    discount = re.search(r'\d{2}', str(discount_text))
    return discount.group(0)
