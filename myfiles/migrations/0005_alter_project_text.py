# Generated by Django 4.2.3 on 2023-07-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0004_remove_project_narxi_project_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='text',
            field=models.TextField(verbose_name=''),
        ),
    ]
