# Generated by Django 5.0.2 on 2024-11-27 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tumbuhan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaTanam', models.CharField(max_length=50)),
                ('jenisTanam', models.CharField(max_length=50)),
                ('deskripsiTanam', models.CharField(max_length=250)),
            ],
        ),
    ]
