import uuid
from django.conf import settings

from django.db import models

from useraccount.models import User

# Create your models here.
class Property(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(default="Apartment")

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    country = models.CharField(max_length=100)
    country_code = models.CharField(max_length=20)

    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    guests = models.CharField(default="1")
    bedrooms = models.CharField(default="1")
    bathrooms = models.CharField(default="1")
    available_from = models.DateField(null=True, blank=True)
    available_to = models.DateField(null=True, blank=True)

    image = models.ImageField(upload_to='uploads/properties/')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def image_url(self):
        if self.image:
            return f"{settings.WEBSITE_URL}{self.image.url}"
        return None
    

class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="reservations")
    start_date = models.DateField()
    end_date = models.DateField()
    guests = models.IntegerField(default=1)
    total_price = models.FloatField()
    created_by = models.ForeignKey(User, related_name="reservations", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)