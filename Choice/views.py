import json
import os
import random

from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse

from Choice.custom_moduli import util
from moduli import modulo_django
from moduli import modulo_functions
from moduli import modulo_system
from moduli_custom_project import modulo_database
from moduli_custom_project import project_util


# This is a global variable, it is created once at the start and never modified later.
CARTELLA_CORRENTE = os.path.basename(os.path.dirname(os.path.realpath(__file__)))

PAGES_LOGIC_TEST = len(util.LOGIC_IMAGES)

###############################################################################################


# function to open the connection to the database
def apri_connessione_db():
	path_db = project_util.FULLPATH_DATABASE
	is_db_new = modulo_system.dimensione_file(path_db) <= 0
	database = modulo_database.Database(path_db)		# crea l'oggetto e apre la connessione
	if is_db_new:										# crea le tabelle solo se non ci sono gia'
		database.schema()
	return database


#################################################################################################


# These are the ENDPOINT, because you can call them from outside
def index(request, template_name=os.path.join(CARTELLA_CORRENTE, util.TEMPLATE_NAME__INDEX)):
	
	images_powerset = modulo_functions.powerset(util.IMAGES, True)
	images_powerset = modulo_functions.shuffle_powerset(images_powerset)
	
	images2 = util.IMAGES2
	images3 = util.IMAGES3
	random.shuffle(images2)
	random.shuffle(images3)
	
	request.session[project_util.SESSION_KEY__POWERSET] = images_powerset
	
	request.session[project_util.SESSION_KEY__IMAGES2] = images2
	request.session[project_util.SESSION_KEY__IMAGES3] = images3
	
	model_map = util.init_modelmap(request, None)
	return TemplateResponse(request, template_name, model_map)


def questionnaire_kids(request, template_name=os.path.join(CARTELLA_CORRENTE, util.TEMPLATE_NAME__QUESTIONARIO_KIDS)):
	model_map = util.init_modelmap(request, None)
	return TemplateResponse(request, template_name, model_map)


def questionnaire_kids_save(request):
	nome = request.POST.get('nome', None)
	cognome = request.POST.get('cognome', None)
	scuola = request.POST.get('scuola', None)
	classe = request.POST.get('classe', None)
	peso = request.POST.get('peso', None)
	altezza = request.POST.get('altezza', None)
	sesso = request.POST.get('sesso', None)
	
	connection_database = apri_connessione_db()
	connection_database.insert_utente_bambino(nome, cognome, scuola, classe, peso, altezza, sesso)

	# get the last id created in the database
	id_utente = connection_database.cursor_db.lastrowid
	
	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	# set the value in the session.
	request.session[project_util.SESSION_KEY__ID_UTENTE] = id_utente
	request.session[project_util.SESSION_KEY__CHOICE_LAST_PAGE] = 0
	
	if modulo_django.is_localhost(request):
		response = redirect('choice_image')
	else:
		response = redirect('video')
	return response


def video(request, template_name=os.path.join(CARTELLA_CORRENTE, util.TEMPLATE_NAME__VIDEO)):
	num_page = int(request.GET.get('num_page', '0'))
	next_page = num_page + 1
	
	next_url_page = '{}?num_page={}'.format(reverse('choice_image'), next_page)
	
	model_map = util.init_modelmap(request, None)
	model_map['video'] = project_util.URL_VIDEO + '/' + util.VIDEOS[num_page]
	model_map['next_url_page'] = next_url_page
	return TemplateResponse(request, template_name, model_map)


