# Generated by Django 4.2.3 on 2023-08-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0009_delete_servis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
                ('rasm', models.ImageField(upload_to='media')),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]