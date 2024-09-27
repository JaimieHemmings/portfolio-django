from django.db import models
import uuid

# Create your models here.
class Blog(models.Model):
    def get_path(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return f'blog_images/{filename}'
    
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    exerpt = models.CharField(max_length=200)
    date = models.DateField()
    author = models.CharField(max_length=50)
    author_title = models.CharField(max_length=50)
    slug = models.SlugField()
    main_img = models.ImageField(upload_to=get_path)
    lead_paragraph = models.TextField()
    first_content = models.TextField()
    subtitle_one = models.CharField(max_length=200)
    second_content = models.TextField()
    subtitle_two = models.CharField(max_length=200)
    body_img = models.ImageField(upload_to=get_path)
    third_content = models.TextField()
    thumb_img = models.ImageField(upload_to=get_path)
    body_img_two = models.ImageField(upload_to=get_path)



    def __str__(self):
        return self.title