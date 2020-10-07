import os

from Questionario_teacher.custom_moduli import util

from django.template.response import TemplateResponse


def index(request, cartella_corrente):
	template_name=os.path.join(cartella_corrente, 'index.html')
	model_map = util.init_modelmap(request)
	return TemplateResponse(request, template_name, model_map)
