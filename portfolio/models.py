from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField

class Profile(models.Model):
    fullname = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return self.fullname

class Social(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    classname = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class About(models.Model):
    profilepic = models.ImageField(upload_to='about/')
    Title = models.CharField(max_length=255)
    Description = models.TextField()
    BirthDate = models.DateField()
    Education = models.CharField(max_length=255)
    contactEmail = models.EmailField()
    address = models.CharField(max_length=255)
    businessEmail = models.EmailField()
    About = models.TextField()
    Resume = models.FileField(upload_to='about/')

    def __str__(self):
        return self.Title

class Skill(models.Model):
    title = models.CharField(max_length=255)
    level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    isHidden = models.BooleanField()

    class Meta:
        ordering = ['-level']

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='blogs/')
    content = RichTextField()
    skills = models.ManyToManyField('Skill', related_name='blogs')

    class Meta:
        ordering = ['-createdAt']

    def __str__(self):
        return self.title
    
class EmailMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = RichTextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} : {self.subject}"
    
class Education(models.Model):
    title = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    institute = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    title = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)
    company = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    description = RichTextField()
    skills = models.ManyToManyField(Skill)

    class Meta:
        ordering = ['-start']
    
    def __str__(self):
        return self.title