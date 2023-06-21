from rest_framework import serializers
from .models import *
from datetime import datetime, timedelta
from django.utils import timezone

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['fullname', 'about']

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['id', 'name', 'link', 'classname', 'icon']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['profilepic', 'Title', 'Description', 'BirthDate', 'Education', 'contactEmail', 'address', 'businessEmail', 'About', 'Resume']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'title', 'level']

class BlogSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)
    createdAt = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'title', 'createdAt', 'thumbnail', 'content', 'skills']

    def get_createdAt(self, obj):
        now = timezone.now()
        elapsed_time = now - obj.createdAt

        if elapsed_time < timedelta(minutes=1):
            seconds = int(elapsed_time.total_seconds())
            return f'{seconds} seconds ago'
        elif elapsed_time < timedelta(hours=1):
            minutes = int(elapsed_time.total_seconds() // 60)
            return f'{minutes} minutes ago'
        elif elapsed_time < timedelta(days=1):
            hours = int(elapsed_time.total_seconds() // 3600)
            return f'{hours} hours ago'
        else:
            return obj.createdAt.strftime('%B %d, %Y')
        
class EmailMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailMessage
        fields = ['id', 'name', 'email', 'subject', 'message', 'sent_at']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'title', 'start', 'end', 'institute', 'description']

class ExperienceSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)

    class Meta:
        model = Experience
        fields = ['id', 'title', 'start', 'end', 'company', 'type', 'description', 'skills']