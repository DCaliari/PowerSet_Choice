from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse  # import functions
import random

from django.template.response import TemplateResponse

from Choice.custom_moduli import util
from Choice.custom_moduli import functions


# These are the ENDPOINT, because you can call them from outside
IMAGES_POWERSET = functions.powerset(util.IMAGES)[len(util.IMAGES)+1:]
random.shuffle(IMAGES_POWERSET)
# This is a global variable, it is created once at the start and never later.


def index(request, template_name='index.html'):  # create the function custom
    model_map={
        'page_title':'Start'

    }
    return TemplateResponse(request, template_name, model_map)


def choice_image(request, template_name='choice_image.html'):
    num_page = int(request.GET.get('page', ''))

    if (num_page>=10):
        pass
        # add final page
    next_page = num_page + 1
    images = list(IMAGES_POWERSET[num_page-1])  # fix the list
    random.shuffle(images)
    model_map={
        'page_title':'Round '+str(num_page),
        'next_page':next_page,
        'images':images
    }
    return TemplateResponse(request, template_name, model_map)


def final_page(request, template_name='final_page.html'):
    final_images = util.IMAGES
    model_map={
        'images':final_images
    }
    return TemplateResponse(request, template_name, model_map)