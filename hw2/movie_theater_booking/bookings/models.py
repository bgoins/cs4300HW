from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    release_date = models.DateField()
    duration = models.IntegerField()

class Seat(models.Model):
    seat_number = models.IntegerField()
    is_booked = models.BooleanField(default=False)

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    booking_date = models.DateTimeField(default=now)

@receiver(post_save, sender=Movie)
def create_seats_for_movie(sender, instance, created, **kwargs):
    if created:
        existing_seats = Seat.objects.count()
        if existing_seats == 0:
            for i in range(1, 21):
                Seat.objects.create(seat_number=i, is_booked=False)
