# Generated by Django 4.2.3 on 2023-07-17 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Caracteristiques",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("jardin", models.BooleanField(blank=True)),
                ("terrasse", models.BooleanField(blank=True)),
                ("balcon", models.BooleanField(blank=True)),
                ("meuble", models.BooleanField(blank=True)),
                ("cuisine", models.BooleanField(blank=True)),
                ("machine_a_laver", models.BooleanField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Emplacement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("adresse", models.CharField(max_length=255)),
                (
                    "quartier",
                    models.CharField(
                        choices=[
                            ("centre_ville", "centre_ville"),
                            ("medina", "medina"),
                            ("moulay_ismail", "moulay_ismail"),
                            ("jawhara", "jawhara"),
                            ("sidi_bouzid", "sidi_bouzid"),
                            ("bir_rami", "bir_rami"),
                            ("mehdiya", "mehdiya"),
                            ("mansouria", "mansouria"),
                            ("val_fleuri", "val_fleuri"),
                            ("ibn_tachfine", "ibn_tachfine"),
                            ("el_oulfa", "el_oulfa"),
                            ("hassan_ii", "hassan_ii"),
                            ("al_qods", "al_qods"),
                            ("al_amal", "al_amal"),
                            ("al_manar", "al_manar"),
                            ("ville_haute", "ville_haute"),
                            ("doha", "doha"),
                            ("maamora", "maamora"),
                            ("saknia", "saknia"),
                        ],
                        max_length=255,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AnnonceDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "categorie",
                    models.CharField(
                        choices=[
                            ("appartement", "appartement"),
                            ("villa", "villa"),
                            ("studio", "studio"),
                            ("chambre", "chambre"),
                            ("bureau", "bureau"),
                        ],
                        default="appartement",
                        max_length=255,
                    ),
                ),
                ("surface", models.DecimalField(decimal_places=2, max_digits=6)),
                ("prix", models.DecimalField(decimal_places=2, max_digits=8)),
                ("pieces", models.IntegerField()),
                ("salleDeBains", models.IntegerField()),
                (
                    "etat",
                    models.CharField(
                        choices=[("nouveau", "nouveau"), ("bon etat", "bon état")],
                        max_length=30,
                    ),
                ),
                (
                    "caracteristiques",
                    models.OneToOneField(
                        default="jardin",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="annonces.caracteristiques",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Annonce",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titre", models.CharField(max_length=500)),
                ("description", models.CharField(max_length=5000)),
                ("image", models.ImageField(upload_to="")),
                (
                    "annonceDetail",
                    models.OneToOneField(
                        default="1",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="annonce",
                        to="annonces.annoncedetail",
                    ),
                ),
                (
                    "emplacement",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="annonce",
                        to="annonces.emplacement",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="annonce",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
