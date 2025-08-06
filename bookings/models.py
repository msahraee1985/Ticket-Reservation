from django.db import models
from django.conf import settings
from transport.models import Transport

class Booking(models.Model):

  STATUS_CHOICES = [
    ('active', 'Active'),
    ('cancelled', 'Cancelled'),
    ]

  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
  seat_number = models.CharField(max_length=10)
  booking_date = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
  total_price = models.DecimalField(max_digits=10, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    # db_table = 'booking' — use this if a custom DB table name is needed; for now, the default is <app_name>_<model_name>
    unique_together = ('transport', 'seat_number') 
  
  def __str__(self):
    return f"Booking by {self.user.username} on {self.transport}"
  
# Payment model added here as a mock implementation. 
# It is not related to other models in the app.
class Payment(models.Model):
  PAYMENT_METHODS = [
    ('credit_card', 'Credit Card'),
    ('cash', 'Cash'),
    ('paypal', 'PayPal'),
  ]

  STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('paid', 'Paid'),
  ]

  booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  method = models.CharField(max_length=50, choices=PAYMENT_METHODS)
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Payment for Booking #{self.booking.id} - {self.status}"
