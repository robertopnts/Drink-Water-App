# Generated by Django 4.2.4 on 2023-08-05 12:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("consumos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consumo",
            name="criado_em",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
