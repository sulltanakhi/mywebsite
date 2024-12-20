from django.db import models

# Create your models here.

class Setting(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    smptserver = models.CharField(blank=True,max_length=50)
    smptemail = models.CharField(blank=True,max_length=50)
    smptpassword = models.CharField(blank=True,max_length=10)
    smptport = models.CharField(blank=True,max_length=5)
    youtube = models.URLField(blank=True, max_length=50)
    instagram = models.URLField(blank=True, max_length=50)
    facebook = models.URLField(blank=True, max_length=50)
    icon = models.ImageField(blank=True, upload_to='images/')
    aboutus = models.CharField(max_length=300)
    contact = models.CharField(max_length=300)

    def __str__(self):
        return self.title
