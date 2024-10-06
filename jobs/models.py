from django.db import models

class job_type_choices(models.TextChoices):
    FULL_TIME = 'Full-Time'
    CONTRACT = 'Contract'
    PART_TIME = 'Part-Time'
    

class experience_level_choices(models.TextChoices):
    JUNIOR = 'Junior',
    INTERMEDIATE = 'Intermediate',
    SENIOR = 'Senior',
    

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    skills = models.JSONField()  # List of skills
    experience_level = models.CharField(max_length=50, choices=experience_level_choices.choices, null=False)
    desired_roles = models.JSONField(null=False)  # List of roles
    locations = models.JSONField()  # List of preferred locations
    job_type = models.CharField(max_length=50, choices=job_type_choices.choices,null=False)


    def __str__(self):
        return self.name

class JobPosting(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=255, null=False)
    company = models.CharField(max_length=255, null=False)
    required_skills = models.JSONField()  # List of required skills
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50,choices=job_type_choices.choices,null=False)
    experience_level = models.CharField(max_length=50, choices=experience_level_choices.choices, null=False)

    def __str__(self):
        return self.job_title
