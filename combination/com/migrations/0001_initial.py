# Generated by Django 3.2.12 on 2022-05-23 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boyname', models.CharField(max_length=50)),
                ('girlname', models.CharField(max_length=50)),
            ],
        ),
    ]
