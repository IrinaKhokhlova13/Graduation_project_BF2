# Generated by Django 4.2.14 on 2024-07-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diagnostic_center", "0003_remove_doctor_direction_doctor_direction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="description",
            field=models.CharField(verbose_name="артикул"),
        ),
    ]
