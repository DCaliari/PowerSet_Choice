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

PAGES_LANGUAGE_TEST = len(util.LANGUAGE_IMAGES)

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
	images_cq = modulo_functions.powerset(util.IMAGES_CQ, True)
	images2 = util.IMAGES2
	images3 = util.IMAGES3
	random.shuffle(images2)
	random.shuffle(images3)
	
	request.session[project_util.SESSION_KEY__POWERSET] = images_powerset
	request.session[project_util.SESSION_KEY__IMAGESCQ] = images_cq
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
		request.session[project_util.SESSION_KEY__PHASE] = util.PHASE_CQ
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
	images_cq = request.session[project_util.SESSION_KEY__IMAGESCQ]
	images2 = request.session[project_util.SESSION_KEY__IMAGES2]
	images3 = request.session[project_util.SESSION_KEY__IMAGES3]
	phase = request.session[project_util.SESSION_KEY__PHASE]
	
	# TODO: fissare questo controllo con if phase == ...
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
	
	if phase == util.PHASE_CQ:
		images = images_cq[num_page - 1]
		model_map['page_title'] = 'Scelta N. ' + str(num_page)
		cartella_img = 'images_cq'
		tipo_test = 10
	elif phase == util.PHASE_CHOICE_IMAGE:
		if num_page < len(images_powerset)+1:
			images = images_powerset[num_page - 1]
			model_map['page_title'] = 'Scelta N. ' + str(num_page)
			cartella_img = 'images_choice'
			tipo_test = 0
		elif num_page == len(images_powerset)+1:
			images = images2
			model_map['page_title'] = 'Scegli la bibita'
			cartella_img = 'images_bibite'
			tipo_test = 1
		elif num_page == len(images_powerset)+2:
			images = images3
			model_map['page_title'] = 'Scegli la merendina'
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
	images_cq = request.session[project_util.SESSION_KEY__IMAGESCQ]
	phase = request.session[project_util.SESSION_KEY__PHASE]
	
	num_page = int(request.GET.get('num_page', ''))
	tipo_test = int(request.GET.get('tipo_test', ''))
	
	connection_database = apri_connessione_db()
	# if the parameter 'choice' exists then insert in the database, otherwise nothing
	# the parameter "choice" comes from javascript code in choice_image.html - "&choice="
	if 'choice' in request.GET:
		choice = int(request.GET.get('choice', ''))
		menu = None
		if phase == util.PHASE_CQ:
			menu = json.dumps(images_cq[num_page-1])
		elif phase == util.PHASE_CHOICE_IMAGE:
			if num_page < len(images_powerset)+1:
				menu = json.dumps(images_powerset[num_page-1])
				# json handle objects (like lists) when they are in the dataset
				# using json.loads I can transform data from the table into list or other objects again
			elif num_page == len(images_powerset)+1:
				menu = json.dumps(images2)
			elif num_page == len(images_powerset)+2:
				menu = json.dumps(images3)
			
		connection_database.insert_choices_menu(id_utente, tipo_test, choice, menu)

	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	# when the pages are finished go to next problem
	if phase == util.PHASE_CQ:
		if num_page >= len(images_cq):
			request.session[project_util.SESSION_KEY__PHASE] = util.PHASE_CHOICE_IMAGE
			response = redirect('choice_image')
			return response
	elif phase == util.PHASE_CHOICE_IMAGE:
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
	
	model_map = util.init_modelmap(request, None)
	model_map['images'] = slider_images
	
	connection_database = apri_connessione_db()
	connection_database.insert_choices_slider(id_utente, None)
	
	connection_database.conn_db.commit()
	connection_database.close_conn()

	return TemplateResponse(request, template_name, model_map)


def slider_save(request):
	id_utente = request.session[project_util.SESSION_KEY__ID_UTENTE]
	slider_images = util.IMAGES
	
	connection_database = apri_connessione_db()
	
	# in the if loop enter the name from html file
	if 'store_slider' in request.POST:
		for image in slider_images:
			slider_value = request.POST.get(image, '')
			slider_list = [image, slider_value]
			slider_json = json.dumps(slider_list)
			connection_database.insert_choices_slider(id_utente, slider_json)
	
	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	response = redirect('numerical_test')
	return response


