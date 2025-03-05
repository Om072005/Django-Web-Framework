from django.db import models

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField()
    comments = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.guest_count} guests"


