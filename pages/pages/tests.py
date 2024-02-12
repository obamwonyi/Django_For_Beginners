from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    """
    This is the test class for the Home Page
    Url
    """
    def test_url_exist_at_correct_location(self):
        """
        This method test if the url exist at the
        correct http locations for the home page
        """
        response = self.client.get("/")
        # here we are matching the status code to see
        # if the code returned by the response is equal to 200
        # which is the ok status code, if equal it returns true
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """
        This will test if the url name(home) that was
        assigned to the home route can actually be used
        to reference the home route.
        """
        response = self.client.get(reverse("home"))
        # the same 200 status match as the method above
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """
        This method test if the template name home is
        the correct for home url/url name
        """
        response = self.client.get(reverse("home"))
        # Check if the url name (home) is actually loading
        # the right template
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        """
        This method would test if the template this
        class is loading is the actual template we
        are ment to load , which is the home page(home.html)
        """
        response = self.client.get(reverse("home"))
        # checks if the template loaded from the url
        # has the content <h1>Homepage</h1> in it
        self.assertContains(response, "<h1>Homepage</h1>")


class AboutPageTests(SimpleTestCase):
    """
    This is the test class for the About Page
    Url
    """
    def test_url_exist_at_correct_location(self):
        """
        This method test if the url exist at the
        correct http location for the about page
        """
        response = self.client.get("/about")
        # here we are matching the status code to see
        # if the code returned by the response is equal to 200
        # which is the ok status code, if equal it returns true
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """
        This method test if the url name(about) that was
        assigned in the urls page can actually be used to
        reference the about page
        """
        response = self.client.get(reverse("about"))
        # The same 200 status match as the method above
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """
        This method would test if the template this
        class is loading is the actual template we
        are ment to load , which is the about page(about.html)
        """
        response = self.client.get(reverse("about"))
        # Check if the url name (about) is actually loading
        # the right template
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        """
        This method would test if the template this
        class is loading is the actual template we
        are ment to load , which is the about page(about.html)
        """
        response = self.client.get(reverse("about"))
        # checks if the template loaded from the url
        # has the content <h1>Aboutpage</h1> in it
        self.assertContains(response, "<h1>Aboutpage</h1>")
