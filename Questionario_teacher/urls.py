from django.urls import path

from . import views  # importazione modulo nella cartella corrente

urlpatterns = [
	path('', views.index, name='index'),
	
	path('numero_alunni', views.numero_alunni, name='numero_alunni'),
	path('numero_alunni_save', views.numero_alunni_save, name='numero_alunni_save'),
	
	path('questionnaire_teacher', views.questionnaire_teacher, name='questionnaire_teacher'),
	path('questionnaire_teacher_save', views.questionnaire_teacher_save, name='questionnaire_teacher_save'),
	
	path('fine', views.fine, name='fine'),
]
