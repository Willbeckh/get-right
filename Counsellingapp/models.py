from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.http import request





class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_doctor = models.BooleanField(default=False)
  is_patient = models.BooleanField(default=False)

class Patient (models.Model):
    patient = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    area = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.TextField()

    def __str__(self):
        return self.patient.username

class Doctor (models.Model):
    doctor = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    specialization = models.CharField(max_length=100,default=None)     
     

    def __str__(self):
        return self.doctor.username




    
          


# Create your models here.
# Counselors can prescribe medication in the event that it is deemed necessary
# Counselors can create support groups for people that  were affected so they can share their issues with people suffering from the same problems.
# Clients can schedule sessions with counselors.
# Counselors can update the scheduled sessions based on their availability.




class Counselor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
  
    def __str__(self):
        return self.first_name
  





class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
   
    def __str__(self):
        return self.first_name



class SupportGroup(models.Model):
    counselor = models.ForeignKey(Counselor, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return self.counselor.first_name + " " + self.client.first_name

class Session(models.Model):
    counselor = models.ForeignKey(Counselor, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    support_group = models.ForeignKey(SupportGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.counselor.first_name + " " + self.client.first_name

class Medication(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dosage = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name



class MedicationDosage(models.Model):
    patient = models.ForeignKey(Client, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    dosage = models.PositiveIntegerField()
        

    def __str__(self):
        return self.patient.first_name + " " + self.medication.name



