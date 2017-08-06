# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Tag(models.Model):
    nombre = models.CharField(max_length=25)

    def __unicode__(self):
        return self.nombre


class Pais(models.Model):
    nombre = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=35)
    fecha_nac = models.DateField(verbose_name="fecha de nacimiento")
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre


class Editorial(models.Model):
    nombre = models.CharField(max_length=45)

    def __unicode__(self):
        return self.nombre


class Sello(models.Model):
    nombre = models.CharField(max_length=25)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre

    
class Librero(models.Model):
    nombre = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nombre


class Genero(models.Model):
    nombre = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nombre


class Coleccion(models.Model):
    nombre = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40, null=True)
    resenna = models.TextField(max_length=600)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    generos = models.ManyToManyField(Genero)
    tags = models.ManyToManyField(Tag)
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE)
    librero = models.ForeignKey(Librero)

    def __unicode__(self):
        return self.titulo


class Edicion(models.Model):
    #Tapas
    BLANDA = 1
    DURA = 2
    TAPAS = (
        (BLANDA, "Tapa blanda"),
        (DURA, "Tapa dura"),
    )

    #Encuadernado
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

    isbn_10 = models.CharField(max_length=10)
    isbn_13 = models.CharField(max_length=13)
    n_paginas = models.PositiveIntegerField()
    idioma = models.CharField(max_length=20)
    cantidad = models.PositiveIntegerField()
    anno = models.DateField(verbose_name="fecha de publicacion")
    tapa = models.SmallIntegerField(choices=TAPAS)
    encuadernado = models.SmallIntegerField(choices=ENCUADERNADO)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    sello = models.ForeignKey(Sello, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.sello.nombre


class Imagen(models.Model):
    nombre = models.CharField(max_length=250)
    n = models.ImageField
    edicion = models.OneToOneField(Edicion)

    def __unicode__(self):
        return self.nombre


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

