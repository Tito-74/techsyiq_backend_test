from rest_framework import serializers
from .models import TechsyiqTeam, EnrollmentApplication




class TechsyiqTeamSerializers(serializers.ModelSerializer):
  class Meta:
    model = TechsyiqTeam
    fields = ['name', 'title', 'description', 'image', 'social_media_link','author']



class EnrollmentApplicationSerializers(serializers.ModelSerializer):
  class Meta:
    model = EnrollmentApplication
    fields = ['name', 'phone_no', 'module', 'email', 'starting_date']

