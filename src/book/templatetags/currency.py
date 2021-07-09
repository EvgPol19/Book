import requests
from django import template

register = template.Library()

USD = 'https://www.nbrb.by/api/exrates/rates/840?parammode=1'
@register.simple_tag
def currency_rate():
    rate = requests.get(USD)
    return rate.json().get('Cur_OfficialRate')