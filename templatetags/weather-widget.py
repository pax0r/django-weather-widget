# coding=utf-8
from datetime import date
from django import template
import json
from weather_widget import models

from weather_widget.models import WeatherLocation

__author__ = 'pax0r'

register = template.Library()

@register.filter(name='format_temperature')
def format_temperature(value):
    if models.METRIC:
        return value + " &deg;C"
    else:
        return value + " &deg;F"


def weather_widget_tag(context, location):
    data = json.loads(WeatherLocation.get_json_data(location))
    for day in data['list']:
        day['dt'] = date.fromtimestamp(long(day['dt']))
    context.update({
        'data': data,
        'metric': models.METRIC
    })
    return context
# Register the custom tag as an inclusion tag with takes_context=True.
register.inclusion_tag('weather_widget/weather_widget.html', takes_context=True)(weather_widget_tag)