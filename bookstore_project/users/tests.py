from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):

    def test_create_user(self):
        User= get_user_model()
        user= User.objects.create_user(
            username='Nelg',
            email='nelg@liamg.com',
            password='testpass123',
        )
        self.assertEqual(user.username,'Nelg')
        self.assertEqual(user.email, 'nelg@liamg.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="Superman",
            email='superman@gmail.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'Superman')
        self.assertEqual(admin_user.email, 'superman@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
