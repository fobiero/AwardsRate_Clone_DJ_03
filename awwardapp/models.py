from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    dpic = CloudinaryField('image', null=True)
    bio = models.TextField(max_length=1000,null=True)
    info = models.TextField(max_length=5000)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Projects(models.Model):
    title = models.CharField(max_length=500,null=True)
    description=models.TextField(max_length=2000)
    link=models.URLField()
    image=CloudinaryField('image')
    user = models.ForeignKey(User,on_delete = models.CASCADE)

    def save_project(self):
            self.save()

    @classmethod
    def all_projects(cls):
        all_projects = cls.objects.all()
        return all_projects

    @classmethod
    def one_project(cls,id):
        one_project = cls.objects.filter(id=id)
        return one_project

    @classmethod
    def user_projects(cls,user):
        user_projects = cls.objects.filter(user = user)
        return

    @classmethod
    def search_project(cls,search_term):
        searched_project = cls.objects.filter(title = search_term)
        return searched_project

    def __str__(self):
        return self.title
   
class Ratings(models.Model):
    design = models.IntegerField(default=1)
    usability = models.IntegerField(default=1)
    content = models.IntegerField(default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)

class Comments(models.Model):
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    user = models.ForeignKey(User,on_delete = models.CASCADE)

    @classmethod
    def get_all_comments(cls,id):
        comments = cls.objects.filter(project_id = id)
        return comments

    def save_comments(self):
        self.save()

    def delete_comment(self):
        self.delete()