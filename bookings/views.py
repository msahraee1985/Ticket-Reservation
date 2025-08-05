from rest_framework import viewsets, permissions
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # فقط رزروهای خود کاربر
        return self.queryset.filter(
            user=self.request.user,
            status='active'
            ).select_related('transport').order_by('transport__departure_date_time')