from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField
# from ckeditor.fields import RichTextField

# Create your models here.

STARTING_DATE = (
    ("2ND Feb","2ND Feb"),
    ("8th Aug", "8th Aug"),
    ("9th Nov", "9th Nov"),
  )
# Create your models here.

class TechsyiqTeam(models.Model):
  name = models.CharField(max_length=255)
  title= models.CharField(max_length=255)
  social_media_link = models.URLField(blank=True)
  description = models.TextField(blank=False)
  image = CloudinaryField('images', default=None)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  


  
class EnrollmentApplication(models.Model):
  name = models.CharField(max_length=255)
  phone_no = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  module = models.CharField(max_length=255)
  starting_date = models.CharField(max_length=255, choices = STARTING_DATE,
  default = '2ND Feb', null=False)

  def __str__(self): 
    return self.name