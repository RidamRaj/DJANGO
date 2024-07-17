# Generated by Django 5.0.6 on 2024-07-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chai", "0002_chaivariety_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Store",
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
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                (
                    "chai_varieties",
                    models.ManyToManyField(
                        related_name="stores", to="chai.chaivariety"
                    ),
                ),
            ],
        ),
    ]