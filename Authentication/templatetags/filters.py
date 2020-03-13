from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter(name='month')
def month(value):
    result = None
    if value == 1:
        result = 'styczeń'
    if value == 2:
        result = 'luty'
    if value == 3:
        result = 'marzec'
    if value == 4:
        result = 'kwiecień'
    if value == 5:
        result = 'maj'
    if value == 6:
        result = 'czerwiec'
    if value == 7:
        result = 'lipiec'
    if value == 8:
        result = 'sierpień'
    if value == 9:
        result = 'wrzesień'
    if value == 10:
        result = 'październik'
    if value == 11:
        result = 'listopad'
    if value == 12:
        result = 'grudzień'
    return result