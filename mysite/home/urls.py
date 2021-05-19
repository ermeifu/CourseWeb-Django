from django.urls import path

from home.views import show_menus, show_homes, show_courseMessage, show_homeImages, show_teachingResources, \
    show_referenceBooks

urlpatterns = [
    path('show_menus', show_menus, ),
    path('show_homes', show_homes, ),
    path('show_courseMessage', show_courseMessage, ),
    path('show_homeImages', show_homeImages, ),
    path('show_teachingResources', show_teachingResources, ),
    path('show_referenceBooks', show_referenceBooks, ),
]
