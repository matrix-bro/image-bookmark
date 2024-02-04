from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="images_created", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to="images/%Y/%m/%d/")
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    
    # M-M with user
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_images", blank=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
