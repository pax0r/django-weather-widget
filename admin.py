from django.contrib import admin

# Register your models here.
from weather_widget.models import WeatherLocation


class WeatherLocationAdmin(admin.ModelAdmin):
     exclude = ('json_data','last_query')

admin.site.register(WeatherLocation, WeatherLocationAdmin)