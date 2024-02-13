from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.


class BlogTests(TestCase):
    """
    For testing the blog post model and associated
    urls
    """

    @classmethod
    def setUpTestData(cls):
        """
        For creating a dummy data in the model
        for testing purpose
        """
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@gmail.com", password="secret"
        )

        cls.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            author=cls.user,
        )

    def test_post_model(self):
        """
        This would test all entries for the post model
        """
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1")

    def test_url_exists_at_correct_location_listview(self):
        """
        This would test if the home route works properly
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        """
        This would test if the post route with a primary key works properly
        """
        response = self.client.get("/post/1")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        """
        This would test if the route name works and if the template loaded is the
        right template for the route that is also tested.
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice body content")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detailview(self):
        """
        This would test if the post_detail with primary key route works properly
        when a primary key passed is available (200 status) and if it returns
        a status code of not found when the primary key passed is not available
        it will also test the right template and content.
        """
        response = self.client.get(reverse("post_detail",
                                           kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "post_detail.html")

    def test_post_createview(self):
        response = self.client.post(
            reverse("post_new"),
            {
                "title": "New title",
                "body": "New text",
                "author": self.user.id
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().body, "New text")

    def test_post_updateview(self):  # new
        """
        When I run the test the error I get is that the status code do not match
        also when I skip status code I also got the error that the recent updated
        value does not match the values I just entered , which means the update was not
        successful .
        """
        response = self.client.post(
            reverse("post_edit", args=[1]),
            {
                "title": "Updated title",
                "body": "Updated text",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Updated title")
        self.assertEqual(Post.objects.last().body, "Updated text")

    def test_post_deleteview(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)
