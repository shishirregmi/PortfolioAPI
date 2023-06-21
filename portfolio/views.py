from rest_framework.response import Response
from rest_framework.decorators import api_view
from portfolio.services import *

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'profile/',
        'about/',
        'blogs/',
        'blogs/{id}',
        'email/'
    ]
    return Response(routes)

@api_view(['GET'])
def getProfile(request):
    res = ProfileService.get()
    return Response(res)

@api_view(['GET'])
def getAbout(request):
    res = AboutService.get()
    return Response(res)

@api_view(['GET'])
def getBlogs(request):
    res = BlogService.getAll()
    return Response(res)

@api_view(['GET'])
def getBlog(request,id):
    res = BlogService.get(id)
    return Response(res)

@api_view(['GET'])
def getContact(request):
    res = ContactService.get()
    return Response(res)

@api_view(['GET'])
def getEducation(request):
    res = EducationService.get()
    return Response(res)

@api_view(['GET'])
def getExperience(request):
    res = ExperienceService.get()
    return Response(res)

@api_view(['POST'])
def sendEmail(request):
    serializer = EmailMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)