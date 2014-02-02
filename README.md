django-weather-widget
=====================

A simple widget to display weather forecast for Django. Weather data from http://openweathermap.org/API.


Usage
-----
Configuration with comments is in models.py. Just put a code into your project directory and add 'weather_widget' to your INSTALLED_APPS and do a syncdb. The default template need also 'django.contrib.humanize'.

Next you need to create object for localization on which you want the weather. There are 3 fields you need to provide:
+ Simple name: a name which will be used to identify this location in template tag
+ Loc query: the name of the city for which you want the weather data. Check the data here: http://openweathermap.org/API
+ Days: for how many days you want the forecast in this location.

After object in db is created you need to put this template tags:

```
{% load weather-widget %}
{% weather_widget_tag 'simple_name' %}
```

where simple_name is the simple name for location you want to display (it can also be a PK of the weather_location object).

TODO:
----
+ Allow diffrent queries. OpenWeatherMap allows also longitude and laditude to be used or id. For now widget can use only city name 

Author and license
------------------
Author of this widget is Bartłomiej Biernacki (https://github.com/pax0r)  
License is MIT so you can you it use it as you wish.  
I would be glad if you could send me info if it is used on your website ;)
