from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserAuthTests(APITestCase):

  def setUp(self):
    self.register_url = reverse('register') 
    self.token_url = reverse('token_obtain_pair') 
    self.token_refresh_url = reverse('token_refresh') 
    self.create_staff_url = reverse('create_staff')

    # Create SuperUser 
    self.superuser = User.objects.create_superuser(
      username='admin', password='admin123', email='admin@example.com'
    )

    # Create NormalUser 
    self.normal_user = User.objects.create_user(
      username='user', password='user123', email='user@example.com'
    )

  def authenticate(self, user):
    refresh = RefreshToken.for_user(user)
    self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

  def test_register_user(self):
    response = self.client.post(self.register_url, {
      'username': 'newuser',
      'password': 'newpass123',
      'email': 'new@example.com'
    }, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertTrue(User.objects.filter(username='newuser').exists())

  def test_register_existing_user(self):
    response = self.client.post(self.register_url, {
      'username': 'user',
      'password': 'newpass123',
      'email': 'duplicate@example.com'
    }, format='json')
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

  def test_token_obtain(self):
    response = self.client.post(self.token_url, {
      'username': 'user',
      'password': 'user123'
    }, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertIn('access', response.data)
    self.assertIn('refresh', response.data)

  def test_token_refresh(self):
    refresh = RefreshToken.for_user(self.normal_user)
    response = self.client.post(self.token_refresh_url, {
      'refresh': str(refresh)
    }, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertIn('access', response.data)

  def test_create_staff_user_by_superuser(self):
    self.authenticate(self.superuser)
    response = self.client.post(self.create_staff_url, {
      'username': 'staff1',
      'password': 'staffpass',
      'email': 'staff1@example.com'
    }, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    user = User.objects.get(username='staff1')
    self.assertTrue(user.is_staff)

  def test_create_staff_user_by_normal_user_forbidden(self):
    self.authenticate(self.normal_user)
    response = self.client.post(self.create_staff_url, {
      'username': 'hacker',
      'password': 'hack123',
      'email': 'hacker@example.com'
    }, format='json')
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
