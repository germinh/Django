# Generated by Django 4.2.5 on 2023-09-14 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BlogId', models.CharField(max_length=30)),
                ('Title', models.CharField(max_length=200)),
                ('Author_Name', models.CharField(max_length=300)),
                ('Start_Date',  models.DateField()),
                ('End_Date' , models.DateField()),


            ],
            options={
                'db_table': 'Blog',
            },
        ),
    ]
