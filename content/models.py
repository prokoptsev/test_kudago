# coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Event(models.Model):
    title = models.CharField("Название", max_length=255)
    is_free = models.NullBooleanField("Бесплатное событие", null=True, blank=True)
    age_restricted = models.CharField("Возрастная категория", max_length=3, null=True, blank=True)
    text = models.TextField("Описание", null=True, blank=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Place(models.Model):
    title = models.CharField("Название", max_length=255)
    city = models.CharField("Город", max_length=255, null=True, blank=True)
    address = models.CharField("Адрес", max_length=255, null=True, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    text = models.TextField("Описание", null=True, blank=True)
    events = models.ManyToManyField("Event", through="Schedule")

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Schedule(models.Model):
    event = models.ForeignKey("Event")
    place = models.ForeignKey("Place")
    date = models.DateField("Дата", null=True, blank=True)
    start = models.TimeField("Время начала", null=True, blank=True)
    finish = models.TimeField("Время окончания", null=True, blank=True)

    def __str__(self):
        view = "{self.date} {self.start}".format(self=self)
        if self.finish:
            return "{}-{}".format(view, self.finish)
        return view
