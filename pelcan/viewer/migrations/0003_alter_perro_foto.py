# Generated by Django 4.1 on 2024-02-02 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_perro_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='foto',
            field=models.ImageField(upload_to='viewer/static/viewer/storage/img/perros'),
        ),
    ]
