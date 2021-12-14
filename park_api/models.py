from django.db import models


class Driver(models.Model):
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['created_at']


class Vehicle(models.Model):
    driver_id = models.ForeignKey('Driver', related_name='cars', on_delete=models.CASCADE)  # link?
    make = models.CharField(max_length=100, blank=True, default='')
    model = models.CharField(max_length=100, blank=True, default='')
    plate_number = models.CharField(max_length=100, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.plate_number

    class Meta:
        ordering = ['created_at']
