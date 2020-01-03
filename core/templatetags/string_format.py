from django import template

register = template.Library()

@register.filter
def ws_to_20(value):
    return value.replace(" ","%20")

@register.filter
def com_to_non(value):
    return value.replace(",","").strip()
