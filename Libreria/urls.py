"""Libreria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from Gestion_Libreros.views import *


urlpatterns = [
    url(r'^$', Inicio.as_view(), name="Inicio"),
    url(r'^gestion_libros/$', GestionLibros.as_view(), name="GestionLibros"),
    url(r'^gestion_libros/nuevo_libro/$', NuevoLibro.as_view(), name="NuevoLibro"),
    url(r'^ajax/crear_autor/$', crear_autor, name="CrearAutor"),
    url(r'^ajax/crear_tag/$', crear_tag, name="CrearTag"),
    url(r'^ajax/crear_coleccion/$', crear_coleccion, name="CrearColeccion"),
    url(r'^ajax/crear_edicion/$', crear_edicion, name="CrearEdicion"),
    url(r'^ajax/crear_editorial/$', crear_editorial, name="CrearEditorial"),
    url(r'^ajax/eliminar_editorial/$', eliminar_editorial, name="EliminarEditorial"),
    url(r'^ajax/editar_editorial/$', editar_editorial, name="EditarEditorial"),
    url(r'^ajax/nuevo_sello/$', nuevo_sello, name="NuevoSello"),
    url(r'^gestion_libros/libro/(?P<pk>[0-9]+)$', LibroDetalles.as_view(), name="DetalleLibro"),
    url(r'^gestion_libros/editoriales/$', GestionEditoriales.as_view(), name="GestionEditoriales"),
]
