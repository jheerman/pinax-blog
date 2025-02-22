from django.contrib.auth import get_user_model
from django.test import TestCase

from ..forms import PostForm
from ..models import Blog, Post, Section
from .test_blog import randomword


class TestForms(TestCase):
    def setUp(self):
        super().setUp()

        self.user = get_user_model().objects.create_user(
            username="patrick", password="password"  # nosec
        )
        self.user.save()
        self.blog = Blog.objects.first()
        self.section = Section.objects.create(name="hello", slug="hello")
        self.content = "You won't believe what happened next!"
        self.teaser = "Only his dog knows the truth"
        self.title_len = Post._meta.get_field("title").max_length

    def test_max_slug(self):
        """
        Ensure Post can be created with slug same length as title.
        """
        title = randomword(self.title_len)
        form_data = {
            "section": self.section,
            "title": title,
            "content": self.content,
            "teaser": self.teaser,
            "state": 1,
        }
        form = PostForm(data=form_data)
        # slug field is not validated in form
        self.assertTrue(form.is_valid())
        # slug field is set (from title) in model .save() method
        self.assertTrue(form.save(blog=self.blog, author=self.user))
