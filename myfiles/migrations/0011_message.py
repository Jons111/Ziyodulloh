# Generated by Django 4.2.3 on 2023-08-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0010_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.ImageField(max_length=50, upload_to='')),
                ('email', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
