# Generated by Django 2.1.7 on 2019-08-15 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_remove_questions_times_asked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='weight',
        ),
        migrations.AddField(
            model_name='questions',
            name='note_for_question',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
