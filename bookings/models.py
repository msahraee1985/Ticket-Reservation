from django.db import models
from django.conf import settings
from transport.models import Transport

class Booking(models.Model):

  STATUS_CHOICES = [
    ('active', 'Active'),
    ('canceled', 'Canceled'),
    ]

  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
  seat_number = models.CharField(max_length=10)
  booking_date = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
  total_price = models.DecimalField(max_digits=10, decimal_places=2)



  class Meta:
    # db_table = 'booking' — use this if a custom DB table name is needed; for now, the default is <app_name>_<model_name>
    unique_together = ('transport', 'seat_number') 
  
  def __str__(self):
      return f"Booking by {self.user.username} on {self.transport}"