def choice_image(request, template_name=os.path.join(CARTELLA_CORRENTE, util.TEMPLATE_NAME__CHOICE)):
	num_page = int(request.GET.get('num_page', '1'))
	last_page = request.session[project_util.SESSION_KEY__CHOICE_LAST_PAGE]
	images_powerset = request.session[project_util.SESSION_KEY__POWERSET]
	
	images2 = request.session[project_util.SESSION_KEY__IMAGES2]
	images3 = request.session[project_util.SESSION_KEY__IMAGES3]
	
	'''
	if num_page < last_page:
		num_page = last_page
		response = redirect('{}?num_page={}'.format(reverse('choice_image'), num_page))
		return response
	'''
	last_page = num_page
	request.session[project_util.SESSION_KEY__CHOICE_LAST_PAGE] = last_page
	
	model_map = util.init_modelmap(request, None)
	model_map['num_page'] = num_page
	
	cartella_img = None
	tipo_test = None
	images = None
	
	if num_page < len(images_powerset)+1:
		images = images_powerset[num_page - 1]
		model_map['page_title'] = 'Quale snack ti piace tra questi?'
		cartella_img = 'images_choice'
		tipo_test = 0
	elif num_page == len(images_powerset)+1:
		images = images2
		model_map['page_title'] = 'Quale bibita ti piace tra queste?'
		cartella_img = 'images_bibite'
		tipo_test = 1
	elif num_page == len(images_powerset)+2:
		images = images3
		model_map['page_title'] = 'Quale merendina ti piace tra queste?'
		cartella_img = 'images_snack'
		tipo_test = 2
			
	model_map['images'] = images
	model_map['cartella_img'] = cartella_img
	model_map['tipo_test'] = tipo_test
	
	id_utente = request.session[project_util.SESSION_KEY__ID_UTENTE]
	# inserisco una riga vuota per calcolo response time
	connection_database = apri_connessione_db()
	connection_database.insert_choices_menu(id_utente, tipo_test, None, None)
	
	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	return TemplateResponse(request, template_name, model_map)


def save_choice(request):
	id_utente = request.session[project_util.SESSION_KEY__ID_UTENTE]
	images_powerset = request.session[project_util.SESSION_KEY__POWERSET]
	images2 = request.session[project_util.SESSION_KEY__IMAGES2]
	images3 = request.session[project_util.SESSION_KEY__IMAGES3]
	
	num_page = int(request.GET.get('num_page', ''))
	tipo_test = int(request.GET.get('tipo_test', ''))
	
	# if the parameter 'choice' exists then insert in the database, otherwise nothing
	# the parameter "choice" comes from javascript code in choice_image.html - "&choice="
	
	if 'choice' in request.GET:
		choice = int(request.GET.get('choice', ''))
		menu = None
		if num_page < len(images_powerset)+1:
			menu = json.dumps(images_powerset[num_page-1])
			# json handle objects (like lists) when they are in the dataset
			# using json.loads I can transform data from the table into list or other objects again
		elif num_page == len(images_powerset)+1:
			menu = json.dumps(images2)
		elif num_page == len(images_powerset)+2:
			menu = json.dumps(images3)
		
		connection_database = apri_connessione_db()
		connection_database.insert_choices_menu(id_utente, tipo_test, choice, menu)
		connection_database.conn_db.commit()
		connection_database.close_conn()
	
	# when the pages are finished go to next problem

	if num_page >= len(images_powerset)+2:
		response = redirect('slider')
		return response
	
	# the function reverse give the URL of the view: choice_image, the URL is http://192.168.1.9:8000/Choice/choice_image
	# we concatenate the parameter num_page with the value next_page
	if modulo_django.is_localhost(request):
		next_page = num_page + 1
		response = redirect('{}?num_page={}'.format(reverse('choice_image'), next_page))
	else:
		response = redirect('{}?num_page={}'.format(reverse('video'), num_page))
	return response


def slider(request, template_name=os.path.join(CARTELLA_CORRENTE, util.TEMPLATE_NAME__SLIDER)):
	id_utente = request.session[project_util.SESSION_KEY__ID_UTENTE]
	slider_images = util.IMAGES
	emoji_images = util.EMOJI
	
	model_map = util.init_modelmap(request, None)
	model_map['images'] = slider_images
	model_map['emoji'] = emoji_images
	
	connection_database = apri_connessione_db()
	connection_database.insert_choices_slider(id_utente, None)
	
	connection_database.conn_db.commit()
	connection_database.close_conn()

	return TemplateResponse(request, template_name, model_map)


