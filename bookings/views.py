from rest_framework import viewsets, permissions
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(
            user=self.request.user,
            status='active'
        ).select_related('transport').order_by('transport__departure_date_time')

    @action(detail=True, methods=['post'], url_path='cancel')
    def cancel(self, request, pk=None):
        booking = self.get_object()

        # اطمینان از اینکه فقط صاحب رزرو می‌تونه کنسل کنه
        if booking.user != request.user:
            return Response({'detail': 'شما اجازه کنسل کردن این رزرو را ندارید.'},
                            status=status.HTTP_403_FORBIDDEN)

        if booking.status != 'active':
            return Response({'detail': 'رزرو قبلاً کنسل شده یا فعال نیست.'},
                            status=status.HTTP_400_BAD_REQUEST)

        booking.status = 'cancelled'
        booking.save()

        return Response({'detail': 'رزرو با موفقیت کنسل شد.'}, status=status.HTTP_200_OK)

