from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class SignupPageTests(TestCase):
    """
    This is the test for the signup page 
    and the user sign up functionality 
    """
    def test_url_exists_at_correct_location_signupview(self):
        """
        Test if the right url is used for the
        user signup
        """
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        """
        Test if the right template is used for the
        user signup
        """
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        """
        Test if the various fields and signup data
        are working properly for user creation (insertion of data) .
        """
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuser@gmail.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        all_user_objects = get_user_model().objects.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(all_user_objects.count(), 1)
        self.assertEqual(all_user_objects[0].username, "testuser")
        self.assertEqual(all_user_objects[0].email, "testuser@gmail.com")
