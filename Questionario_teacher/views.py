import json
import random

from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse

from Questionario_teacher.custom_moduli import modulo_database
from Questionario_teacher.custom_moduli import util

from Moduli import modulo_system
from Moduli import modulo_functions


# costanti globali
last_page = 0


###############################################################################################


# function to open the connection to the database
def apri_connessione_db():
	path_db = util.FULLPATH_DB
	is_db_new = modulo_system.dimensione_file(path_db) <= 0
	database = modulo_database.Database(path_db)		# crea l'oggetto e apre la connessione
	if is_db_new:										# crea le tabelle solo se non ci sono gia'
		database.schema()
	return database


#################################################################################################


# These are the ENDPOINT, because you can call them from outside
def index(request, template_name='index.html'):
	global last_page
	# if the variable has been create outside the function (global) then it must be recalled inside
	# se devo leggere la variabile non serve, se invece devo modificarla serve global
	
	last_page = 0
	
	model_map = util.init_modelmap(request)
	return TemplateResponse(request, template_name, model_map)


def questionnaire_teacher(request, template_name='questionnaire_teacher.html'):
	model_map = util.init_modelmap(request)
	
	model_map['frasi'] = util.QUESTIONNAIRE
	model_map['intensity'] = range(util.QUESTIONNAIRE_INTENSITY)
	return TemplateResponse(request, template_name, model_map)


def questionnaire_teacher_save(request):
	nome = request.POST.get('nome', None)
	cognome = request.POST.get('cognome', None)
	
	connection_database = apri_connessione_db()
	connection_database.insert_questionario_teacher(nome, cognome)

	connection_database.conn_db.commit()
	connection_database.close_conn()


