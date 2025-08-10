from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.text import slugify


# =======================
#  Task 1: Basic Models
# =======================

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    color = models.CharField(max_length=7, default="#007bff")  # HEX color

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["user__username"]

    def __str__(self):
        return self.user.get_full_name() or self.user.username


# ===============================
#  Task 2: Advanced Article Model
# ===============================

class PublishedManager(models.Manager):
    """Custom manager to filter published articles."""
    def get_queryset(self):
        return super().get_queryset().filter(status=Article.Status.PUBLISHED)


class Article(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        PUBLISHED = "PUBLISHED", "Published"
        ARCHIVED = "ARCHIVED", "Archived"

    # Basic Fields
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True)
    featured_image = models.ImageField(upload_to="articles/", blank=True)

    # Relationships
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    # Status & Publishing
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    is_featured = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)

    # Metadata
    view_count = models.PositiveIntegerField(default=0)
    reading_time = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Managers
    objects = models.Manager()  # Default manager
    published = PublishedManager()  # Custom manager

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(fields=["slug"], name="unique_article_slug")
        ]
        indexes = [
            models.Index(fields=["status", "created_at"])
        ]

    def __str__(self):
        return self.title

    # ================
    # Custom Methods
    # ================

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def is_published(self):
        return self.status == self.Status.PUBLISHED

    def increment_view_count(self):
        self.view_count += 1
        self.save(update_fields=["view_count"])

    def calculate_reading_time(self):
        # Average reading speed ~ 200 words per minute
        words = len(self.content.split())
        self.reading_time = max(1, round(words / 200))
        self.save(update_fields=["reading_time"])

    # ==================
    # Custom Validation
    # ==================
    def clean(self):
        # Ensure published articles have a published_at date
        if self.status == self.Status.PUBLISHED and not self.published_at:
            raise ValidationError({"published_at": "Published articles must have a published date."})

        # Ensure excerpt is not longer than content
        if self.excerpt and len(self.excerpt) > len(self.content):
            raise ValidationError({"excerpt": "Excerpt cannot be longer than content."})

    def save(self, *args, **kwargs):
        # Auto-generate slug if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
