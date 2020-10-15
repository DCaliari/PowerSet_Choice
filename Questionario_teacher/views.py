import os

from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse

from Questionario_teacher.beans.formbeans.QuestionarioTeacherFormBean import QuestionarioTeacherFormBean
from Questionario_teacher.beans.formbeans.PreFormBean import PreFormBean
from Questionario_teacher.custom_moduli import util
from moduli import modulo_system
from moduli_custom_project import modulo_database
from moduli_custom_project import project_util


# get l'ultima parte del path della cartella corrente
CARTELLA_CORRENTE = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

last_page = 0
preFormBean = None


###############################################################################################


# function to open the connection to the database
def apri_connessione_db():
	path_db = project_util.FULLPATH_DB_POWERSET
	is_db_new = modulo_system.dimensione_file(path_db) <= 0
	database = modulo_database.Database(path_db)  # crea l'oggetto e apre la connessione
	if is_db_new:  # crea le tabelle solo se non ci sono gia'
		database.schema()
	return database


#################################################################################################


# These are the ENDPOINT, because you can call them from outside
def index(request, template_name=os.path.join(CARTELLA_CORRENTE, util.TEMPLATE_NAME__INDEX)):
	global last_page
	
	last_page = 0
	model_map = util.init_modelmap(request, None)
	return TemplateResponse(request, template_name, model_map)#TODO: adeguare html come fatto in choice


def numero_alunni(request, template_name=os.path.join(CARTELLA_CORRENTE, util.TEMPLATE_NAME__NUMERO_ALUNNI)):
	model_map = util.init_modelmap(request, None)
	return TemplateResponse(request, template_name, model_map)


def numero_alunni_save(request):
	global preFormBean
	
	preFormBean = PreFormBean(request.POST)

	response = redirect('questionnaire_teacher')
	return response


def questionnaire_teacher(request, template_name=os.path.join(CARTELLA_CORRENTE, util.TEMPLATE_NAME__QUESTIONARIO_TEACHER)):
	global last_page
	
	formBean = QuestionarioTeacherFormBean()
	num_page = int(request.GET.get('num_page', 1))
	if num_page < last_page:
		num_page = last_page
		response = redirect('{}?num_page={}'.format(reverse('questionnaire_teacher'), num_page))
		return response
	last_page = num_page
	
	model_map = questionnaire_teacher__init_model_map(request, formBean, num_page)
	return TemplateResponse(request, template_name, model_map)


def questionnaire_teacher_save(request, template_name=os.path.join(CARTELLA_CORRENTE, util.TEMPLATE_NAME__QUESTIONARIO_TEACHER)):
	# TODO: perche richiamo il template nella save page?
	num_page = int(request.GET.get('num_page', 1))
	next_page = num_page + 1
	formBean = QuestionarioTeacherFormBean(request.POST)
	is_valid = formBean.is_valid()
	if not is_valid:
		model_map = questionnaire_teacher__init_model_map(request, formBean, num_page)
		return TemplateResponse(request, template_name, model_map)
	
	connection_database = apri_connessione_db()
	connection_database.insert_utenti(formBean.cleaned_data['nome'], formBean.cleaned_data['cognome'], formBean.cleaned_data['classe_alunno'],
			formBean.cleaned_data['data_nascita'])
	id_utente = connection_database.cursor_db.lastrowid
	for num_trait in range(len(util.QUESTIONNAIRE)):
		trait = request.POST.get('trait' + str(num_trait), None)
		if trait is None:
			model_map = questionnaire_teacher__init_model_map(request, formBean, num_page)
			model_map['traits_errors'] = True
			return TemplateResponse(request, template_name, model_map)
		connection_database.insert_personality_traits(id_utente, trait, num_trait)
	
	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	if num_page >= preFormBean.n_alunni:
		response = redirect('final_page')
		return response
	
	response = redirect('{}?num_page={}'.format(reverse('questionnaire_teacher'), next_page))
	return response


def fine(request, template_name=os.path.join(CARTELLA_CORRENTE, util.TEMPLATE_NAME__FINAL_PAGE)):#TODO: rinominare in final_page
	model_map = util.init_modelmap(request, None)
	return TemplateResponse(request, template_name, model_map)


def questionnaire_teacher__init_model_map(request, formBean, num_page):
	model_map = util.init_modelmap(request, formBean)
	
	model_map['page_title'] = 'Questionario ' + str(num_page)
	model_map['num_page'] = num_page
	# TODO: aggiungere il numero massimo di pagine
	model_map['frasi'] = util.QUESTIONNAIRE
	model_map['intensity'] = range(util.QUESTIONNAIRE_INTENSITY)
	return model_map

