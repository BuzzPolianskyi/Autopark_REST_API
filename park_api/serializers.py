from rest_framework import serializers
from park_api import models


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Driver
        fields = ['id', 'first_name', 'last_name', 'created_at', 'updated_at']


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    driver_id = serializers.ReadOnlyField(source='driver.last_name')

    class Meta:
        model = models.Vehicle
        fields = ['id', 'driver_id', 'make', 'model', 'plate_number', 'created_at', 'updated_at']
