# Generated by Django 4.0.3 on 2022-04-15 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modipy_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modipy_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]