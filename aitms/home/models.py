from django.db import models

# Create your models here.
class Enquiry_contacts(models.Model):
    contact_name  = models.CharField(max_length=255)
    contact_email = models.EmailField(unique = True)
    contact_phone = models.CharField(max_length=10)
    contact_subject = models.CharField(max_length=100)
    contact_message = models.TextField()

class Vistor_contacts(models.Model):
    contact_name  = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=10)
    contact_subject = models.CharField(max_length=100)
    contact_message = models.TextField()

class Parscore(models.Model):
    Parscore_student_name  = models.CharField(max_length=255)
    Parscore_school_name  = models.CharField(max_length=255)
    Parscore_sector = models.CharField(max_length=50)
    Parscore_phone = models.CharField(max_length=10)
    Parscore_email = models.EmailField(unique = True)
    Parscore_location = models.CharField(max_length=60)
    Parscore_career = models.CharField(max_length=80)
    Parscore_career_other = models.CharField(max_length=80)