from django.urls import path
from .views import *

urlpatterns = [
    path('',Header.as_view(),name = "header"),
    path('home',Home.as_view(),name='home'),
    path('about',About.as_view(),name='about'),
    path('login',Login.as_view(),name="login"),
    path('logout',Logout.as_view(),name = 'logout'),
    path('signup',UserRegistation.as_view(),name ='signup'),
    path('profile',Profile.as_view(),name = "profile"),
    path('adduserprofiel',AddUserProfile.as_view(),name = 'adduserprofile'),
    path('alluser',AllUser.as_view(),name = 'alluser'),
    path('sendnote/<int:pk>',SendNote.as_view(),name = 'sandnote'),
    path('allsendnote',AllSandNotes.as_view(),name = 'allsendnote'),
    path("allrecivednote",AllReviedNotes.as_view(),name = 'allrecivenote'),
    path('search',SearchFirend.as_view(),name = "searchfriend"),
    path('reviedsearch',SearchReciver.as_view(),name="searchrecived"),
    path('updateprofile/<int:pk>',ProfileUpdate.as_view(),name = "profileupdate"),

]