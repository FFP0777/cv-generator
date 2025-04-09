# CV_Gen/models.py
from django.db import models
from ckeditor.fields import RichTextField  # 如使用 CKEditor

class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    # summary = RichTextField(blank=True, null=True)
    # skills = RichTextField(blank=True, null=True)
    # previous_work = RichTextField(blank=True, null=True)
    # degree = models.CharField(max_length=200, blank=True, null=True)

    # school = models.CharField(max_length=200, blank=True)
    # university = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    
    additional_sections = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name
