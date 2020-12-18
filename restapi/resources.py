from import_export import resources
from restapi.models import Airport

class AirportResource(resources.ModelResource):
    class Meta:
        model= Airport