def slider_save(request):
	id_utente = request.session[project_util.SESSION_KEY__ID_UTENTE]
	
	if 'marks' in request.GET:
		slider_marks = request.GET.get('marks', '')
	
		connection_database = apri_connessione_db()
		connection_database.insert_choices_slider(id_utente, slider_marks)
		connection_database.conn_db.commit()
		connection_database.close_conn()

	response = redirect('logic_test')
	return response


def logic_test(request, template_name=os.path.join(CARTELLA_CORRENTE, util.TEMPLATE_NAME__LOGIC_TEST)):
	last_page = 0
	id_utente = request.session[project_util.SESSION_KEY__ID_UTENTE]
	
	num_page = int(request.GET.get('num_page', '1'))
	
	# I go and take different images for each num_page in the language test
	immagini = util.LOGIC_IMAGES[num_page-1]
	
	if num_page < last_page:
		num_page = last_page
		response = redirect('{}?num_page={}'.format(reverse('logic_test'), num_page))
		return response
	last_page = num_page
	request.session[project_util.SESSION_KEY__CHOICE_LAST_PAGE] = last_page
	
	model_map = util.init_modelmap(request, None)
	model_map['num_page'] = num_page
	model_map['immagini'] = immagini
	model_map['page_title'] = "Scegli il pezzo mancante"
	
	connection_database = apri_connessione_db()
	connection_database.insert_logic_test(id_utente, num_page, None)
	
	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	return TemplateResponse(request, template_name, model_map)


def save_logic_test(request):
	id_utente = request.session[project_util.SESSION_KEY__ID_UTENTE]
	
	num_page = int(request.GET.get('num_page', ''))
	
	connection_database = apri_connessione_db()
	
	# inserire il risultato del test
	if 'risultato' in request.GET:
		risultato = request.GET.get('risultato', '')
		connection_database.insert_logic_test(id_utente, num_page, risultato)
	
	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	# when the pages are finished go to next problem
	if num_page >= PAGES_LOGIC_TEST:
		response = redirect('final_page_C')
		return response
	
	next_page = num_page + 1
	
	# the function reverse give the URL of the view: choice_image, the URL is http://192.168.1.9:8000/Choice/choice_image
	# we concatenate the parameter num_page with the value next_page
	response = redirect('{}?num_page={}'.format(reverse('logic_test'), next_page))
	return response


def final_page(request, template_name=os.path.join(CARTELLA_CORRENTE, util.TEMPLATE_NAME__FINAL_PAGE)):
	id_utente = request.session[project_util.SESSION_KEY__ID_UTENTE]
	# leggo dal db
	connection_database = apri_connessione_db()
	choices = connection_database.select_choices_menu(id_utente)
	connection_database.close_conn()
	# elaboro le scelte
	images_payoff = []
	for choice in choices:
		tipo_test = choice['tipo_test']
		# choice e' la riga della tabella, per selezionare una colonna usare le parentesi quadre come un array
		num_choice = choice['choice']
		menu = choice['menu']
		if menu is not None:
			menu = json.loads(menu)
			image_chosen = menu[num_choice]
			image_chosen = os.path.join(project_util.from_tipo_test_to_cartella_immagini(tipo_test), image_chosen)
			images_payoff.append(image_chosen)
	# scelgo un'immagine a caso
	image_payoff = random.choice(images_payoff[1:10])
	
	model_map = util.init_modelmap(request, None)
	model_map['page_title'] = 'Fine'
	model_map['image_payoff'] = image_payoff
	model_map['choices'] = images_payoff
	return TemplateResponse(request, template_name, model_map)
