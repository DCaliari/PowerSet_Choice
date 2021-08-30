from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	
	path('questionnaire_kids', views.questionnaire_kids, name='questionnaire_kids'),
	path('questionnaire_kids_save', views.questionnaire_kids_save, name='questionnaire_kids_save'),
	
	path('video', views.video, name='video'),
	
	path('choice_image', views.choice_image, name='choice_image'),
	path('save_choice', views.save_choice, name='save_choice'),
	
	path('slider', views.slider, name='slider'),
	path('slider_save', views.slider_save, name='slider_save'),
	
	path('numerical_test', views.numerical_test, name='numerical_test'),
	path('save_numerical_test', views.save_numerical_test, name='save_numerical_test'),
	
	path('logic_test', views.logic_test, name='logic_test'),
	path('save_logic_test', views.save_logic_test, name='save_logic_test'),
	
	path('final_page_C', views.final_page, name='final_page_C')
]
