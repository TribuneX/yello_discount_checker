from bottle import route, run, template
from app.discount_scraper import get_discount
import json


@route('/discount/<plz>')
def discount(plz):
    discount = get_discount(plz)
    return json.dumps({'plz': plz, 'discount' : int(discount)})


@route('/dummy')
def dummy():
    return json.dumps({'discount': 10})

run(host='0.0.0.0', port=5000)
