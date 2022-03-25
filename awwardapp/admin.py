from django.contrib import admin
from .models import Profile,Projects,Ratings,Comments
# Register your models here.
admin.site.register(Profile)
admin.site.register(Projects)
admin.site.register(Comments)
admin.site.register(Ratings)