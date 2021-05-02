from django.test import TestCase
from django.contrib.auth import get_user_model


class TestModel(TestCase):

    def test_user_creation_successful(self):
        """Test whether user creation with email and password is successful"""
        email = 'testmail@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalized_user(self):
        """Test the email for normalized user"""
        email = 'testmail@gmail.com'
        user = get_user_model().objects.create_user(email, '97055@yOu')
        self.assertEqual(user.email, email.lower())

    def test_email_validation(self):
        """Test creating a user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_super_user(self):
        """Test create super user"""
        user = get_user_model().objects.create_superuser(
            'testmail@gmail.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
