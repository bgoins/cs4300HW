from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MovieViewSet, SeatViewSet, BookingViewSet, 
    movie_list, seat_booking, book_seat, booking_history
)

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet, basename="bookings")

urlpatterns = [
    path('api/', include(router.urls)),
    path('', movie_list, name='movie_list'),
    path('movie/<int:movie_id>/seats/', seat_booking, name='seat_booking'),
    path("movie/<int:movie_id>/seat/<int:seat_id>/book/", book_seat, name="book_seat"),
    path("booking-history/", booking_history, name="booking_history"),
]
