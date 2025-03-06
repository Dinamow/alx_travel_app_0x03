from rest_framework import viewsets
from .serializers import ListingSerializer, BookingSerializer
from .models import Listing, Booking
from .tasks import send_booking_confirmation_email


class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing listings.
    Provides CRUD operations for Listing model.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing bookings.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        user_email = booking.user.email
        booking_details = f"Booking ID: {booking.id}, Destination: {booking.destination}"

        send_booking_confirmation_email.delay(user_email, booking_details)