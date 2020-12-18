from django.contrib import admin
from .models import Airport
from import_export.admin import ImportExportModelAdmin
from restapi.models import Airport

# Register your models here.
admin.site.register(Airport)


class AirportAdmin(ImportExportModelAdmin):
    list_display = ("iata","icao","name","location","gps")
    pass