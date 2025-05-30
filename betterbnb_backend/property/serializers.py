from rest_framework import serializers

from .models import Property, Reservation

from useraccount.serializers import UserDetailSerializer

class PropertiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id',
            'title',
            'price_per_night',
            'image_url',
        ]

class PropertyDetailSerializer(serializers.ModelSerializer):
    host = UserDetailSerializer(read_only=True, many=False)
    class Meta:
        model = Property
        fields = [
            'id',
            'title',
            'host',
            'description',
            'category',
            'latitude',
            'longitude',
            'country',
            'price_per_night',
            'image_url',
            'guests',
            'bedrooms',
            'bathrooms',
        ]

class PropertyReservationSerializer(serializers.ModelSerializer):
    property = PropertyDetailSerializer(read_only=True, many=False)
    class Meta:
        model = Reservation
        fields = [
            "start_date",
            "end_date",
            "guests",
            "total_price",
            'id',
            'property',
        ]