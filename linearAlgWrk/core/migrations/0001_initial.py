# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 06:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col_size', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='3', max_length=1)),
                ('row_size', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='3', max_length=1)),
                ('input_type', models.CharField(choices=[('add', 'ADD'), ('multiply', 'MULTIPLY'), ('rref', 'RREF'), ('determinant', 'DETERMINANT'), ('inverse', 'INVERSE')], max_length=12)),
                ('queried_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Var',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_length', models.IntegerField(null=True)),
                ('col_length', models.IntegerField(null=True)),
                ('row1element1', models.IntegerField(null=True)),
                ('row1element2', models.IntegerField(null=True)),
                ('row1element3', models.IntegerField(null=True)),
                ('row1element4', models.IntegerField(null=True)),
                ('row1element5', models.IntegerField(null=True)),
                ('row2element1', models.IntegerField(null=True)),
                ('row2element2', models.IntegerField(null=True)),
                ('row2element3', models.IntegerField(null=True)),
                ('row2element4', models.IntegerField(null=True)),
                ('row2element5', models.IntegerField(null=True)),
                ('row3element1', models.IntegerField(null=True)),
                ('row3element2', models.IntegerField(null=True)),
                ('row3element3', models.IntegerField(null=True)),
                ('row3element4', models.IntegerField(null=True)),
                ('row3element5', models.IntegerField(null=True)),
                ('row4element1', models.IntegerField(null=True)),
                ('row4element2', models.IntegerField(null=True)),
                ('row4element3', models.IntegerField(null=True)),
                ('row4element4', models.IntegerField(null=True)),
                ('row4element5', models.IntegerField(null=True)),
                ('row5element1', models.IntegerField(null=True)),
                ('row5element2', models.IntegerField(null=True)),
                ('row5element3', models.IntegerField(null=True)),
                ('row5element4', models.IntegerField(null=True)),
                ('row5element5', models.IntegerField(null=True)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to='core.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='output',
            name='endVar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='endVar', to='core.Var'),
        ),
        migrations.AddField(
            model_name='output',
            name='startVar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='startVar', to='core.Var'),
        ),
    ]