def numerical_test(request, template_name=os.path.join(CARTELLA_CORRENTE, util.TEMPLATE_NAME__NUMERICAL_TEST)):
	immagini = []
	last_page = 0
	id_utente = request.session[project_util.SESSION_KEY__ID_UTENTE]
	
	num_page = int(request.GET.get('num_page', '1'))
	
	if num_page < 4:
		immagini = util.NUMBERS
	elif num_page == 4 or 5:
		immagini = util.DICES
	elif num_page == 6:
		immagini = util.SHAPES
	elif num_page == 7:
		immagini = util.PENCILS
		
	if num_page < last_page:
		num_page = last_page
		response = redirect('{}?num_page={}'.format(reverse('numerical_test'), num_page))
		return response
	last_page = num_page
	request.session[project_util.SESSION_KEY__CHOICE_LAST_PAGE] = last_page
	
	model_map = util.init_modelmap(request, None)
	model_map['num_page'] = num_page
	model_map['immagini'] = immagini
	if num_page == 1:
		model_map['page_title'] = 'Quale numero è più vicino al 6?'
	elif num_page == 2:
		model_map['page_title'] = 'Quale numero viene prima del 3?'
	elif num_page == 3:
		model_map['page_title'] = 'Quale numero viene dopo il 4?'
	elif num_page == 4:
		model_map['page_title'] = 'Quale è la somma dei puntini?'
	elif num_page == 5:
		model_map['page_title'] = 'Quale dado contiene più puntini?'
	elif num_page == 6:
		model_map['page_title'] = 'Trova il quadrato.'
	elif num_page == 7:
		model_map['page_title'] = 'Trova la matita più lunga.'
	
	connection_database = apri_connessione_db()
	connection_database.insert_numerical_test(id_utente, num_page, None)
	
	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	return TemplateResponse(request, template_name, model_map)


def save_numerical_test(request):
	id_utente = request.session[project_util.SESSION_KEY__ID_UTENTE]
	
	num_page = int(request.GET.get('num_page', ''))

	connection_database = apri_connessione_db()
	
	# inserire il risultato del test
	if 'risultato' in request.GET:
		risultato = request.GET.get('risultato', '')
		connection_database.insert_numerical_test(id_utente, num_page, risultato)
	
	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	# when the pages are finished go to next problem
	if num_page >= util.PAGES_NUMERICAL_TEST:
		response = redirect('language_test')
		return response
	
	next_page = num_page + 1
	
	# the function reverse give the URL of the view: choice_image, the URL is http://192.168.1.9:8000/Choice/choice_image
	# we concatenate the parameter num_page with the value next_page
	response = redirect('{}?num_page={}'.format(reverse('numerical_test'), next_page))
	return response


def language_test(request, template_name=os.path.join(CARTELLA_CORRENTE, util.TEMPLATE_NAME__LANGUAGE_TEST)):
	last_page = 0
	id_utente = request.session[project_util.SESSION_KEY__ID_UTENTE]
	
	num_page = int(request.GET.get('num_page', '0'))
	
	# I go and take different images for each num_page in the language test
	immagini = util.LANGUAGE_IMAGES[num_page]
	
	if num_page < last_page:
		num_page = last_page
		response = redirect('{}?num_page={}'.format(reverse('language_test'), num_page))
		return response
	last_page = num_page
	request.session[project_util.SESSION_KEY__CHOICE_LAST_PAGE] = last_page
	
	model_map = util.init_modelmap(request, None)
	model_map['num_page'] = num_page
	model_map['immagini'] = immagini
	model_map['page_title'] = "Scegli l'immagine corretta"
	
	connection_database = apri_connessione_db()
	connection_database.insert_language_test(id_utente, num_page, None)
	
	connection_database.conn_db.commit()
	connection_database.close_conn()
	
	return TemplateResponse(request, template_name, model_map)


def save_language_test(request):
	id_utente = request.session[project_util.SESSION_KEY__ID_UTENTE]
	
	num_page = int(request.GET.get('num_page', ''))
	
	connection_database = apri_connessione_db()
	
	# inserire il risultato del test
	if 'risultato' in request.GET:
		risultato = request.GET.get('risultato', '')
		connection_database.insert_language_test(id_utente, num_page, risultato)
	
	connection_database.conn_db.commit()
	connection_database.close_conn()

	# when the pages are finished go to next problem
	if num_page+1 >= PAGES_LANGUAGE_TEST:
		response = redirect('final_page_C')
		return response
	
	next_page = num_page + 1
	
	# the function reverse give the URL of the view: choice_image, the URL is http://192.168.1.9:8000/Choice/choice_image
	# we concatenate the parameter num_page with the value next_page
	response = redirect('{}?num_page={}'.format(reverse('language_test'), next_page))
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
	image_payoff = random.choice(images_payoff)

	model_map = util.init_modelmap(request, None)
	model_map['page_title'] = 'Fine'
	model_map['image_payoff'] = image_payoff
	model_map['choices'] = images_payoff
	return TemplateResponse(request, template_name, model_map)
