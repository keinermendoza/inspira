# Generated by Django 4.2.7 on 2023-11-22 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_alter_categoria_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]