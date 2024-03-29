# Generated by Django 5.0.2 on 2024-03-08 20:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
        ('exam', '0001_initial'),
        ('library', '0003_alter_module_options_alter_question_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='module',
        ),
        migrations.AddField(
            model_name='exam',
            name='modules',
            field=models.ManyToManyField(through='exam.ExamModule', to='library.module', verbose_name='Modulos'),
        ),
        migrations.AlterField(
            model_name='breakdown',
            name='answer',
            field=models.CharField(default='_', max_length=5, verbose_name='Respuesta'),
        ),
        migrations.AlterField(
            model_name='breakdown',
            name='correct',
            field=models.CharField(default='_', max_length=5, verbose_name='Respuesta Correcta'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='career',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career', verbose_name='Carrera'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='score',
            field=models.FloatField(default=0.0, verbose_name='Puntaje'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.stage', verbose_name='Etapa'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualizacion'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='exammodule',
            name='score',
            field=models.FloatField(default=0.0, verbose_name='Puntaje'),
        ),
    ]
