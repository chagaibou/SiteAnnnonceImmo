# Generated by Django 4.2.3 on 2023-07-17 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("annonces", "0002_alter_annonce_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="annonce",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
    ]
