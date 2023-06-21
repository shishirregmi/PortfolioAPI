from portfolio.serializers import *

class ProfileService():
    def get():
        try:
            profile = ProfileSerializer(Profile.objects.first()).data
            social = SocialSerializer(Social.objects.all(), many=True).data
            res = {'profile': profile, 'social': social}
            return {'code':200, 'data':res}
        except Exception as ex:
            return {'code': 500, 'message': str(ex)}
    
class AboutService():
    def get():
        try:
            about = AboutSerializer(About.objects.first()).data
            skill = SkillSerializer(Skill.objects.filter(isHidden=False), many=True).data
            res = {'about': about, 'skill': skill}
            return {'code':200, 'data':res}
        except Exception as ex:
            return {'code': 500, 'message': str(ex)}
    
class BlogService():
    def getAll():
        try:
            res = BlogSerializer(Blog.objects.all(), many=True).data
            return {'code':200, 'data':res}
        except Exception as ex:
            return {'code': 500, 'message': str(ex)}
        
    def get(req):
        try:
            res = BlogSerializer(Blog.objects.get(id = req)).data
            return {'code':200, 'data':res}
        except Exception as ex:
            return {'code': 500, 'message': str(ex)}
    
class EducationService():
    def get():
        try:
            res = EducationSerializer(Education.objects.all(), many=True).data
            return {'code':200, 'data':res}
        except Exception as ex:
            return {'code': 500, 'message': str(ex)}

class ExperienceService():
    def get():
        try:
            res = ExperienceSerializer(Experience.objects.all(), many=True).data
            return {'code':200, 'data':res}
        except Exception as ex:
            return {'code': 500, 'message': str(ex)}
    
class ContactService():
    def get():
        try:
            about = AboutSerializer(About.objects.first()).data
            social = SocialSerializer(Social.objects.all(), many=True).data
            res = {'about': about, 'social': social}
            return {'code':200, 'data':res}
        except Exception as ex:
            return {'code': 500, 'message': str(ex)}
    
class EmailService():
    def get(req):
        try:
            serializer = EmailMessageSerializer(data=req.data)
            if serializer.is_valid():
                serializer.save()
                return {'code': 200, 'data': serializer.data}
            return {'code': 400, 'message': serializer.errors}
        except Exception as ex:
            return {'code': 500, 'message': str(ex)}
