from django.urls import path

from . import views  # from same folder

urlpatterns = [
	path('', views.index, name='index'),  # [] list
	path('choice_image', views.choice_image, name='choice_image'),
	path('save_choice', views.save_choice, name='save_choice'),
	path('drag_drop', views.drag_drop, name='drag_drop'),
	path('slider', views.slider, name='slider'),
	path('final_page', views.final_page, name='final_page')
]
