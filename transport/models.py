from django.db import models

class Transport(models.Model):
  TRANSPORT_TYPES = [
    ('flight', 'Flight'),
    ('train', 'Train'),
    ('bus', 'Bus'),
  ]
    
  transport_type = models.CharField(max_length=10, choices=TRANSPORT_TYPES)
  origin = models.CharField(max_length=100)
  destination = models.CharField(max_length=100)
  arrival_date_time = models.DateTimeField()
  departure_date_time = models.DateTimeField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  capacity = models.PositiveIntegerField()

  class Meta:
    # db_table = 'transport' — use this if a custom DB table name is needed; for now, the default is <app_name>_<model_name>
    pass

  def __str__(self):
    return f"{self.transport_type} from {self.origin} to {self.destination}"
