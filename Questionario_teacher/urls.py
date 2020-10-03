from django.urls import path

from . import views  # from same folder

urlpatterns = [
	path('', views.index, name='index'),  # [] list
	path('questionnaire_teacher', views.questionnaire_teacher, name='questionnaire_teacher'),
	path('questionnaire_teacher_save', views.questionnaire_teacher_save, name='questionnaire_teacher_save'),
]
