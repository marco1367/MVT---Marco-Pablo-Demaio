from tkinter import font
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from AppMVT.models import Familiar


# Create your views here.
def familiares(request):
    
    familiar1 = Familiar(
        nombre='Horacio Agustin', 
        apellido = 'Demaio',
        edad = 23,
        fechaCumpleaños = '1998-10-09',
        realacionParental= 'hermano'
    )

    familiar2 = Familiar(
        nombre='Mila Florencia', 
        apellido = 'Gomez Beret',
        edad = 62,
        fechaCumpleaños = '1960-02-16',
        realacionParental= 'madre'
    )

    familiar3 = Familiar(
        nombre='Guido Dante', 
        apellido = 'Demaio',
        edad = 28,
        fechaCumpleaños = '1994-11-30',
        realacionParental= 'hermano'
    )

    familiar4 = Familiar(
        nombre='Mila Florencia', 
        apellido = 'Maestri',
        edad = 36,
        fechaCumpleaños = '1986-02-14',
        realacionParental= 'hermana'
    )

    familiar5 = Familiar(
        nombre='Maria Pia', 
        apellido = 'Demaio',
        edad = 9,
        fechaCumpleaños = '2013-05-03',
        realacionParental= 'hija'
    )

    familiar6 = Familiar(
        nombre='Luna FLorencia', 
        apellido = 'Demaio Ayala',
        edad = 0,
        fechaCumpleaños = '2022-08-25',
        realacionParental= 'hija'
    )

    dict = {
        "familiares": [familiar1, familiar2, familiar3, familiar4, familiar5, familiar6]
    }
    

    

    # for familiar in dict["familiares"]:
    #     familiar.save()

    familiar1.save()
    familiar2.save()
    familiar3.save()
    familiar4.save()
    familiar5.save()
    familiar6.save()

    template = loader.get_template('familiares.html')
    documento = template.render(dict)
    

    return HttpResponse(documento)