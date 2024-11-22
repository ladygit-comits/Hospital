# Generated by Django 5.1.3 on 2024-11-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('datetime', models.DateTimeField()),
                ('department', models.CharField(max_length=20)),
                ('doctor', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
    ]
