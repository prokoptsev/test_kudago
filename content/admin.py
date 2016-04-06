# coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.contrib import admin

from .models import Event, Place, Schedule

admin.site.register(Event)
admin.site.register(Place)
admin.site.register(Schedule)
