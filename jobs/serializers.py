from rest_framework import serializers
from .models import UserProfile, JobPosting

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['name', 'skills', 'experience_level', 'desired_roles', 'locations', 'job_type']
        extra_kwargs = {'__all__': {'required': False}}
    
    def validate(self, attrs):
        allowed_fields = set(self.Meta.fields)
        extra_fields = set(attrs.keys()) - allowed_fields
        if extra_fields:
            raise serializers.ValidationError(f"Invalid fields: {', '.join(extra_fields)}")

        return attrs

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'
