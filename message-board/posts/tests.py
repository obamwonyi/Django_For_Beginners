from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.


class PostTests(TestCase):
    """
    This class will be used for the various
    test for the post model
    """

    @classmethod
    def setUpTestData(cls):
        """
        This method would create a new data entry in the text column
        which value is "This is a text!"
        Note: this table created would automatically be
        destroyed after the test have been made.And also
        note the only test that get to run in a class are the
        methods that start with the test keyword.
        Note: also the @classmethod decorator , tells python that this
        method should be passed the class it's self as
        an argument, this argument is commonly stored in the parameter "cls".
        """
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        """
        This method would then check if the value created in the
        method above is equal to the one we are passing
        to the second parameter in the assertEqual method
        """
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        """
        This would test if a particular url responsible
        for loading the post display exist
        """
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        """
        This would test if a particular url can be accessed
        by the name that has been set to reference it .
        Would also test if the correct template used for the url
        is home.html .
        Would also test if the template is the one with the right
        content.
        """
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "home.html")

        self.assertContains(response, "<h1>Message board homepage</h1>")


