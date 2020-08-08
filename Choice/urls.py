from django.urls import path

from . import views  # from same folder

urlpatterns = [
    path('', views.index, name='index'),  # [] list
    path('choice_image', views.choice_image, name='choice_image'),  # [] list
]
