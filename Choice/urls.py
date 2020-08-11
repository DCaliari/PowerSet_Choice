from django.urls import path

from . import views  # from same folder

urlpatterns = [
    path('', views.index, name='index'),  # [] list
    path('choice_image', views.choice_image, name='choice_image'),  # [] list
    path('final_page', views.final_page, name='final_page')
]
