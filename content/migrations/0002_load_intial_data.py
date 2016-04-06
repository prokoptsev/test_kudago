# coding: utf-8
from __future__ import unicode_literals, absolute_import
from os import path

from django.core.management import call_command
from django.db import migrations


fixture_filename = 'initial_data.json'
fixture_dir = path.abspath(path.join(path.dirname(path.dirname(__file__)), 'fixtures'))


def load_fixture(apps, schema_editor):
    fixture_file = path.join(fixture_dir, fixture_filename)
    call_command('loaddata', fixture_file)


class Migration(migrations.Migration):
    dependencies = [
        ('content', '0001_initial'),
        ('feedmapper', '0001_initial'),
        ('auth', '0007_alter_validators_add_error_messages'),

    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
