# Generated by Django 2.1.7 on 2019-08-15 18:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0005_auto_20190816_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branches',
            name='semesters',
            field=models.ManyToManyField(blank=True, to='analysis.Semesters'),
        ),
        migrations.AlterField(
            model_name='modules',
            name='questions',
            field=models.ManyToManyField(blank=True, to='analysis.Questions'),
        ),
        migrations.AlterField(
            model_name='questionpapers',
            name='questions',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='semesters',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='analysis.Subjects'),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='modules',
            field=models.ManyToManyField(blank=True, to='analysis.Modules'),
        ),
    ]
