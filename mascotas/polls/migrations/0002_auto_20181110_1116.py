# Generated by Django 2.1.3 on 2018-11-10 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='color',
            field=models.TextField(max_length=20),
        ),
    ]