from django.db import models
import uuid
from ckeditor.fields import RichTextField

# Create your models here.
class PortfolioItem(models.Model):
    
    def get_path(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return f'portfolio/{filename}'

    title = models.CharField(max_length=100, blank=False, null=False)
    description_one = RichTextField(config_name='default')
    description_two = RichTextField(config_name='default')
    exerpt = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to=get_path, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    external_link = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to=get_path, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title