# Generated by Django 5.1.1 on 2024-09-23 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_cad_clientes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="clientes",
            name="status",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
