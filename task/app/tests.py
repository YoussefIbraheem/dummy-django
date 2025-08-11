from django.test import TestCase
from app.models import Category, Tag, Author, Article
from django.contrib.auth.models import User


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category", slug="test-category")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Test Category")

    def test_category_slug(self):
        self.assertEqual(self.category.slug, "test-category")
        
    def test_category_description(self):
        self.assertEqual(self.category.description, "")
        
class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag", slug="test-tag", color="#ff0000")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "Test Tag")

    def test_tag_color(self):
        self.assertEqual(self.tag.color, "#ff0000")
        

class AuthorModelTest(TestCase):
    def setUp(self):     
        self.user = User.objects.create_user(username="testuser", password="password")
        self.author = Author.objects.create(user=self.user, bio="Test bio")

    def test_author_str(self):
        self.assertEqual(str(self.author), "testuser")

    def test_author_bio(self):
        self.assertEqual(self.author.bio, "Test bio")
        


class ArticleModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testauthor", password="password")
        self.author = Author.objects.create(user=self.user)
        self.category = Category.objects.create(name="Test Category", slug="test-category")
        self.tag = Tag.objects.create(name="Test Tag", slug="test-tag")

        self.article = Article.objects.create(
            title="Test Article",
            slug="test-article",
            author=self.author,
            category=self.category,
            status=Article.Status.PUBLISHED
        )
        self.article.tags.add(self.tag)

    def test_article_str(self):
        self.assertEqual(str(self.article), "Test Article")

    def test_article_status(self):
        self.assertEqual(self.article.status, Article.Status.PUBLISHED)

    def test_article_tags(self):
        self.assertIn(self.tag, self.article.tags.all())
