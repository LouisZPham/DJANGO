# Generated by Django 4.1.2 on 2022-10-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffID', models.IntegerField()),
                ('staffname', models.CharField(max_length=50)),
                ('staffemail', models.EmailField(max_length=70)),
            ],
        ),
    ]
