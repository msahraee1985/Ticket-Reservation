from rest_framework import serializers
from .models import Booking




class BookingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)


    
    class Meta:
        model = Booking
        fields = ['id', 'user', 'transport', 'seat_number', 'booking_date', 'status', 'total_price']
        read_only_fields = ['booking_date', 'status']  # وضعیت در API دستی تغییر نمی‌کنه

    def validate(self, attrs):
        transport = attrs.get('transport')
        seat_number = attrs.get('seat_number')

        if Booking.objects.filter(transport=transport, seat_number=seat_number).exists():
            raise serializers.ValidationError("این صندلی قبلاً رزرو شده است.")

        return attrs

    def create(self, validated_data):
        transport = validated_data['transport']
        price_per_seat = transport.price  # فرض بر اینکه Transport مدل قیمت داره
        validated_data['total_price'] = price_per_seat

        booking = Booking.objects.create(**validated_data)
        return booking