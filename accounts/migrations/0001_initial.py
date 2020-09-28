# Generated by Django 3.1 on 2020-09-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DesignProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Owner', models.CharField(max_length=255)),
                ('ArchDesign', models.CharField(max_length=255)),
                ('StructureType', models.CharField(max_length=255)),
                ('Story', models.CharField(max_length=255)),
                ('Area', models.CharField(max_length=255)),
                ('Service', models.CharField(max_length=225)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
