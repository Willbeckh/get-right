from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

from .models import Doctor, Patient

class PatientCustomRegistrationSerializer(RegisterSerializer):
    patient = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    area = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    age = serializers.CharField(required=True)
    
    def get_cleaned_data(self):
            data = super(PatientCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'area' : self.validated_data.get('area', ''),
                'address' : self.validated_data.get('address', ''),
                'age': self.validated_data.get('age', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(PatientCustomRegistrationSerializer, self).save(request)
        user.is_patient = True
        user.save()
        patient = Patient(patient=user, area=self.cleaned_data.get('area'), 
                address=self.cleaned_data.get('address'),
                age=self.cleaned_data.get('age'))
        patient.save()
        return user


class DoctorCustomRegistrationSerializer(RegisterSerializer):
    doctor = serializers.PrimaryKeyRelatedField(read_only=True,) #by default allow_null = False
    specialization = serializers.CharField(required=True)    

    
    
    def get_cleaned_data(self):
            data = super(DoctorCustomRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'specialization' : self.validated_data.get('specialization', ''),
            }
            data.update(extra_data)
            return data

    def save(self, request):
        user = super(DoctorCustomRegistrationSerializer, self).save(request)
        user.is_doctor = True
        user.save()
        doctor = Doctor(doctor=user,specialization=self.cleaned_data.get('specialization'))
        doctor.save()
        return user
