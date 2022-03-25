from django.urls import path  
from django.contrib import admin  
from . import views  
from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home, name='home'),
     path('newproject/',views.new_project,name='newproject'),
     path('profile/',views.profile,name = 'profile'),
     path('search/',views.search_results,name = 'search_results'),
     path('comment/<int:id>/',views.comment,name='comment'),
     path('rate/<int:id>/',views.rate,name='rates'),
     path('api/profile/',views.ProfileList.as_view()),
     path('api/projects/',views.ProfileList.as_view()),
     path('singleproject/(\d+)',views.single_project,name='singleproject'),
     path('editprofile/',views.edit_profile,name='editprofile'),
     path('logout/',views.logout_request,name='logout')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)