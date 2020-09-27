from django.urls import path

from . import views		# from same folder

urlpatterns = [
	path('', views.index, name='index'),	# [] list
	path('questionnaire_kids', views.questionnaire_kids, name='questionnaire_kids'),
	path('questionnaire_kids_save', views.questionnaire_kids_save, name='questionnaire_kids_save'),
	path('choice_image', views.choice_image, name='choice_image'),
	path('save_choice', views.save_choice, name='save_choice'),
	path('slider', views.slider, name='slider'),
	path('slider_save', views.slider_save, name='slider_save'),
	path('numerical_comparison', views.numerical_comparison, name='numerical_comparison'),
	path('summation', views.summation, name='summation'),
	path('number_after', views.number_after, name='number_after'),
	path('number_before', views.number_before, name='number_before'),
	path('number_closer', views.number_closer, name='number_closer'),
	path('shapes', views.shapes, name='shapes'),
	path('pencils_length', views.pencils_length, name='pencils_length'),
	path('final_page', views.final_page, name='final_page')
]
