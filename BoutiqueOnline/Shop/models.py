from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=56)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    category = models.ManyToManyField(Category)
    published = models.BooleanField(default=True)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField(default='')
    picture = models.ImageField(blank=True, null=True, upload_to="Imges")

    class Meta:
        verbose_name = "Article"

    def __str__(self):
        return self.title

    @property
    def publier(self):
        return "publier" if(self.published) else "non publier"

    def pub_or_no(self):
        return self.author.username if self.author else "inconnu"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)