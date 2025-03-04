from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    @action(detail=True, methods=['post'])
    def book(self, request, pk=None):
        seat = self.get_object()
        username = request.data.get('user')

        if not username:
            return Response({"error": "User field is required"}, status=400)
        
        if seat.is_booked:
            return Response({"error": "Seat is already booked"}, status=400)
        
        booking = Booking.objects.create(movie=seat.booking.movie, seat=seat, user=username)
        seat.is_booked = True
        seat.save()
        return Response({"message": "Seat booked successfully", "booking_id": booking.id})

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["GET"], url_path="user-bookings")
    def user_bookings(self, request):
        user_name = request.GET.get("user", "").strip()
        if not user_name:
            return Response([])

        bookings = Booking.objects.filter(user=user_name).select_related("movie", "seat")
        data = [
            {
                "movie_title": booking.movie.title,
                "seat_number": booking.seat.seat_number,
                "booking_date": booking.booking_date.strftime("%Y-%m-%d %H:%M:%S"),
            }
            for booking in bookings
        ]
        return Response(data)




def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(is_booked=False)

    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

@csrf_exempt
@require_POST
def book_seat(request, movie_id, seat_id):
    try:
        print("Received request at book_seat")
        print("Request method:", request.method)

        try:
            data = json.loads(request.body)
            user_name = data.get("user", "").strip()
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid JSON format"}, status=400)

        if not user_name:
            return JsonResponse({"success": False, "message": "User name is required."}, status=400)

        seat = Seat.objects.get(id=seat_id, is_booked=False)
        movie = Movie.objects.get(id=movie_id)

        Booking.objects.create(movie=movie, seat=seat, user=user_name)
        seat.is_booked = True
        seat.save()

        return JsonResponse({"success": True, "message": f"Seat {seat.seat_number} booked successfully!"})

    except Seat.DoesNotExist:
        return JsonResponse({"success": False, "message": "Seat is already booked."}, status=400)

    except Movie.DoesNotExist:
        return JsonResponse({"success": False, "message": "Movie not found."}, status=404)

    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)}, status=500)

def booking_history(request):
    return render(request, 'bookings/booking_history.html')







