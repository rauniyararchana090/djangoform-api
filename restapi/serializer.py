from rest_framework import serializers
from . models import Airport


class  AirportSerializer (serializers.ModelSerializer):
     class Meta:
         model= Airport
         fields = '__all__'

'''  iata= serializers.CharField(max_length=100)
    icao= serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    location= serializers.CharField(max_length=100)
    gps= serializers.CharField(max_length=100)
           
    def create(self,validated_data):
        return Airport.objects.create(validated_data)

    def update(self,instance, validated_data): 
        instance.iata = validated_data.get('iata',instance.iata)
        instance.icao = validated_data.get('icao',instance.icao)
        instance.name = validated_data.get('name',instance.name)
        instance.location = validated_data.get('location',instance.location)
        instance.gps = validated_data.get('gps',instance.gps)
        instance.save()
        return instance''' 


