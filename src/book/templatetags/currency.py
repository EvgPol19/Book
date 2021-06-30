import requests
from django import template

register = template.Library()

USD = 'https://www.nbrb.by/api/exrates/rates/145'
@register.simple_tag
def currency_rate():
    rate = requests.get(USD)
    return rate.json().get('Cur_OfficialRate')