import os

from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.urls import reverse

from custom_project_moduli import project_util
from Questionario_teacher.custom_moduli import modulo_database
from Questionario_teacher.custom_moduli import util

from Moduli import modulo_system

# get l'ultima parte del path della cartella corrente
CARTELLA_CORRENTE = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

last_page = 0
n_alunni = '0'


###############################################################################################


# function to open the connection to the database
def apri_connessione_db():
	path_db = project_util.FULLPATH_DB
	is_db_new = modulo_system.dimensione_file(path_db) <= 0
	database = modulo_database.Database(path_db)  # crea l'oggetto e apre la connessione
	if is_db_new:  # crea le tabelle solo se non ci sono gia'
		database.schema()
	return database


#################################################################################################


# These are the ENDPOINT, because you can call them from outside
def index(request, template_name=os.path.join(CARTELLA_CORRENTE, 'index.html')):
	global last_page
	# if the variable has been create outside the function (global) then it must be recalled inside
	# se devo leggere la variabile non serve, se invece devo modificarla serve global
	
	model_map = util.init_modelmap(request)
	return TemplateResponse(request, template_name, model_map)


def numero_alunni(request, template_name=os.path.join(CARTELLA_CORRENTE, 'numero_alunni.html')):
	model_map = util.init_modelmap(request)
	return TemplateResponse(request, template_name, model_map)


def numero_alunni_save(request):
	global n_alunni
	
	n_alunni = request.POST.get('n_alunni', '0')
	
	response = redirect('questionnaire_teacher')
	return response


def questionnaire_teacher(request, template_name=os.path.join(CARTELLA_CORRENTE, 'questionnaire_teacher.html')):
	global last_page
	
	num_page = int(request.GET.get('num_page', '1'))
	
	if num_page < last_page:
		num_page = last_page
		response = redirect('{}?num_page={}'.format(reverse('questionnaire_teacher'), num_page))
		return response
	last_page = num_page
	
	model_map = util.init_modelmap(request)
	
	model_map['num_page'] = num_page
	model_map['frasi'] = util.QUESTIONNAIRE
	model_map['intensity'] = range(util.QUESTIONNAIRE_INTENSITY)
	return TemplateResponse(request, template_name, model_map)


def questionnaire_teacher_save(request):
	
	num_page = int(request.GET.get('num_page', '1'))
	
	next_page = num_page + 1
	
	nome = request.POST.get('nome', None)
	cognome = request.POST.get('cognome', None)
	classe_alunno = request.POST.get('classe_alunno', None)
	data_nascita = request.POST.get('data_nascita', None)
	traits = dict()
	for i in range(1, util.QUESTIONNAIRE_INTENSITY + 1):
		traits[str(i)] = request.POST.get('trait' + str(i), None)
	
	connection_database = apri_connessione_db()
	connection_database.insert_questionario_teacher(nome, cognome, classe_alunno, data_nascita, traits['1'],
													traits['2'], traits['3'],
													traits['4'], traits['5'], traits['6'], traits['7'], traits['8'],
													traits['9'], traits['10'])
	
	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	max_num_page = n_alunni

	if num_page >= int(max_num_page):
		response = redirect('fine')
		return response
	
	response = redirect('{}?num_page={}'.format(reverse('questionnaire_teacher'), next_page))
	return response


def fine(request, template_name=os.path.join(CARTELLA_CORRENTE, 'fine.html')):
	model_map = util.init_modelmap(request)
	return TemplateResponse(request, template_name, model_map)
