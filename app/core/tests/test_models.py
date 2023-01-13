"""
Tests for Models
"""
from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTest(TestCase):
    """Test models."""

    def test_create_user_with_email_sucessful(self):
        """Test creating a user with an emailis sucessful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['Test1@EXAMPLE.com', 'Test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for sample, another in sample_emails:
            user = get_user_model().objects.create_user(sample, 'sample123')
            self.assertEqual(user.email, another)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValuError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_new_super_user(self):
        """Test create superuser"""
        user = get_user_model().objects.create_superuser(
            'teste@123.com',
            'teste123',
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
