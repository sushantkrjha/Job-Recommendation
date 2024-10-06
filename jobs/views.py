from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import JobPosting
from .serializers import UserProfileSerializer
from django.http import Http404


class JobRecommendationView(APIView):
    def post(self, request):
        # import pdb;pdb.set_trace()
        serializer = UserProfileSerializer(data=request.data)

        if serializer.is_valid():
            # Save the user profile
            user_profile = serializer.save()
        else:
            raise Http404("Input data is not valid.")

        try:
            # Retrieve job postings
            job_postings = JobPosting.objects.filter(
                experience_level=user_profile.experience_level,
                job_type=user_profile.job_type,
            )
            job_skills = [", ".join(job.required_skills) for job in job_postings]
            job_locations = [
                job.location if job.location else "" for job in job_postings
            ]
            job_roles = [job.job_title for job in job_postings]

            # Create user skills string for vectorization
            user_skills_str = " ".join(user_profile.skills)
            user_location_str = " ".join(user_profile.locations)
            user_roles_str = " ".join(user_profile.desired_roles)

            job_combined = [
                skills + " " + locations + " " + desired_roles
                for skills, locations, desired_roles in zip(
                    job_skills, job_locations, job_roles
                )
            ]

            user_combined = (
                user_skills_str + " " + user_location_str + " " + user_roles_str
            )

            # Vectorization
            vectorizer = TfidfVectorizer()
            vectors = vectorizer.fit_transform([user_combined] + job_combined)

            # Calculate cosine similarity
            cosine_similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

            # With experinencing simmilarity scores on sample data come to the point that threshold score 10% works well
            threshold = 0.1
            # Filter the jobs and their corresponding cosine similarity scores
            jobs_with_similarity = [
                (job, score)
                for job, score in zip(job_postings, cosine_similarities)
                if score >= threshold
            ]

            # Sort jobs by similarity score in descending order
            jobs_with_similarity.sort(key=lambda x: x[1], reverse=True)

            # Get the top 5 job postings based on similarity
            final_jobs = jobs_with_similarity[:5]

            # Prepare the response
            response_data = [
                {
                    "job_title": job.job_title,
                    "company": job.company,
                    "location": job.location,
                    "job_type": job.job_type,
                    "required_skills": job.required_skills,
                    "experience_level": job.experience_level,
                }
                for job, score in final_jobs
            ]

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception:
            return Response(
                {"msg": "Something went wrong."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
