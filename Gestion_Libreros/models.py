# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


default_error_messages = {
    'invalid_choice': _('El valor %r no es una opcion valida'),
    'null': _(u'Este campo es obligatorio.'),
    'blank': _(u'Este campo no puede estar en blanco.'),
    'max_length': _(u'La cantidad de caracteres debe ser de %(limit_value)s.'),
    'unique': _(u'E')
}


# def validar_isbn(value):
  #  if value.match('[0-9]'):
   #     raise ValidationError(
    #        _('%(value)s no es un numero'),
     #       params={'value': value},)


class Tag(models.Model):
    nombre = models.CharField(max_length=25, unique=True, error_messages={'unique': 'El nombre del tag no puede repetirse'}.update(default_error_messages))

    def __unicode__(self):
        return self.nombre


class Pais(models.Model):
    nombre = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=35, error_messages=default_error_messages, unique=True)
    fecha_nac = models.DateField(verbose_name="fecha de nacimiento", error_messages=default_error_messages)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, error_messages=default_error_messages)

    def __unicode__(self):
        return self.nombre


class Editorial(models.Model):
    nombre = models.CharField(max_length=45, unique=True, error_messages=dict(default_error_messages, **{'unique': 'Ya existe una editorial con el mismo nombre'}))

    def __unicode__(self):
        return self.nombre


class Sello(models.Model):
    nombre = models.CharField(max_length=25, unique=True)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre

    
class Librero(models.Model):
    nombre = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.nombre


class Coleccion(models.Model):
    nombre = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=40, error_messages=default_error_messages)
    subtitulo = models.CharField(max_length=40, null=True, error_messages=default_error_messages)
    resenna = models.TextField(max_length=600, verbose_name="reseña", error_messages=default_error_messages)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, error_messages=default_error_messages)
    tags = models.ManyToManyField(Tag)
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE, error_messages=default_error_messages)

    def __unicode__(self):
        return self.titulo


class Edicion(models.Model):
    # Tapas
    BLANDA = 1
    DURA = 2
    TAPAS = (
        (BLANDA, "Tapa blanda"),
        (DURA, "Tapa dura"),
    )

    # Encuadernado
    RUSTICA = 1
    ENCARTONADA = 2
    CARTONE = 3
    SUELTA = 4
    ENCUADERNADO = (
        (RUSTICA, "Encuadernado rustico"),
        (ENCARTONADA, "Encuadernado encartonado"),
        (CARTONE, "Encuadernado cartoné"),
        (SUELTA, "Encuadernado de tapa suelta")
    )
    # Tipo de isbn
    ISBN_10 = 1
    ISBN_13 = 2
    ISBN = {
        (ISBN_10, "ISBN"),
        (ISBN_13, "ISBN 13")
    }
    tipo_isbn = models.SmallIntegerField(choices=ISBN, error_messages=default_error_messages)
    isbn = models.CharField(max_length=13, unique=True, error_messages=default_error_messages)
    n_paginas = models.PositiveIntegerField(verbose_name="N° Paginas", error_messages=default_error_messages)
    idioma = models.CharField(max_length=20, error_messages=default_error_messages)
    cantidad = models.PositiveIntegerField(error_messages=default_error_messages)
    imagen = models.ImageField(upload_to='imagenes_edicion', error_messages=default_error_messages)
    anno = models.DateField(verbose_name="fecha de publicacion", error_messages=default_error_messages)
    tapa = models.SmallIntegerField(choices=TAPAS, error_messages=default_error_messages)
    encuadernado = models.SmallIntegerField(choices=ENCUADERNADO, error_messages=default_error_messages)
    libro = models.OneToOneField(Libro, on_delete=models.CASCADE, error_messages=default_error_messages)
    sello = models.ForeignKey(Sello, on_delete=models.CASCADE, error_messages=default_error_messages)

    def __unicode__(self):
        return self.sello.nombre


class Articulo(models.Model):
    BUENO = 1
    MAL = 2
    MUY_MAL = 3
    ESTADOS = (
        (BUENO, "Buen estado"),
        (MAL, "Mal estado"),
        (MUY_MAL, "Muy mal estado"),
    )
    estado = models.SmallIntegerField(choices=ESTADOS)
    edicion = models.ForeignKey(Edicion, on_delete=models.CASCADE)
    librero = models.ForeignKey(Librero, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.estado

