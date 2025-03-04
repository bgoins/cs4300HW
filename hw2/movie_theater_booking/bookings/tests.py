from django.test import TestCase
from django.utils.timezone import now
from .models import Movie, Seat, Booking
from datetime import date
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class MovieModelTest(TestCase):
    def test_create_movie(self):
        movie = Movie.objects.create(
            title="Test Movie",
            description="Test Description",
            release_date=date(2025, 1, 1),
            duration=120
        )
        self.assertEqual(movie.title, "Test Movie")
        self.assertEqual(movie.description, "Test Description")
        self.assertEqual(movie.release_date, date(2025, 1, 1))
        self.assertEqual(movie.duration, 120)
    
    def test_movie_creation_triggers_seat_creation(self):
        Movie.objects.create(
            title="movie2",
            description="desc2",
            release_date="2025-02-01",
            duration=100
        )
        self.assertEqual(Seat.objects.count(), 20)

class SeatModelTest(TestCase):
    def test_create_seat(self):
        seat = Seat.objects.create(seat_number=1, is_booked=False)
        self.assertEqual(seat.seat_number, 1)
        self.assertFalse(seat.is_booked)
    
class BookingModelTest(TestCase):
    def test_create_booking(self):
        movie = Movie.objects.create(
            title="movie3",
            description="desc3",
            release_date="2025-03-01",
            duration=90
        )
        seat = Seat.objects.create(seat_number=5, is_booked=False)
        booking = Booking.objects.create(
            movie=movie,
            seat=seat,
            user="user1",
            booking_date=now()
        )
        self.assertEqual(booking.movie.title, "movie3")
        self.assertEqual(booking.seat.seat_number, 5)
        self.assertEqual(booking.user, "user1")

class APITestCases(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="movieapi",
            description="descapi",
            release_date=date(2025, 1, 1),
            duration=120
        )
        
        self.seat = Seat.objects.create(seat_number=1, is_booked=False)
        self.user_name = "userapi"
        
    def test_get_movies(self):
        url = reverse("movie-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
    
    def test_get_seats(self):
        url = reverse("seat-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
    
    def test__seat_booking(self):
        url = reverse("book_seat", kwargs={"movie_id": self.movie.id, "seat_id": self.seat.id})
        response = self.client.post(url, {"user": self.user_name}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Seat.objects.get(id=self.seat.id).is_booked)
    
    def test_booking_history(self):
        url = reverse("booking_history")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
