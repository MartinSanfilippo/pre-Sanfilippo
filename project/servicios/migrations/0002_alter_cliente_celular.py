# Generated by Django 5.1 on 2024-08-29 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
