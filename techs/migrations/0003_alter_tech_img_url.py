# Generated by Django 4.1.4 on 2022-12-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("techs", "0002_alter_tech_img_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tech",
            name="img_url",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
