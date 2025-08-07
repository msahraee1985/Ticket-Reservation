from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User 
from transport.models import Transport
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken


class TransportPermissionsTest(APITestCase):

  def setUp(self):
    # Create NormalUser
    self.normal_user = User.objects.create_user(
      username='normaluser', password='pass123', email='n@example.com'
    )

    # Create StaffUser
    self.staff_user = User.objects.create_user(
      username='staffuser', password='pass123', email='s@example.com', is_staff=True
    )

    self.url = reverse('transport-list')

    self.valid_data = {
      "origin": "Tehran",
      "destination": "Mashhad",
      "price": 100000,
      "transport_type": "bus",
      "arrival_date_time": "2025-08-15T10:00:00Z",
      "departure_date_time": "2025-08-16T10:00:00Z",
      "capacity": 40
    }

  def authenticate(self, user):
    refresh = RefreshToken.for_user(user)
    self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

  def test_create_transport_unauthenticated_user(self):
    response = self.client.post(self.url, self.valid_data)
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  def test_create_transport_normal_user(self):
    self.authenticate(self.normal_user)
    response = self.client.post(self.url, self.valid_data)
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_create_transport_staff_user(self):
    self.authenticate(self.staff_user)
    response = self.client.post(self.url, self.valid_data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    transport = Transport.objects.filter(id=response.data['id']).first()
    self.assertIsNotNone(transport)
    self.assertIsInstance(transport, Transport)

