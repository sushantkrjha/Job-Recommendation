# jobs/management/commands/populate_jobs.py
from django.core.management.base import BaseCommand
from jobs.models import JobPosting

class Command(BaseCommand):
    help = 'Populate mock job postings'

    def handle(self, *args, **kwargs):
        job_data = [
            {
                "job_id": 1,
                "job_title": "Software Engineer",
                "company": "Tech Solutions Inc.",
                "required_skills": ["JavaScript", "React", "Node.js"],
                "location": "San Francisco",
                "job_type": "Full-Time",
                "experience_level": "Intermediate"
            },
            {
                "job_id": 2,
                "job_title": "Data Scientist",
                "company": "Data Analytics Corp.",
                "required_skills": ["Python", "Data Analysis", "Machine Learning"],
                "location": "Remote",
                "job_type": "Full-Time",
                "experience_level": "Intermediate"
            },
            {
                "job_id": 3,
                "job_title": "Frontend Developer",
                "company": "Creative Designs LLC",
                "required_skills": ["HTML", "CSS", "JavaScript", "Vue.js"],
                "location": "New York",
                "job_type": "Part-Time",
                "experience_level": "Junior"
            },

            {
                "job_title": "Backend Developer",
                "company": "Web Services Co.",
                "required_skills": ["Python", "Django", "REST APIs"],
                "location": "Chicago",
                "job_type": "Full-Time",
                "experience_level": "Senior"
            },
            {
                "job_id": 5,
                "job_title": "Machine Learning Engineer",
                "company": "AI Innovations",
                "required_skills": ["Python", "Machine Learning", "TensorFlow"],
                "location": "Boston",
                "job_type": "Full-Time",
                "experience_level": "Intermediate"
            },
            {
                "job_id": 6,
                "job_title": "DevOps Engineer",
                "company": "Cloud Networks",
                "required_skills": ["AWS", "Docker", "Kubernetes"],
                "location": "Seattle",
                "job_type": "Full-Time",
                "experience_level": "Senior"
            },
            {
                "job_id": 7,
                "job_title": "Full Stack Developer",
                "company": "Startup Hub",
                "required_skills": ["JavaScript", "Node.js", "Angular", "MongoDB"],
                "location": "Austin",
                "job_type": "Full-Time",
                "experience_level": "Intermediate"
            },
            {
                "job_id": 8,
                "job_title": "Data Analyst",
                "company": "Finance Analytics",
                "required_skills": ["SQL", "Python", "Tableau"],
                "location": "New York",
                "job_type": "Full-Time",
                "experience_level": "Junior"
            },
            {
                "job_id": 9,
                "job_title": "Quality Assurance Engineer",
                "company": "Reliable Software",
                "required_skills": ["Selenium", "Java", "Testing"],
                "location": "San Francisco",
                "job_type": "Contract",
                "experience_level": "Intermediate"
            },
            {
                "job_id": 10,
                "job_title": "Systems Administrator",
                "company": "Enterprise Solutions",
                "required_skills": ["Linux", "Networking", "Shell Scripting"],
                "location": "Remote",
                "job_type": "Full-Time",
                "experience_level": "Senior"
            }


  

                    
        ]
        
        for job in job_data:
            JobPosting.objects.create(**job)

        self.stdout.write(self.style.SUCCESS('Successfully populated job postings'))
