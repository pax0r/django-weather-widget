from datetime import datetime, timedelta
import urllib2
from django.db import models

from django.utils.timezone import utc

#How frequent the weather is checked (in minutes)
FREQUENCY = 240
#Use metrical (Celcius) or imperial (Farenheit)
METRIC = True
#Language code from http://openweathermap.org/API#weather
LANGUAGE = 'pl'
#APPID from http://openweathermap.org/appid
#It can work without APPID but it is recommended by OpenWeatherMap
APPID = None



class WeatherLocation(models.Model):
    simple_name = models.CharField(max_length=10, unique=True)
    loc_query = models.CharField(max_length=30)
    json_data = models.TextField(null=True, blank=True)
    last_query = models.DateTimeField(default=datetime.min.replace(tzinfo=utc))
    days = models.IntegerField()

    @classmethod
    def get_json_data(cls, location):
        weatherloc = None
        try:
            weatherloc = cls.objects.get(pk=location)
        except ValueError or cls.DoesNotExist:
            weatherloc = cls.objects.get(simple_name__iexact=location.__str__())

        td = datetime.now(tz=utc) - weatherloc.last_query
        frequency = timedelta(minutes=FREQUENCY)
        if not td or frequency < td:
        #if True:
            url = "http://api.openweathermap.org/data/2.5/forecast/daily?q="
            url += weatherloc.loc_query
            if METRIC:
                url += "&units=metric"
            else:
                url += "&units=imperial"

            url += "&cnt=" + weatherloc.days.__str__()
            url += "&lang=" + LANGUAGE
            if APPID:
                url += "&APPID=" + APPID
            try: #in case of error use stored data and try again next time
                response = urllib2.urlopen(url)
                json_data = response.read()
                response.close()
                weatherloc.json_data = json_data
                weatherloc.last_query = datetime.now()
                weatherloc.save()
            except:
                pass
        return weatherloc.json_data

    def __unicode__(self):
        return self.simple_name.__str__()

