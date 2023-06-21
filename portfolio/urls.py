from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes),
    path('profile/',views.getProfile),
    path('about/',views.getAbout),
    path('blog/',views.getBlogs),
    path('blog/<int:id>',views.getBlog),
    path('contact/',views.getContact),
    path('email',views.sendEmail),
    path('education/',views.getEducation),
    path('experience/',views.getExperience),
]