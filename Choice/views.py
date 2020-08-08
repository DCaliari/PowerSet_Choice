from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse  # import functions

from django.template.response import TemplateResponse

from Choice.custom_moduli import util
import random


# These are the ENDPOINT, because you can call them from outside


def index(request, template_name='index.html'):  # create the function custom
    model_map={
        'page_title':'Start'

    }
    return TemplateResponse(request, template_name, model_map)


def choice_image(request, template_name='choice_image.html'):
    num_page = request.GET.get('page', '')
    images = random.sample(util.IMAGES, 2)
    model_map={
        'page_title':'Round '+num_page,
        'image_1':images[0],
        'image_2':images[1]
    }

    return TemplateResponse(request, template_name, model_map)
