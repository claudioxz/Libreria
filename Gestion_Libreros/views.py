# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, CreateView, DetailView
from forms import EdicionForm, SelloForm
from models import Libro, Pais, Autor, Tag, Coleccion, Editorial, Edicion


class Inicio(TemplateView):
    template_name = "Gestion_Libreros/index.html"

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context["titulo"] = "Inicio"
        context["ultimos_libros"] = Libro.objects.all()[:5]
        return context


class GestionEditoriales(TemplateView):
    template_name = "Gestion_Libreros/editoriales.html"

    def get_context_data(self, **kwargs):
        context = super(GestionEditoriales, self).get_context_data(**kwargs)
        context["titulo"] = "Editoriales"
        context["editoriales"] = list(reversed(Editorial.objects.all()[:15]))
        return context


class GestionLibros(TemplateView):
    template_name = "Gestion_Libreros/gestion_libros.html"

    def get_context_data(self, **kwargs):
        context = super(GestionLibros, self).get_context_data(**kwargs)
        context["titulo"] = "Gestion de libros"
        context["libros"] = Libro.objects.all()[:15]
        return context


class NuevoLibro(CreateView):
    success_url = 'http://127.0.0.1:8000/gestion_libros/'
    template_name = "Gestion_Libreros/nuevo_libro.html"
    model = Libro
    fields = ["titulo", "subtitulo", "resenna", "autor", "tags", "coleccion"]

    def get_context_data(self, **kwargs):
        context = super(NuevoLibro, self).get_context_data(**kwargs)
        context["titulo"] = "Nuevo Libro"
        context["paises"] = Pais.objects.all()
        return context


class LibroDetalles(DetailView):
    model = Libro
    template_name = "Gestion_Libreros/libro.html"

    def get_context_data(self, **kwargs):
        context = super(LibroDetalles, self).get_context_data(**kwargs)
        context["titulo"] = self.object.titulo
        context["formEdicion"] = EdicionForm
        context["formSello"] = SelloForm
        return context


def crear(modelo, data={}):
    try:
        modelo.full_clean()
        modelo.save()
        data["nombre"] = modelo.nombre
        data["id"] = modelo.id
        data["error"] = False
        return JsonResponse(data)
    except ValidationError as e:
        data["error"] = True
        data.update(e.message_dict)
        return JsonResponse(data)
    except IntegrityError as i:
        data["error"] = True
        data.update(i.message_dict)
        return JsonResponse(data)


# Ajax views

def crear_edicion(request):
    edicion_form = EdicionForm(request.POST)
    data = {}
    if edicion_form.is_valid():
        e = edicion_form.save()
        data["edicion"] = e
    else:
        data["error"] = True
        data.update(edicion_form.errors)
    return JsonResponse(data)


def crear_editorial(request):
    nombre = request.GET.get('nombre', None)
    data = {}
    if nombre == "":
        data["error"] = True
        data["nombre"] = "Debe ingresar un nombre para la editorial."
        return JsonResponse(data)
    return crear(Editorial(nombre=nombre))


def crear_autor(request):
    nombre = request.GET.get('nombre', None)
    fecha_nac = request.GET.get('fecha_nac', None)
    pais = request.GET.get('pais', None)
    data = {}
    if nombre == "":
        data["nombre"] = "Debe ingresar un nombre."
    if fecha_nac == "":
        data["fecha_nac"] = "Debe ingresar una fecha."
    if pais == "":
        data["pais"] = "Debe seleccionar un pais."
    if data:
        data["error"] = True
        return JsonResponse(data)
    return crear(Autor(nombre=nombre, fecha_nac=fecha_nac, pais=Pais.objects.get(pk=pais)))


def crear_tag(request):
    nombre = request.GET.get('nombre', None)
    data = {}
    if nombre == "":
        data["error"] = True
        data["nombre"] = "Debe ingresar un nombre para el tag."
        return JsonResponse(data)

    return crear(Tag(nombre=nombre))


def crear_coleccion(request):
    nombre = request.GET.get('nombre', None)
    data = {}
    if nombre == "":
        data["error"] = True
        data["nombre"] = "Debe ingresar un nombre para la coleccion"
        return JsonResponse(data)
    return crear(Coleccion(nombre=nombre))


def nuevo_sello(request):
    sello_form = SelloForm(request.POST)
    data = {}
    if sello_form.is_valid():
        s = sello_form.save()
        data["nombre"] = s.nombre
        data["id"] = s.id
    else:
        data["error"] = True
        data.update(sello_form.errors)
    return JsonResponse(data)


@csrf_exempt
def eliminar_editorial(request):
    e = Editorial.objects.get(pk=request.GET.get('pk')).delete()
    return JsonResponse({"response": e})


def editar_editorial(request):
    e = Editorial.objects.get(pk=request.GET.get('pk'))
    e.nombre = request.GET.get('nombre')
    return crear(e)


